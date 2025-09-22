# run_example.py
from indexer import build_index
from searcher import search
import json

docs = [
    "Python is a friendly language. I like Python for small scripts.",
    "Search engines use inverted index. The index maps terms to documents.",
    "A mini search index is fun to build."
]

inv, lengths = build_index(docs)
print("--- Index built ---\nTerms sample:", list(inv.keys())[:12])

tests = [
    "python",
    "index",
    "python index",
    "python | index"
]

for q in tests:
    res = search(q, inv)
    print(f"\nQuery: '{q}' -> Results (doc_id:score):", res)

# Save the index to inspect
with open('index.json', 'w', encoding='utf-8') as f:
    json.dump(inv, f, ensure_ascii=False, indent=2)
print('\nSaved index.json (inspect to see postings lists).')
