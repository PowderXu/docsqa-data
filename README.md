# DocsQA Data

Versioned evaluation data for the DocsQA-Repo benchmark: real community
questions answered using a pinned documentation corpus.

The benchmark implementation is maintained separately in
[Research-on-DSH](https://github.com/PowderXu/Research-on-DSH).

## Contents

| File | Contents |
| --- | --- |
| `data/questions.jsonl` | 467 question inputs and question provenance; no reference answers or gold document labels |
| `data/answers.jsonl` | 467 reference-answer records, accepted-answer provenance, evidence labels, and grading metadata |
| `data/aspects.jsonl` | 467 frozen scoring records; question and reference-answer text are joined by the evaluator |
| `data/corpus.jsonl.gz` | 4,860 documentation pages, compressed for distribution |
| `data/image_text.jsonl` | Existing image-to-text annotations |
| `data/manifest.json` | File hashes, record counts, compression metadata, and pinned upstream sources |
| `sources.json` | Documentation repositories and source revisions |
| `provenance/discussion_sources.jsonl` | 798 frozen public source identifiers and accepted-answer permalinks used during construction |
| `provenance/candidate_discovery.json` | Source-manifest hash, collection scopes and documented historical selection limits |

Questions and answers match through `question_id`. There are no
train/validation/test partitions. A line number is not a join key.

This repository owns both the evaluation release and its dataset source
manifests. The benchmark repository retains code, schemas and a pinned download
reference; downloaded data and generated documentation there are ignored caches.
The 798 construction candidates are provenance, not 798 evaluated questions.

| Documentation project | Questions |
| --- | ---: |
| GitHub Docs | 197 |
| Prisma | 125 |
| Supabase | 52 |
| Tailwind CSS | 93 |
| Total | 467 |

## Download from the benchmark

The benchmark's `evaluation/dataset/templates/dataset_source.json` pins this
repository to an exact commit and manifest SHA-256. From the benchmark root:

```sh
PYTHONPATH=evaluation:. evaluation/.venv/bin/python -m dataset.scripts.download_dataset
```

Private repositories require GitHub CLI authentication with access to this
repository (`gh auth login`). Public repositories can use unauthenticated
downloads. The downloader verifies compressed and decompressed file hashes,
checks question/answer IDs and qrels, and installs a local cache.

Plugin setup downloads the pinned data when no local source is supplied:

```sh
PYTHONPATH=evaluation:. evaluation/.venv/bin/python -m dsh_plugin.backend.prepare_plugin_data --arm hybrid
```

## Reference answers and scoring

`original_reference_answer` is the source community answer;
`normalized_answer` is a model-assisted expansion grounded in the recorded
documentation. They must not be described as identical community-authored
text. `qrel_ids` are sparse reference document labels, not an exhaustive
judgment of every potentially useful page. Frozen aspects are model-assisted
annotations, not expert-validated labels.

Existing development results retain their original cohorts. Publishing this
unpartitioned pool does not turn historical results into fresh held-out results.
Exploratory rclone and Logseq cases from the separate research work are not part
of this release.

The evaluation corpus contains the frozen text already used by the benchmark,
including existing image-derived text. Downloads do not regenerate answers,
call a model, or fetch live documentation during evaluation.

See [SCHEMA.md](SCHEMA.md) for record fields and
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for source attribution.

## Verify a checkout

```sh
python3 scripts/verify.py
```

To release a new dataset version, update the data and hashes, commit this
repository, then explicitly update the benchmark's pinned commit and manifest
hash. The benchmark never follows the latest branch implicitly.
