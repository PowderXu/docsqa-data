<a id="case-02"></a>

# Case 02

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-01-prisma-prisma-24697.md) | [Next case](case-03-tailwind-css-tailwind-15809.md)

**Dataset:** Prisma
**Question ID:** `prisma::prisma-12782`
**Distinct linked documents:** 2
**Original discussion:** [Source](https://github.com/prisma/prisma/discussions/12782)
**Accepted answer:** [Source answer](https://github.com/prisma/prisma/discussions/12782#discussioncomment-2555670)

**Reviewer:** __________  **Date:** __________

### Question

```text
Can I create my own data type?

I want to store TIME WITH TIMEZONE in PostgreSQL, there are a way to implement it?
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

````text
Yes. If you are using Prisma with PostgreSQL, use Prisma’s native type mapping rather than defining a new user-defined type:

```prisma
sometime DateTime @db.Timetz()
```

`@db.Timetz()` is the relevant native mapping for storing the requested PostgreSQL time-with-time-zone value. Prisma’s default mapping for `DateTime` is `timestamp(3)`, so apply the native type attribute when you specifically need this PostgreSQL type.
````

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [PostgreSQL](../documents/D054-78f918540d86.md)  
   Document ID: `prisma::/docs/orm/v7/core-concepts/supported-databases/postgresql`
   Recorded heading(s): Type mappings
2. [How to use Prisma ORM&#39;s type system](../documents/D062-9993b852920a.md)
   Document ID: `prisma::/docs/orm/v7/prisma-client/type-safety/prisma-type-system`
   Recorded heading(s): Native type mappings

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
Hey @Sasha-hk 👋,
You can use a native Postgres type mapping for this, specifically @db.Timetz().
sometime DateTime @db.Timetz()
Let me know if that works!
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-01-prisma-prisma-24697.md) | [Next case](case-03-tailwind-css-tailwind-15809.md)
