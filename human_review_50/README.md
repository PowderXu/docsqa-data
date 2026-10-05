# Human review: 50 QA cases

Each case now has only **two review items**:

1. Does the reference answer correctly and completely answer the question?
2. Do the provided documents collectively cover everything needed to answer it?

Use **Yes / Partly / No / Cannot judge**, with a short explanation for a non-Yes
label. Read the [instructions](INSTRUCTIONS.md), then choose a case below.
The main answer being reviewed is the normalized benchmark reference answer;
the original community answer is retained as optional provenance.

The same 50 cases, question and answer texts, document lists and 81 complete
local documentation pages are preserved. Per-aspect dispositions, importance
ratings, normalization checks and aspect-set checks have been removed from the
active form. New labels start blank; earlier labels assessed different items
and have not been automatically converted.

The review fields are blank. Earlier working annotations were preserved in a
separate local backup and are not included in this review package.

Download this entire folder so the case and full-document links keep working.
For document sufficiency, assess the document list for the current case, not
all 81 pages in the folder. Use the supplied snapshot and account for necessary
conditions and versions. Document headers retain source paths without links
to a reviewer's local machine; the exported documentation text is unchanged.

## Sampling

The source pool contains **467 normalized QA records**. This sample intentionally emphasizes **multiple linked documents: 30 cases (60%)**, alongside **20 single-document cases (40%)**. The population has 101 multiple-document and 366 single-document cases. A link count here means the number of distinct local documentation pages cited by the accepted answer (`qrel_count`), not repeated hyperlinks, the number of outgoing links within those pages, or a claim that the question requires multiple reasoning hops.

| Dataset | Population: 1 document | Population: 2+ documents | Sample: 1 document | Sample: 2+ documents | Total sampled |
|---|---:|---:|---:|---:|---:|
| GitHub Docs | 158 | 39 | 9 | 12 | 21 |
| Prisma | 80 | 45 | 4 | 13 | 17 |
| Supabase | 41 | 11 | 2 | 3 | 5 |
| Tailwind CSS | 87 | 6 | 5 | 2 | 7 |
| **Total** | **366** | **101** | **20** | **30** | **50** |

| Distinct linked documents per answer | Sampled cases |
|---:|---:|
| 1 | 20 |
| 2 | 23 |
| 3 | 5 |
| 4 | 1 |
| 7 | 1 |

Selection uses seed **20260907**. Allocate the 20 single-document and 30 multiple-document slots separately across projects in proportion to each project’s population within that group, using the largest-remainder method; ties use the project ID alphabetically. Within each project/group, sort by the hexadecimal SHA-256 of UTF-8 `20260907\nQUESTION_ID` and take the allocated number. The `\n` denotes an actual newline. Display order uses SHA-256 of `order\n20260907\nQUESTION_ID`. Selection does not use model judgments or agent outcomes.

Because multiple-document cases are oversampled, the unweighted review percentage describes this sample. To estimate a population rate, weight each reviewed case in stratum h by `N_h / n_h`, using the population and sample counts above, and report Cannot judge cases separately. These weights apply only to population estimates from this review.

## Case index

| Case | Dataset | Question ID | Linked documents |
|---|---|---|---:|
| [Case 01](cases/case-01-prisma-prisma-24697.md) | Prisma | `prisma::prisma-24697` | 2 |
| [Case 02](cases/case-02-prisma-prisma-12782.md) | Prisma | `prisma::prisma-12782` | 2 |
| [Case 03](cases/case-03-tailwind-css-tailwind-15809.md) | Tailwind CSS | `tailwind-css::tailwind-15809` | 2 |
| [Case 04](cases/case-04-prisma-prisma-13540.md) | Prisma | `prisma::prisma-13540` | 1 |
| [Case 05](cases/case-05-prisma-prisma-28901.md) | Prisma | `prisma::prisma-28901` | 2 |
| [Case 06](cases/case-06-github-docs-23381.md) | GitHub Docs | `github-docs::23381` | 1 |
| [Case 07](cases/case-07-prisma-prisma-5982.md) | Prisma | `prisma::prisma-5982` | 1 |
| [Case 08](cases/case-08-prisma-prisma-15898.md) | Prisma | `prisma::prisma-15898` | 2 |
| [Case 09](cases/case-09-github-docs-25309.md) | GitHub Docs | `github-docs::25309` | 2 |
| [Case 10](cases/case-10-tailwind-css-tailwind-18456.md) | Tailwind CSS | `tailwind-css::tailwind-18456` | 1 |
| [Case 11](cases/case-11-github-docs-120943.md) | GitHub Docs | `github-docs::120943` | 2 |
| [Case 12](cases/case-12-prisma-prisma-20554.md) | Prisma | `prisma::prisma-20554` | 3 |
| [Case 13](cases/case-13-github-docs-24939.md) | GitHub Docs | `github-docs::24939` | 1 |
| [Case 14](cases/case-14-supabase-supabase-34352.md) | Supabase | `supabase::supabase-34352` | 1 |
| [Case 15](cases/case-15-supabase-supabase-29864.md) | Supabase | `supabase::supabase-29864` | 2 |
| [Case 16](cases/case-16-github-docs-5033.md) | GitHub Docs | `github-docs::5033` | 1 |
| [Case 17](cases/case-17-tailwind-css-tailwind-20353.md) | Tailwind CSS | `tailwind-css::tailwind-20353` | 1 |
| [Case 18](cases/case-18-prisma-prisma-29524.md) | Prisma | `prisma::prisma-29524` | 2 |
| [Case 19](cases/case-19-supabase-supabase-27860.md) | Supabase | `supabase::supabase-27860` | 2 |
| [Case 20](cases/case-20-prisma-prisma-11775.md) | Prisma | `prisma::prisma-11775` | 2 |
| [Case 21](cases/case-21-github-docs-166561.md) | GitHub Docs | `github-docs::166561` | 1 |
| [Case 22](cases/case-22-github-docs-26686.md) | GitHub Docs | `github-docs::26686` | 3 |
| [Case 23](cases/case-23-tailwind-css-tailwind-16506.md) | Tailwind CSS | `tailwind-css::tailwind-16506` | 1 |
| [Case 24](cases/case-24-prisma-prisma-9691.md) | Prisma | `prisma::prisma-9691` | 1 |
| [Case 25](cases/case-25-github-docs-166151.md) | GitHub Docs | `github-docs::166151` | 7 |
| [Case 26](cases/case-26-supabase-supabase-4133.md) | Supabase | `supabase::supabase-4133` | 1 |
| [Case 27](cases/case-27-tailwind-css-tailwind-19697.md) | Tailwind CSS | `tailwind-css::tailwind-19697` | 1 |
| [Case 28](cases/case-28-github-docs-24740.md) | GitHub Docs | `github-docs::24740` | 4 |
| [Case 29](cases/case-29-tailwind-css-tailwind-13967.md) | Tailwind CSS | `tailwind-css::tailwind-13967` | 1 |
| [Case 30](cases/case-30-prisma-prisma-14086.md) | Prisma | `prisma::prisma-14086` | 2 |
| [Case 31](cases/case-31-prisma-prisma-27294.md) | Prisma | `prisma::prisma-27294` | 2 |
| [Case 32](cases/case-32-github-docs-147941.md) | GitHub Docs | `github-docs::147941` | 1 |
| [Case 33](cases/case-33-prisma-prisma-14469.md) | Prisma | `prisma::prisma-14469` | 2 |
| [Case 34](cases/case-34-prisma-prisma-3163.md) | Prisma | `prisma::prisma-3163` | 2 |
| [Case 35](cases/case-35-supabase-supabase-45668.md) | Supabase | `supabase::supabase-45668` | 2 |
| [Case 36](cases/case-36-github-docs-23427.md) | GitHub Docs | `github-docs::23427` | 1 |
| [Case 37](cases/case-37-github-docs-22539.md) | GitHub Docs | `github-docs::22539` | 2 |
| [Case 38](cases/case-38-prisma-prisma-5405.md) | Prisma | `prisma::prisma-5405` | 2 |
| [Case 39](cases/case-39-github-docs-132566.md) | GitHub Docs | `github-docs::132566` | 3 |
| [Case 40](cases/case-40-github-docs-64750.md) | GitHub Docs | `github-docs::64750` | 1 |
| [Case 41](cases/case-41-github-docs-69168.md) | GitHub Docs | `github-docs::69168` | 2 |
| [Case 42](cases/case-42-github-docs-88452.md) | GitHub Docs | `github-docs::88452` | 3 |
| [Case 43](cases/case-43-github-docs-109354.md) | GitHub Docs | `github-docs::109354` | 1 |
| [Case 44](cases/case-44-github-docs-55027.md) | GitHub Docs | `github-docs::55027` | 2 |
| [Case 45](cases/case-45-github-docs-148518.md) | GitHub Docs | `github-docs::148518` | 3 |
| [Case 46](cases/case-46-prisma-prisma-13456.md) | Prisma | `prisma::prisma-13456` | 2 |
| [Case 47](cases/case-47-tailwind-css-tailwind-13638.md) | Tailwind CSS | `tailwind-css::tailwind-13638` | 2 |
| [Case 48](cases/case-48-github-docs-167845.md) | GitHub Docs | `github-docs::167845` | 1 |
| [Case 49](cases/case-49-prisma-prisma-11953.md) | Prisma | `prisma::prisma-11953` | 1 |
| [Case 50](cases/case-50-github-docs-188227.md) | GitHub Docs | `github-docs::188227` | 2 |

## Original packet provenance

The following benchmark-repository paths and hashes are retained from the original packet. They identify its historical inputs, not files at these paths in this data repository.

Source files are identified below so this sample can be reconstructed. SHA-256 hashes identify the exact input files; they do not expose hidden model judgments in this packet.

| Input | Original path in Research-on-DSH | SHA-256 |
|---|---|---|
| Normalized QA | `evaluation/dataset/evaluation_data/normalized/questions.jsonl` | `b573837e065894d9f1786661f524b91c3db09f02a7edbcb752becfc7657a02ca` |
| Normalized corpus | `evaluation/dataset/evaluation_data/normalized/corpus.jsonl` | `d7ade1a007c04fcec5627b1583d31f360ef5f672da466599d5b156c3ea9ff1b4` |
