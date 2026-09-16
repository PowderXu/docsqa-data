# Record layout

All text files use UTF-8. JSONL stores one JSON object per line.

## Questions

`question_id` is the stable identifier. `query` is the actual agent input,
including previously transcribed question images where applicable. `title`,
`project`, `dataset`, `community_category`, `source_question_id`, `source_url`,
`question_images`, and `question_modalities` provide question context and
provenance. No reference answer, qrel, or scoring rubric is supplied here.

## Answers

Each record has one matching `question_id` and preserves:

- `original_reference_answer`, `accepted_answer_url`, and
  `reference_answer_links`: source answer and provenance;
- `normalized_answer` and `normalized_answer_with_local_sources`: grounded
  reference text and local citations;
- `qrel_ids`, `qrel_anchors`, and `qrel_count`: document relevance labels;
- `normalized_claims`, `user_requirements`, and `local_document_citations`:
  reference claims and evidence;
- normalization, grading, image-evidence, and classification metadata.

The matching question text is stored only in `questions.jsonl`. Quoted user
requirements and image evidence may also appear in annotation provenance.

## Aspects

`aspects.jsonl` contains `question_id`, project and rule metadata, weighted
scoring aspects, evidence bindings, and source-coverage diagnostics. It omits
the `question` and `reference_answer` fields from the historical annotation
artifact. The evaluator joins them in memory using `question_id`. All reference
answer copies matched the canonical answers exactly. For 69 questions, the
historical annotation copy omitted the image-to-text suffix already present in
the canonical `query`; the canonical question, including that suffix, is the
authoritative input. Aspect descriptions, weights, and evidence are preserved.

## Corpus

Decompress `corpus.jsonl.gz` into `corpus.jsonl`. `doc_id` is the canonical
document identifier referenced by qrels and aspects. `rendered_text` is the
fixed searchable text; source paths, links, versions, and image-text metadata
are preserved. Local source paths are portable provenance, not a requirement
to use another user's filesystem. The benchmark materializes its searchable
workspace from these corpus records.

The manifest records both stored download hashes and uncompressed file hashes.
