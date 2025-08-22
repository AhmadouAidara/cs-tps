# TP1 — Hash Tables

This assignment implements and compares several hash table variants.

## Contents
- `implementations.py`: `Container` ABC + `ListContainer` (baseline O(n)) + `SetContainer` (Python set).
- `hashtable.py`: `HashTableContainer` (fixed m, list chaining), `ResizingHashTableContainer` (load-factor resize), `LinkedListHashTableContainer` (singly linked chaining).
- `tests/test_basic.py`: smoke tests for add / contains / len.
- `comparison.ipynb`: optional notebook to empirically compare complexities.

## Run tests
```bash
pytest -q

## Notes
	•	Indexing: idx = hash(x) % m
	•	Load factor: α = n / m, resize when α > threshold (e.g., 0.75)
	•	Expected average complexities (with good hash distribution):
	•	add, contains: O(1) avg; worst-case O(n) if heavy collisions
---

## 3) Prochaines actions
1) Ouvre le dossier dans VS Code : `code /Users/ahmadouaidara/Desktop/IMI\ 2A/cs-tps`.
2) Lance les tests : `pytest -q` (ils devraient passer avec ces squelettes).
3) Commit & push :
   - Message : `feat(algo-tp1): scaffold hash table TP with baselines and tests`

Ensuite, on pourra ajouter le **notebook de comparaison** (mesure empirique des temps d’`add`/`contains` vs `n` et facteur de charge), et rédiger la **section complexités** plus détaillée dans le README.