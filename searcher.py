# searcher.py
from collections import defaultdict

def and_query(terms, inv):
    """Return dict doc_id -> score where docs contain ALL terms. Score = sum of freqs."""
    doc_scores = defaultdict(int)
    sets = []
    for t in terms:
        postings = inv.get(t, [])
        # postings may have string keys if loaded from JSON; ensure ints
        sets.append({int(doc_id) for doc_id, _ in postings})
    if not sets:
        return {}
    common = set.intersection(*sets)
    for t in terms:
        for doc_id, freq in inv.get(t, []):
            if int(doc_id) in common:
                doc_scores[int(doc_id)] += int(freq)
    return dict(sorted(doc_scores.items(), key=lambda x: -x[1]))

def or_query(terms, inv):
    """Return dict doc_id -> score for docs that contain any term. Score = sum of freqs."""
    doc_scores = defaultdict(int)
    for t in terms:
        for doc_id, freq in inv.get(t, []):
            doc_scores[int(doc_id)] += int(freq)
    return dict(sorted(doc_scores.items(), key=lambda x: -x[1]))

def parse_query(q):
    if '|' in q:
        terms = [t.strip().lower() for t in q.split('|') if t.strip()]
        return 'OR', terms
    else:
        terms = [t.strip().lower() for t in q.split() if t.strip()]
        return 'AND', terms

def search(q, inv):
    qtype, terms = parse_query(q)
    if qtype == 'AND':
        return and_query(terms, inv)
    else:
        return or_query(terms, inv)
