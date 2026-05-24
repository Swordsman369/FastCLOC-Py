from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from .models import LanguageSpec


class LineKind(str, Enum):
    BLANK = "blank"
    COMMENT = "comment"
    CODE = "code"


@dataclass
class ParseState:
    block_end: str | None = None

    @property
    def in_block(self) -> bool:
        return self.block_end is not None

    def enter_block(self, end: str) -> None:
        self.block_end = end

    def leave_block(self) -> None:
        self.block_end = None


def find_unquoted_token(text: str, tokens: tuple[str, ...], start: int = 0) -> tuple[int, str] | None:
    if not tokens:
        return None
    quote: str | None = None
    escaped = False
    index = start
    while index < len(text):
        char = text[index]
        if escaped:
            escaped = False
            index += 1
            continue
        if char == "\\":
            escaped = True
            index += 1
            continue
        if quote:
            if char == quote:
                quote = None
            index += 1
            continue
        if char in {"'", '"', "`"}:
            quote = char
            index += 1
            continue
        for token in tokens:
            if text.startswith(token, index):
                return index, token
        index += 1
    return None


def first_token_position(text: str, tokens: tuple[str, ...]) -> tuple[int, str] | None:
    best: tuple[int, str] | None = None
    for token in tokens:
        pos = text.find(token)
        if pos >= 0 and (best is None or pos < best[0]):
            best = (pos, token)
    return best


def remove_comment_ranges(line: str, spec: LanguageSpec, state: ParseState) -> tuple[str, bool]:
    cursor = 0
    code_parts: list[str] = []
    saw_comment = False
    while cursor < len(line):
        if state.in_block:
            end = state.block_end or ""
            end_pos = line.find(end, cursor)
            saw_comment = True
            if end_pos < 0:
                cursor = len(line)
                break
            cursor = end_pos + len(end)
            state.leave_block()
            continue
        starts = tuple(pair[0] for pair in spec.block_comments)
        line_tokens = spec.line_comments
        block_hit = find_unquoted_token(line, starts, cursor)
        line_hit = find_unquoted_token(line, line_tokens, cursor)
        candidates = [item for item in [block_hit, line_hit] if item is not None]
        if not candidates:
            code_parts.append(line[cursor:])
            break
        pos, token = min(candidates, key=lambda item: item[0])
        code_parts.append(line[cursor:pos])
        saw_comment = True
        if token in line_tokens:
            cursor = len(line)
            break
        end_token = next(end for start, end in spec.block_comments if start == token)
        end_pos = line.find(end_token, pos + len(token))
        if end_pos < 0:
            state.enter_block(end_token)
            cursor = len(line)
            break
        cursor = end_pos + len(end_token)
    return "".join(code_parts), saw_comment


def classify_line(line: str, spec: LanguageSpec, state: ParseState) -> LineKind:
    stripped = line.strip()
    if not stripped and not state.in_block:
        return LineKind.BLANK
    if not state.in_block:
        for start, end in spec.block_comments:
            if start in {"\"\"\"", "'''"} and line.lstrip().startswith(start):
                after = line.lstrip()[len(start):]
                if end in after:
                    tail = after.split(end, 1)[1]
                    return LineKind.CODE if tail.strip() else LineKind.COMMENT
                state.enter_block(end)
                return LineKind.COMMENT
    code_without_comments, saw_comment = remove_comment_ranges(line.rstrip("\n"), spec, state)
    if code_without_comments.strip():
        return LineKind.CODE
    if saw_comment or state.in_block:
        return LineKind.COMMENT
    return LineKind.BLANK


def count_lines(lines: list[str], spec: LanguageSpec) -> tuple[int, int, int]:
    state = ParseState()
    blank = 0
    comment = 0
    code = 0
    for line in lines:
        kind = classify_line(line, spec, state)
        if kind == LineKind.BLANK:
            blank += 1
        elif kind == LineKind.COMMENT:
            comment += 1
        else:
            code += 1
    return blank, comment, code
