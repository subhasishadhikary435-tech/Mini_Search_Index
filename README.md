# Mini Search Index (Inverted Index) — Example

This small project builds an inverted index from a few text documents and supports simple AND / OR queries.

## Files
- `indexer.py` — build the inverted index and save/load it.
- `searcher.py` — simple AND / OR search functions and ranking by term frequency.
- `run_example.py` — a runnable example showing how to build the index and run searches.
- `index.json` — (generated) saved index after running the example.
- `docs/` — optional folder for adding text files to index (not included).

## Run the example (no extra packages required)
1. Unzip the package and `cd` into the folder.
2. Run:
    ```
    python run_example.py
    ```
3. Inspect `index.json` to see the postings lists.

## Next steps (ideas)
- Add stopword removal and stemming.
- Persist index to SQLite for larger collections.
- Add phrase search by storing token positions.
- Build a small web UI (Flask) to try queries in browser.

## License
Use freely for learning. No warranty.
