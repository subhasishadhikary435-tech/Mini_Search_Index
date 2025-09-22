# indexer.py
import re
from collections import defaultdict, Counter
import json
import os

WORD_RE = re.compile(r"[a-zA-Z0-9']+")

def tokenize(text):
    """Simple tokenizer: lowercase, keep words and numbers.""" 
    return [w.lower() for w in WORD_RE.findall(text)]

def build_index(docs):
    """Build an inverted index from a list of document strings.
    Returns (inv_index, doc_lengths) where inv_index is dict term->list of (doc_id, freq).
    """ 
    inv = defaultdict(list)
    doc_lengths = {}
    for doc_id, text in enumerate(docs):
        tokens = tokenize(text)
        counts = Counter(tokens)
        doc_lengths[doc_id] = len(tokens)
        for term, freq in counts.items():
            inv[term].append((doc_id, freq))
    return dict(inv), doc_lengths

def save_index(inv, path="index.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(inv, f, ensure_ascii=False, indent=2)

def load_index(path="index.json"):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

if __name__ == "__main__":
    sample_docs = []
    docs_dir = "docs"
    if os.path.isdir(docs_dir):
        for fname in sorted(os.listdir(docs_dir)):
            full = os.path.join(docs_dir, fname)
            if os.path.isfile(full):
                with open(full, "r", encoding="utf-8") as f:
                    sample_docs.append(f.read())
    else:
        sample_docs = [
            "Python is a friendly language. I like Python for small scripts.",
            "Search engines use inverted index. The index maps terms to documents.",
            "A mini search index is fun to build."
        ]
    inv, lengths = build_index(sample_docs)
    save_index(inv, "index.json")
    print("Built index for", len(sample_docs), "docs. Saved to index.json.")
