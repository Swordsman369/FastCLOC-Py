# Test Record

The evidence folder contains generated records from the local validation run:

- `unit_test.log`: unittest output.
- `loc.txt`: effective Python source line count excluding blank and comment-only lines.
- `sample_table.txt`: CLI table output for fixture files.
- `sample_json.json`: CLI JSON output for fixture files.

These files can be regenerated with:

```bash
python -m unittest discover -s tests -v
python tools/count_effective_loc.py src
python -m fastcloc.cli tests/fixtures --format table
python -m fastcloc.cli tests/fixtures --format json --by-file
```
