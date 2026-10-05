<a id="case-08"></a>

# Case 08

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-07-prisma-prisma-5982.md) | [Next case](case-09-github-docs-25309.md)

**Dataset:** Prisma  
**Question ID:** `prisma::prisma-15898`  
**Distinct linked documents:** 2  
**Original discussion:** [Source](https://github.com/prisma/prisma/discussions/15898)  
**Accepted answer:** [Source answer](https://github.com/prisma/prisma/discussions/15898#discussioncomment-4024086)

**Reviewer:** __________  **Date:** __________

### Question

```text
Is there a difference between create and createMany when used in nested writes?

When using nested write to create multiple nested entities, it seems I can use both create and createMany to achieve the same goal. Is there any difference between them?
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

```text
In Prisma, `create` and `createMany` can both create multiple related records in a nested one-to-many relation, so they can be interchangeable for the narrow goal of creating several direct child records.

They are not equivalent in capability:

- **Nested `create`** supports further nested relations. For example, one query can create a user, multiple posts, and categories or comments related to those posts. It also supports many-to-many relations.
- **Nested `createMany`** is for creating multiple records at that relation level. It cannot contain another nested `create` or `createMany`, and it does not support nested many-to-many writes.
- **`createMany`** supports `skipDuplicates`; nested `create` does not.

Therefore, use nested `create` by default when you need additional relation nesting. Use nested `createMany` when you only need to insert multiple direct children and need duplicate skipping. For the simple case of creating multiple one-to-many children, either option can achieve the same result.
```

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Relations and joins](../documents/D048-97243d4508f1.md)  
   Document ID: `prisma::/docs/orm/fundamentals/relations-and-joins`

2. [Relation queries](../documents/D059-ee0f569f320d.md)  
   Document ID: `prisma::/docs/orm/v7/prisma-client/queries/relation-queries`
   Recorded heading(s): Create a single record and multiple related records

### Two-item review

Choose **Yes / Partly / No / Cannot judge** for each item. Blank means unanswered.

| Item | Human label | Missing or incorrect content / evidence |
|---|---|---|
| 1. Does the reference answer correctly and completely resolve the question? | __________ | __________ |
| 2. Do the provided documents, taken together, contain enough information to answer all essential parts of the question? | __________ | __________ |

For **Partly** or **No**, briefly name the missing requirement, error, or condition and identify a relevant document/heading if available. For **Cannot judge**, state what information or expertise is missing.

Judge answer completeness from what the answer actually explains; do not fill its omissions with text found only in the documents. Judge document sufficiency independently: the reference answer or community acceptance alone is not documentation evidence. Include necessary steps, conditions and version restrictions; do not require unrelated background or an identical implementation.

<details>
<summary>Original accepted answer — provenance only</summary>

```text
Thank you, guys. I just noticed Prisma has nice documentation explaining the differences, and I missed it before raising this discussion:
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-07-prisma-prisma-5982.md) | [Next case](case-09-github-docs-25309.md)
