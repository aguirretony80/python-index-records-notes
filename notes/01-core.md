# Index records by unique IDs: implementation

## What the example does

Indexing enables direct lookup. Duplicate IDs are rejected rather than letting the last record silently overwrite an earlier record.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
[
  {
    "id": "a",
    "name": "Ada"
  },
  {
    "id": "b",
    "name": "Lin"
  }
]
```

Expected result:

```json
{
  "a": {
    "id": "a",
    "name": "Ada"
  },
  "b": {
    "id": "b",
    "name": "Lin"
  }
}
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
