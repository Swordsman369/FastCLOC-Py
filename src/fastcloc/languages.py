from __future__ import annotations
from .models import LanguageSpec

LANGUAGES: dict[str, LanguageSpec] = {}

LANGUAGES['Python'] = LanguageSpec(
    name='Python',
    extensions=('py', 'pyw'),
    filenames=(),
    line_comments=('#',),
    block_comments=(("'''", "'''"), ('"""', '"""')),
    shebangs=('python',),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Perl'] = LanguageSpec(
    name='Perl',
    extensions=('pl', 'pm', 'pod', 't'),
    filenames=(),
    line_comments=('#',),
    block_comments=(('=pod', '=cut'),),
    shebangs=('perl',),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Ruby'] = LanguageSpec(
    name='Ruby',
    extensions=('rb', 'rake', 'gemspec'),
    filenames=(),
    line_comments=('#',),
    block_comments=(('=begin', '=end'),),
    shebangs=('ruby',),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['JavaScript'] = LanguageSpec(
    name='JavaScript',
    extensions=('js', 'mjs', 'cjs'),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=('node',),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['TypeScript'] = LanguageSpec(
    name='TypeScript',
    extensions=('ts', 'tsx'),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Java'] = LanguageSpec(
    name='Java',
    extensions=('java',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['C'] = LanguageSpec(
    name='C',
    extensions=('c', 'h'),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['C++'] = LanguageSpec(
    name='C++',
    extensions=('cc', 'cpp', 'cxx', 'hpp', 'hh', 'hxx'),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['C#'] = LanguageSpec(
    name='C#',
    extensions=('cs',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Go'] = LanguageSpec(
    name='Go',
    extensions=('go',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Rust'] = LanguageSpec(
    name='Rust',
    extensions=('rs',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Swift'] = LanguageSpec(
    name='Swift',
    extensions=('swift',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Kotlin'] = LanguageSpec(
    name='Kotlin',
    extensions=('kt', 'kts'),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Scala'] = LanguageSpec(
    name='Scala',
    extensions=('scala', 'sc'),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Dart'] = LanguageSpec(
    name='Dart',
    extensions=('dart',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['PHP'] = LanguageSpec(
    name='PHP',
    extensions=('php', 'phtml'),
    filenames=(),
    line_comments=('//', '#'),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['R'] = LanguageSpec(
    name='R',
    extensions=('r', 'R'),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=('Rscript',),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Julia'] = LanguageSpec(
    name='Julia',
    extensions=('jl',),
    filenames=(),
    line_comments=('#',),
    block_comments=(('#=', '=#'),),
    shebangs=('julia',),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Lua'] = LanguageSpec(
    name='Lua',
    extensions=('lua',),
    filenames=(),
    line_comments=('--',),
    block_comments=(('--[[', ']]'),),
    shebangs=('lua',),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Shell'] = LanguageSpec(
    name='Shell',
    extensions=('sh', 'bash', 'zsh', 'ksh'),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=('sh', 'bash', 'zsh'),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['PowerShell'] = LanguageSpec(
    name='PowerShell',
    extensions=('ps1', 'psm1', 'psd1'),
    filenames=(),
    line_comments=('#',),
    block_comments=(('<#', '#>'),),
    shebangs=('powershell',),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['SQL'] = LanguageSpec(
    name='SQL',
    extensions=('sql',),
    filenames=(),
    line_comments=('--',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['HTML'] = LanguageSpec(
    name='HTML',
    extensions=('html', 'htm', 'xhtml'),
    filenames=(),
    line_comments=(),
    block_comments=(('<!--', '-->'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['XML'] = LanguageSpec(
    name='XML',
    extensions=('xml', 'xsd', 'xsl', 'svg'),
    filenames=(),
    line_comments=(),
    block_comments=(('<!--', '-->'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['CSS'] = LanguageSpec(
    name='CSS',
    extensions=('css',),
    filenames=(),
    line_comments=(),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['SCSS'] = LanguageSpec(
    name='SCSS',
    extensions=('scss',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Less'] = LanguageSpec(
    name='Less',
    extensions=('less',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['JSON'] = LanguageSpec(
    name='JSON',
    extensions=('json',),
    filenames=(),
    line_comments=(),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['YAML'] = LanguageSpec(
    name='YAML',
    extensions=('yaml', 'yml'),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['TOML'] = LanguageSpec(
    name='TOML',
    extensions=('toml',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['INI'] = LanguageSpec(
    name='INI',
    extensions=('ini', 'cfg', 'conf'),
    filenames=(),
    line_comments=('#', ';'),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Markdown'] = LanguageSpec(
    name='Markdown',
    extensions=('md', 'markdown'),
    filenames=(),
    line_comments=(),
    block_comments=(('<!--', '-->'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['reStructuredText'] = LanguageSpec(
    name='reStructuredText',
    extensions=('rst',),
    filenames=(),
    line_comments=('..',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Makefile'] = LanguageSpec(
    name='Makefile',
    extensions=('mk', 'mak'),
    filenames=('Makefile', 'makefile', 'GNUmakefile'),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Dockerfile'] = LanguageSpec(
    name='Dockerfile',
    extensions=('dockerfile',),
    filenames=('Dockerfile', 'dockerfile', 'Containerfile'),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['CMake'] = LanguageSpec(
    name='CMake',
    extensions=('cmake',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Objective-C'] = LanguageSpec(
    name='Objective-C',
    extensions=('m', 'mm'),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Objective-C++'] = LanguageSpec(
    name='Objective-C++',
    extensions=('M',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Haskell'] = LanguageSpec(
    name='Haskell',
    extensions=('hs', 'lhs'),
    filenames=(),
    line_comments=('--',),
    block_comments=(('{-', '-}'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Erlang'] = LanguageSpec(
    name='Erlang',
    extensions=('erl', 'hrl'),
    filenames=(),
    line_comments=('%',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Elixir'] = LanguageSpec(
    name='Elixir',
    extensions=('ex', 'exs'),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Clojure'] = LanguageSpec(
    name='Clojure',
    extensions=('clj', 'cljs', 'cljc'),
    filenames=(),
    line_comments=(';',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['F#'] = LanguageSpec(
    name='F#',
    extensions=('fs', 'fsi', 'fsx'),
    filenames=(),
    line_comments=('//',),
    block_comments=(('(*', '*)'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['OCaml'] = LanguageSpec(
    name='OCaml',
    extensions=('ml', 'mli'),
    filenames=(),
    line_comments=(),
    block_comments=(('(*', '*)'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Nim'] = LanguageSpec(
    name='Nim',
    extensions=('nim', 'nims'),
    filenames=(),
    line_comments=('#',),
    block_comments=(('#[', ']#'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Zig'] = LanguageSpec(
    name='Zig',
    extensions=('zig',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['V'] = LanguageSpec(
    name='V',
    extensions=('v',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Fortran'] = LanguageSpec(
    name='Fortran',
    extensions=('f', 'for', 'f90', 'f95', 'f03', 'f08'),
    filenames=(),
    line_comments=('!',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Pascal'] = LanguageSpec(
    name='Pascal',
    extensions=('pas', 'pp'),
    filenames=(),
    line_comments=('//',),
    block_comments=(('{', '}'), ('(*', '*)')),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Ada'] = LanguageSpec(
    name='Ada',
    extensions=('adb', 'ads'),
    filenames=(),
    line_comments=('--',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['COBOL'] = LanguageSpec(
    name='COBOL',
    extensions=('cob', 'cbl'),
    filenames=(),
    line_comments=('*',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Assembly'] = LanguageSpec(
    name='Assembly',
    extensions=('asm', 's', 'S'),
    filenames=(),
    line_comments=(';', '#'),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['MATLAB'] = LanguageSpec(
    name='MATLAB',
    extensions=('m',),
    filenames=(),
    line_comments=('%',),
    block_comments=(('%{', '%}'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Groovy'] = LanguageSpec(
    name='Groovy',
    extensions=('groovy', 'gradle'),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Visual Basic'] = LanguageSpec(
    name='Visual Basic',
    extensions=('vb', 'vbs', 'bas'),
    filenames=(),
    line_comments=("'",),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['VB.NET'] = LanguageSpec(
    name='VB.NET',
    extensions=('vbnet',),
    filenames=(),
    line_comments=("'",),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Solidity'] = LanguageSpec(
    name='Solidity',
    extensions=('sol',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Verilog'] = LanguageSpec(
    name='Verilog',
    extensions=('v', 'vh'),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['VHDL'] = LanguageSpec(
    name='VHDL',
    extensions=('vhd', 'vhdl'),
    filenames=(),
    line_comments=('--',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['SystemVerilog'] = LanguageSpec(
    name='SystemVerilog',
    extensions=('sv', 'svh'),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Tcl'] = LanguageSpec(
    name='Tcl',
    extensions=('tcl',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Awk'] = LanguageSpec(
    name='Awk',
    extensions=('awk',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=('awk',),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Sed'] = LanguageSpec(
    name='Sed',
    extensions=('sed',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=('sed',),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Prolog'] = LanguageSpec(
    name='Prolog',
    extensions=('pl', 'pro'),
    filenames=(),
    line_comments=('%',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Smalltalk'] = LanguageSpec(
    name='Smalltalk',
    extensions=('st',),
    filenames=(),
    line_comments=(),
    block_comments=(('"', '"'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Lisp'] = LanguageSpec(
    name='Lisp',
    extensions=('lisp', 'lsp'),
    filenames=(),
    line_comments=(';',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Common Lisp'] = LanguageSpec(
    name='Common Lisp',
    extensions=('cl', 'asd'),
    filenames=(),
    line_comments=(';',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Scheme'] = LanguageSpec(
    name='Scheme',
    extensions=('scm', 'ss'),
    filenames=(),
    line_comments=(';',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Racket'] = LanguageSpec(
    name='Racket',
    extensions=('rkt',),
    filenames=(),
    line_comments=(';',),
    block_comments=(('#|', '|#'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Crystal'] = LanguageSpec(
    name='Crystal',
    extensions=('cr',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Elm'] = LanguageSpec(
    name='Elm',
    extensions=('elm',),
    filenames=(),
    line_comments=('--',),
    block_comments=(('{-', '-}'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['PureScript'] = LanguageSpec(
    name='PureScript',
    extensions=('purs',),
    filenames=(),
    line_comments=('--',),
    block_comments=(('{-', '-}'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['CoffeeScript'] = LanguageSpec(
    name='CoffeeScript',
    extensions=('coffee',),
    filenames=(),
    line_comments=('#',),
    block_comments=(('###', '###'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Vue'] = LanguageSpec(
    name='Vue',
    extensions=('vue',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('<!--', '-->'), ('/*', '*/')),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Svelte'] = LanguageSpec(
    name='Svelte',
    extensions=('svelte',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('<!--', '-->'), ('/*', '*/')),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Nix'] = LanguageSpec(
    name='Nix',
    extensions=('nix',),
    filenames=(),
    line_comments=('#',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Terraform'] = LanguageSpec(
    name='Terraform',
    extensions=('tf', 'tfvars'),
    filenames=(),
    line_comments=('#', '//'),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['HCL'] = LanguageSpec(
    name='HCL',
    extensions=('hcl',),
    filenames=(),
    line_comments=('#', '//'),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Protocol Buffers'] = LanguageSpec(
    name='Protocol Buffers',
    extensions=('proto',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Thrift'] = LanguageSpec(
    name='Thrift',
    extensions=('thrift',),
    filenames=(),
    line_comments=('//', '#'),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['GraphQL'] = LanguageSpec(
    name='GraphQL',
    extensions=('graphql', 'gql'),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Razor'] = LanguageSpec(
    name='Razor',
    extensions=('cshtml', 'razor'),
    filenames=(),
    line_comments=(),
    block_comments=(('<!--', '-->'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Jinja'] = LanguageSpec(
    name='Jinja',
    extensions=('jinja', 'jinja2', 'j2'),
    filenames=(),
    line_comments=(),
    block_comments=(('{#', '#}'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Twig'] = LanguageSpec(
    name='Twig',
    extensions=('twig',),
    filenames=(),
    line_comments=(),
    block_comments=(('{#', '#}'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Mustache'] = LanguageSpec(
    name='Mustache',
    extensions=('mustache',),
    filenames=(),
    line_comments=(),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Handlebars'] = LanguageSpec(
    name='Handlebars',
    extensions=('hbs', 'handlebars'),
    filenames=(),
    line_comments=(),
    block_comments=(('{{!', '}}'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['LaTeX'] = LanguageSpec(
    name='LaTeX',
    extensions=('tex', 'sty', 'cls'),
    filenames=(),
    line_comments=('%',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['BibTeX'] = LanguageSpec(
    name='BibTeX',
    extensions=('bib',),
    filenames=(),
    line_comments=('%',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['SAS'] = LanguageSpec(
    name='SAS',
    extensions=('sas',),
    filenames=(),
    line_comments=('*',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['SPSS'] = LanguageSpec(
    name='SPSS',
    extensions=('sps',),
    filenames=(),
    line_comments=('*',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['Stata'] = LanguageSpec(
    name='Stata',
    extensions=('do', 'ado'),
    filenames=(),
    line_comments=('*', '//'),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['OpenCL'] = LanguageSpec(
    name='OpenCL',
    extensions=('cl',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['CUDA'] = LanguageSpec(
    name='CUDA',
    extensions=('cu', 'cuh'),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['GLSL'] = LanguageSpec(
    name='GLSL',
    extensions=('glsl', 'vert', 'frag'),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['MQL4'] = LanguageSpec(
    name='MQL4',
    extensions=('mq4', 'mqh'),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['MQL5'] = LanguageSpec(
    name='MQL5',
    extensions=('mq5',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang001'] = LanguageSpec(
    name='DomainLang001',
    extensions=('dl001',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang002'] = LanguageSpec(
    name='DomainLang002',
    extensions=('dl002',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang003'] = LanguageSpec(
    name='DomainLang003',
    extensions=('dl003',),
    filenames=(),
    line_comments=('#',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang004'] = LanguageSpec(
    name='DomainLang004',
    extensions=('dl004',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang005'] = LanguageSpec(
    name='DomainLang005',
    extensions=('dl005',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang006'] = LanguageSpec(
    name='DomainLang006',
    extensions=('dl006',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang007'] = LanguageSpec(
    name='DomainLang007',
    extensions=('dl007',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang008'] = LanguageSpec(
    name='DomainLang008',
    extensions=('dl008',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang009'] = LanguageSpec(
    name='DomainLang009',
    extensions=('dl009',),
    filenames=(),
    line_comments=('#',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang010'] = LanguageSpec(
    name='DomainLang010',
    extensions=('dl010',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang011'] = LanguageSpec(
    name='DomainLang011',
    extensions=('dl011',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang012'] = LanguageSpec(
    name='DomainLang012',
    extensions=('dl012',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang013'] = LanguageSpec(
    name='DomainLang013',
    extensions=('dl013',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang014'] = LanguageSpec(
    name='DomainLang014',
    extensions=('dl014',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang015'] = LanguageSpec(
    name='DomainLang015',
    extensions=('dl015',),
    filenames=(),
    line_comments=('#',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang016'] = LanguageSpec(
    name='DomainLang016',
    extensions=('dl016',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang017'] = LanguageSpec(
    name='DomainLang017',
    extensions=('dl017',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang018'] = LanguageSpec(
    name='DomainLang018',
    extensions=('dl018',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang019'] = LanguageSpec(
    name='DomainLang019',
    extensions=('dl019',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang020'] = LanguageSpec(
    name='DomainLang020',
    extensions=('dl020',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang021'] = LanguageSpec(
    name='DomainLang021',
    extensions=('dl021',),
    filenames=(),
    line_comments=('#',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang022'] = LanguageSpec(
    name='DomainLang022',
    extensions=('dl022',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang023'] = LanguageSpec(
    name='DomainLang023',
    extensions=('dl023',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang024'] = LanguageSpec(
    name='DomainLang024',
    extensions=('dl024',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang025'] = LanguageSpec(
    name='DomainLang025',
    extensions=('dl025',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang026'] = LanguageSpec(
    name='DomainLang026',
    extensions=('dl026',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang027'] = LanguageSpec(
    name='DomainLang027',
    extensions=('dl027',),
    filenames=(),
    line_comments=('#',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang028'] = LanguageSpec(
    name='DomainLang028',
    extensions=('dl028',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang029'] = LanguageSpec(
    name='DomainLang029',
    extensions=('dl029',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang030'] = LanguageSpec(
    name='DomainLang030',
    extensions=('dl030',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang031'] = LanguageSpec(
    name='DomainLang031',
    extensions=('dl031',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang032'] = LanguageSpec(
    name='DomainLang032',
    extensions=('dl032',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang033'] = LanguageSpec(
    name='DomainLang033',
    extensions=('dl033',),
    filenames=(),
    line_comments=('#',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang034'] = LanguageSpec(
    name='DomainLang034',
    extensions=('dl034',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang035'] = LanguageSpec(
    name='DomainLang035',
    extensions=('dl035',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang036'] = LanguageSpec(
    name='DomainLang036',
    extensions=('dl036',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang037'] = LanguageSpec(
    name='DomainLang037',
    extensions=('dl037',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang038'] = LanguageSpec(
    name='DomainLang038',
    extensions=('dl038',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang039'] = LanguageSpec(
    name='DomainLang039',
    extensions=('dl039',),
    filenames=(),
    line_comments=('#',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang040'] = LanguageSpec(
    name='DomainLang040',
    extensions=('dl040',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang041'] = LanguageSpec(
    name='DomainLang041',
    extensions=('dl041',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang042'] = LanguageSpec(
    name='DomainLang042',
    extensions=('dl042',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang043'] = LanguageSpec(
    name='DomainLang043',
    extensions=('dl043',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang044'] = LanguageSpec(
    name='DomainLang044',
    extensions=('dl044',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang045'] = LanguageSpec(
    name='DomainLang045',
    extensions=('dl045',),
    filenames=(),
    line_comments=('#',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang046'] = LanguageSpec(
    name='DomainLang046',
    extensions=('dl046',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang047'] = LanguageSpec(
    name='DomainLang047',
    extensions=('dl047',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang048'] = LanguageSpec(
    name='DomainLang048',
    extensions=('dl048',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang049'] = LanguageSpec(
    name='DomainLang049',
    extensions=('dl049',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang050'] = LanguageSpec(
    name='DomainLang050',
    extensions=('dl050',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang051'] = LanguageSpec(
    name='DomainLang051',
    extensions=('dl051',),
    filenames=(),
    line_comments=('#',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang052'] = LanguageSpec(
    name='DomainLang052',
    extensions=('dl052',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang053'] = LanguageSpec(
    name='DomainLang053',
    extensions=('dl053',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang054'] = LanguageSpec(
    name='DomainLang054',
    extensions=('dl054',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang055'] = LanguageSpec(
    name='DomainLang055',
    extensions=('dl055',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang056'] = LanguageSpec(
    name='DomainLang056',
    extensions=('dl056',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang057'] = LanguageSpec(
    name='DomainLang057',
    extensions=('dl057',),
    filenames=(),
    line_comments=('#',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang058'] = LanguageSpec(
    name='DomainLang058',
    extensions=('dl058',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang059'] = LanguageSpec(
    name='DomainLang059',
    extensions=('dl059',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang060'] = LanguageSpec(
    name='DomainLang060',
    extensions=('dl060',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang061'] = LanguageSpec(
    name='DomainLang061',
    extensions=('dl061',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang062'] = LanguageSpec(
    name='DomainLang062',
    extensions=('dl062',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang063'] = LanguageSpec(
    name='DomainLang063',
    extensions=('dl063',),
    filenames=(),
    line_comments=('#',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang064'] = LanguageSpec(
    name='DomainLang064',
    extensions=('dl064',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang065'] = LanguageSpec(
    name='DomainLang065',
    extensions=('dl065',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang066'] = LanguageSpec(
    name='DomainLang066',
    extensions=('dl066',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang067'] = LanguageSpec(
    name='DomainLang067',
    extensions=('dl067',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang068'] = LanguageSpec(
    name='DomainLang068',
    extensions=('dl068',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang069'] = LanguageSpec(
    name='DomainLang069',
    extensions=('dl069',),
    filenames=(),
    line_comments=('#',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang070'] = LanguageSpec(
    name='DomainLang070',
    extensions=('dl070',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang071'] = LanguageSpec(
    name='DomainLang071',
    extensions=('dl071',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang072'] = LanguageSpec(
    name='DomainLang072',
    extensions=('dl072',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang073'] = LanguageSpec(
    name='DomainLang073',
    extensions=('dl073',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang074'] = LanguageSpec(
    name='DomainLang074',
    extensions=('dl074',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang075'] = LanguageSpec(
    name='DomainLang075',
    extensions=('dl075',),
    filenames=(),
    line_comments=('#',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang076'] = LanguageSpec(
    name='DomainLang076',
    extensions=('dl076',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang077'] = LanguageSpec(
    name='DomainLang077',
    extensions=('dl077',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang078'] = LanguageSpec(
    name='DomainLang078',
    extensions=('dl078',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang079'] = LanguageSpec(
    name='DomainLang079',
    extensions=('dl079',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang080'] = LanguageSpec(
    name='DomainLang080',
    extensions=('dl080',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang081'] = LanguageSpec(
    name='DomainLang081',
    extensions=('dl081',),
    filenames=(),
    line_comments=('#',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang082'] = LanguageSpec(
    name='DomainLang082',
    extensions=('dl082',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang083'] = LanguageSpec(
    name='DomainLang083',
    extensions=('dl083',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang084'] = LanguageSpec(
    name='DomainLang084',
    extensions=('dl084',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang085'] = LanguageSpec(
    name='DomainLang085',
    extensions=('dl085',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang086'] = LanguageSpec(
    name='DomainLang086',
    extensions=('dl086',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang087'] = LanguageSpec(
    name='DomainLang087',
    extensions=('dl087',),
    filenames=(),
    line_comments=('#',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang088'] = LanguageSpec(
    name='DomainLang088',
    extensions=('dl088',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang089'] = LanguageSpec(
    name='DomainLang089',
    extensions=('dl089',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang090'] = LanguageSpec(
    name='DomainLang090',
    extensions=('dl090',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang091'] = LanguageSpec(
    name='DomainLang091',
    extensions=('dl091',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang092'] = LanguageSpec(
    name='DomainLang092',
    extensions=('dl092',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang093'] = LanguageSpec(
    name='DomainLang093',
    extensions=('dl093',),
    filenames=(),
    line_comments=('#',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang094'] = LanguageSpec(
    name='DomainLang094',
    extensions=('dl094',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang095'] = LanguageSpec(
    name='DomainLang095',
    extensions=('dl095',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang096'] = LanguageSpec(
    name='DomainLang096',
    extensions=('dl096',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang097'] = LanguageSpec(
    name='DomainLang097',
    extensions=('dl097',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang098'] = LanguageSpec(
    name='DomainLang098',
    extensions=('dl098',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang099'] = LanguageSpec(
    name='DomainLang099',
    extensions=('dl099',),
    filenames=(),
    line_comments=('#',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang100'] = LanguageSpec(
    name='DomainLang100',
    extensions=('dl100',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang101'] = LanguageSpec(
    name='DomainLang101',
    extensions=('dl101',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang102'] = LanguageSpec(
    name='DomainLang102',
    extensions=('dl102',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang103'] = LanguageSpec(
    name='DomainLang103',
    extensions=('dl103',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang104'] = LanguageSpec(
    name='DomainLang104',
    extensions=('dl104',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang105'] = LanguageSpec(
    name='DomainLang105',
    extensions=('dl105',),
    filenames=(),
    line_comments=('#',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang106'] = LanguageSpec(
    name='DomainLang106',
    extensions=('dl106',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang107'] = LanguageSpec(
    name='DomainLang107',
    extensions=('dl107',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang108'] = LanguageSpec(
    name='DomainLang108',
    extensions=('dl108',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang109'] = LanguageSpec(
    name='DomainLang109',
    extensions=('dl109',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang110'] = LanguageSpec(
    name='DomainLang110',
    extensions=('dl110',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang111'] = LanguageSpec(
    name='DomainLang111',
    extensions=('dl111',),
    filenames=(),
    line_comments=('#',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang112'] = LanguageSpec(
    name='DomainLang112',
    extensions=('dl112',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang113'] = LanguageSpec(
    name='DomainLang113',
    extensions=('dl113',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang114'] = LanguageSpec(
    name='DomainLang114',
    extensions=('dl114',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang115'] = LanguageSpec(
    name='DomainLang115',
    extensions=('dl115',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang116'] = LanguageSpec(
    name='DomainLang116',
    extensions=('dl116',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang117'] = LanguageSpec(
    name='DomainLang117',
    extensions=('dl117',),
    filenames=(),
    line_comments=('#',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang118'] = LanguageSpec(
    name='DomainLang118',
    extensions=('dl118',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang119'] = LanguageSpec(
    name='DomainLang119',
    extensions=('dl119',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang120'] = LanguageSpec(
    name='DomainLang120',
    extensions=('dl120',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang121'] = LanguageSpec(
    name='DomainLang121',
    extensions=('dl121',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang122'] = LanguageSpec(
    name='DomainLang122',
    extensions=('dl122',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang123'] = LanguageSpec(
    name='DomainLang123',
    extensions=('dl123',),
    filenames=(),
    line_comments=('#',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang124'] = LanguageSpec(
    name='DomainLang124',
    extensions=('dl124',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang125'] = LanguageSpec(
    name='DomainLang125',
    extensions=('dl125',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang126'] = LanguageSpec(
    name='DomainLang126',
    extensions=('dl126',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang127'] = LanguageSpec(
    name='DomainLang127',
    extensions=('dl127',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang128'] = LanguageSpec(
    name='DomainLang128',
    extensions=('dl128',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang129'] = LanguageSpec(
    name='DomainLang129',
    extensions=('dl129',),
    filenames=(),
    line_comments=('#',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang130'] = LanguageSpec(
    name='DomainLang130',
    extensions=('dl130',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang131'] = LanguageSpec(
    name='DomainLang131',
    extensions=('dl131',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang132'] = LanguageSpec(
    name='DomainLang132',
    extensions=('dl132',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang133'] = LanguageSpec(
    name='DomainLang133',
    extensions=('dl133',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang134'] = LanguageSpec(
    name='DomainLang134',
    extensions=('dl134',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang135'] = LanguageSpec(
    name='DomainLang135',
    extensions=('dl135',),
    filenames=(),
    line_comments=('#',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang136'] = LanguageSpec(
    name='DomainLang136',
    extensions=('dl136',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang137'] = LanguageSpec(
    name='DomainLang137',
    extensions=('dl137',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang138'] = LanguageSpec(
    name='DomainLang138',
    extensions=('dl138',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang139'] = LanguageSpec(
    name='DomainLang139',
    extensions=('dl139',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang140'] = LanguageSpec(
    name='DomainLang140',
    extensions=('dl140',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang141'] = LanguageSpec(
    name='DomainLang141',
    extensions=('dl141',),
    filenames=(),
    line_comments=('#',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang142'] = LanguageSpec(
    name='DomainLang142',
    extensions=('dl142',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang143'] = LanguageSpec(
    name='DomainLang143',
    extensions=('dl143',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang144'] = LanguageSpec(
    name='DomainLang144',
    extensions=('dl144',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang145'] = LanguageSpec(
    name='DomainLang145',
    extensions=('dl145',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang146'] = LanguageSpec(
    name='DomainLang146',
    extensions=('dl146',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang147'] = LanguageSpec(
    name='DomainLang147',
    extensions=('dl147',),
    filenames=(),
    line_comments=('#',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang148'] = LanguageSpec(
    name='DomainLang148',
    extensions=('dl148',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang149'] = LanguageSpec(
    name='DomainLang149',
    extensions=('dl149',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang150'] = LanguageSpec(
    name='DomainLang150',
    extensions=('dl150',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang151'] = LanguageSpec(
    name='DomainLang151',
    extensions=('dl151',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang152'] = LanguageSpec(
    name='DomainLang152',
    extensions=('dl152',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang153'] = LanguageSpec(
    name='DomainLang153',
    extensions=('dl153',),
    filenames=(),
    line_comments=('#',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang154'] = LanguageSpec(
    name='DomainLang154',
    extensions=('dl154',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang155'] = LanguageSpec(
    name='DomainLang155',
    extensions=('dl155',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang156'] = LanguageSpec(
    name='DomainLang156',
    extensions=('dl156',),
    filenames=(),
    line_comments=('//',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang157'] = LanguageSpec(
    name='DomainLang157',
    extensions=('dl157',),
    filenames=(),
    line_comments=('#',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang158'] = LanguageSpec(
    name='DomainLang158',
    extensions=('dl158',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang159'] = LanguageSpec(
    name='DomainLang159',
    extensions=('dl159',),
    filenames=(),
    line_comments=('#',),
    block_comments=(('/*', '*/'),),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

LANGUAGES['DomainLang160'] = LanguageSpec(
    name='DomainLang160',
    extensions=('dl160',),
    filenames=(),
    line_comments=('//',),
    block_comments=(),
    shebangs=(),
    aliases=(),
    category="programming",
    supports_strings=True,
    default_tab_width=4,
)

def iter_language_specs() -> tuple[LanguageSpec, ...]:
    return tuple(LANGUAGES.values())

def get_language_spec(name: str) -> LanguageSpec | None:
    return LANGUAGES.get(name)

def extension_index() -> dict[str, LanguageSpec]:
    index: dict[str, LanguageSpec] = {}
    for spec in LANGUAGES.values():
        for ext in spec.extensions:
            index.setdefault(ext.lower().lstrip("."), spec)
    return index

def filename_index() -> dict[str, LanguageSpec]:
    index: dict[str, LanguageSpec] = {}
    for spec in LANGUAGES.values():
        for filename in spec.filenames:
            index.setdefault(filename.lower(), spec)
    return index
