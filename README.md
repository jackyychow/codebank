# Interview Question Bank

Every interview question lives as one Python file under `questions/`.

Filename prefixes:

- `algorithm_` — LeetCode-style algorithms and data structures
- `design_` — low-level design and object-oriented problems
- `python_` — Python language and runtime questions

Each file keeps the question as comments above the implementation. Tests and small runnable examples stay at the bottom of the same file. Source information is included as a comment when known.

Useful searches:

```bash
rg --files questions | rg '^questions/algorithm_'
rg --files questions | rg '^questions/design_'
rg -l 'Source: Tower Capital' questions/
rg -l 'Question:.*heap' questions/
```

Machine-learning material is maintained separately from this question bank.
