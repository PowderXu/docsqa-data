# Human review: two questions

[Return to the case index](README.md#case-index).

This review checks the **reference answer** and the **provided documentation**
for each sampled QA case. It is a dataset-quality review, not a score of the
three agents. There are only two labels to enter per case.

## What to judge

| Item | Question |
|---|---|
| Answer completeness | Does the normalized reference answer correctly and completely resolve the user's question? |
| Document sufficiency | Do the documents listed for this case, taken together, contain enough information to answer all essential parts of the question? |

1. Read the question and identify its actual needs, including stated constraints.
2. Read the reference answer and open the listed local documentation pages.
3. Enter the two labels. Add a short explanation for Partly, No or Cannot judge.

The answer must include the necessary explanation, steps and conditions, without
material errors. Do not treat an omitted explanation as answered merely because
a linked document contains it. The original accepted answer is available for
provenance; only the normalized benchmark answer receives the first label.

For the second label, assess the **combined document set**, not whether each
page answers the whole question. Necessary facts, steps, prerequisites and
version restrictions must be available or reasonably inferable from those pages
and the question. Matching the topic or keywords is insufficient. Equivalent
valid solutions are allowed; unrelated background and optional details are not
required. An explicit documented limitation can also answer a question.

Judge the two items independently. For example, the answer can omit a required
step even when the documents explain it: **Answer = Partly, Documents = Yes**.
Conversely, a complete answer can rely on a fact known only from the community
reply: the document set can still be insufficient.

## Labels

| Label | Answer completeness | Document sufficiency |
|---|---|---|
| Yes | Correctly resolves every essential part; no material error. | The listed pages collectively supply enough information for a complete, applicable answer. |
| Partly | Provides useful, applicable help but omits or needs correction on an essential part. | Supports part of the solution but an essential fact, step or condition is missing. |
| No | Does not resolve the main problem, or its central solution is materially wrong or inapplicable. | Does not provide enough support for the central solution. |
| Cannot judge | Evidence or reviewer expertise is insufficient to decide. | The available evidence or reviewer expertise is insufficient to decide. |

Use the pinned local pages, not today's live website. A community reply is not
local-document evidence. If a needed fact is available only in an unlisted
page, note the missing evidence instead of silently expanding the document set.
Existing image-derived text is part of the supplied question. If it is
insufficient, choose Cannot judge. A blank field is unanswered, never a pass.

## Short form

```text
Case ID:
Reviewer / date:

1. Reference answer correctly and completely answers the question:
   Yes / Partly / No / Cannot judge
   Missing or incorrect content / evidence:

2. Provided documents collectively cover all essential question requirements:
   Yes / Partly / No / Cannot judge
   Missing content / evidence:
```

## What these labels establish

These labels assess answer quality and the sufficiency of each case's supplied
document set. They do not validate individual generated aspects, their weights,
or agreement with the LLM judge. Those fields have been removed from this form.
A failure of the listed document set does not prove that the entire product
corpus lacks an answer.

Report the two label distributions separately, with unanswered and Cannot judge
counts visible. The sample oversamples multiple-document cases: use the
sampling information in the [summary](README.md#sampling) when estimating rates
for the full 467-question pool.
