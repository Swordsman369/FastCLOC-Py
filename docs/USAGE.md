# Usage

FastCLOC-Py exposes both a command-line interface and a Python API.

## CLI examples

```bash
fastcloc src
fastcloc src --format json --by-file
fastcloc old_version new_version --diff old_version new_version
```

## API examples

```python
from fastcloc import analyze_path
summary = analyze_path("src")
print(summary.total_code)
```

## Security notes

The scanner never executes files. It reads bounded text samples to reject binary data and only follows symlinks when explicitly requested.
