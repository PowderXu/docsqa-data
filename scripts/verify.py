"""Validate a dataset checkout with only the Python standard library."""

import gzip
import hashlib
import json
from pathlib import Path


root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / "data/manifest.json").read_text())
rows = {}
for name, expected in manifest["files"].items():
    download = manifest["downloads"][name]
    stored = (root / download["path"]).read_bytes()
    assert len(stored) == download["bytes"], name
    assert hashlib.sha256(stored).hexdigest() == download["sha256"], name
    raw = gzip.decompress(stored) if download["compression"] == "gzip" else stored
    assert len(raw) == expected["bytes"], name
    assert hashlib.sha256(raw).hexdigest() == expected["sha256"], name
    rows[name] = [json.loads(line) for line in raw.splitlines() if line.strip()]
questions, answers = rows["questions.jsonl"], rows["answers.jsonl"]
question_ids = {row["question_id"] for row in questions}
answer_ids = {row["question_id"] for row in answers}
assert len(question_ids) == len(questions) == manifest["questions"]
assert len(answer_ids) == len(answers) == manifest["answers"]
assert question_ids == answer_ids
assert all("normalized_answer" not in row and "qrel_ids" not in row for row in questions)
assert all("query" not in row for row in answers)
assert all("split" not in row for row in questions + answers)
corpus_ids = {row["doc_id"] for row in rows["corpus.jsonl"]}
assert len(corpus_ids) == len(rows["corpus.jsonl"]) == manifest["documents"]
assert all(set(row["qrel_ids"]) <= corpus_ids for row in answers)
if "aspects.jsonl" in rows:
    aspects = rows["aspects.jsonl"]
    assert len(aspects) == len(questions)
    assert {row["question_id"] for row in aspects} == question_ids
    assert all("question" not in row and "reference_answer" not in row for row in aspects)
print(f"Verified {len(questions)} questions, {len(answers)} answers, and {len(corpus_ids)} documents.")
