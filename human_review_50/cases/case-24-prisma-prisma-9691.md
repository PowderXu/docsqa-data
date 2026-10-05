<a id="case-24"></a>

# Case 24

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-23-tailwind-css-tailwind-16506.md) | [Next case](case-25-github-docs-166151.md)

**Dataset:** Prisma  
**Question ID:** `prisma::prisma-9691`  
**Distinct linked documents:** 1  
**Original discussion:** [Source](https://github.com/prisma/prisma/discussions/9691)  
**Accepted answer:** [Source answer](https://github.com/prisma/prisma/discussions/9691#discussioncomment-1458381)

**Reviewer:** __________  **Date:** __________

### Question

```text
Create migration file without applying it

Not sure If I'm missing something from the documentation but is there no way of generating a migration file using a command like prisma migrate dev except not applying it to the database? Feels weird that it's applied generated and applied instantly without the chance of reviewing the generated migration file.
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

````text
Yes. Use the `--create-only` option:

```bash
npx prisma migrate dev --create-only
```

This generates the migration without applying it to the development database, so you can review the generated migration file first. Run `prisma migrate dev` afterward to apply it.
````

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Prisma CLI reference](../documents/D066-5fa0571d11d8.md)  
   Document ID: `prisma::/docs/orm/v7/reference/prisma-cli-reference`
   Recorded heading(s): `migrate dev`

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
You can use the --create-only option to generate the migration file without applying it to the database. So the command will look like this:
npx prisma migrate dev --create-only
You can find more details in the reference for Prisma Migrate in the docs.
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-23-tailwind-css-tailwind-16506.md) | [Next case](case-25-github-docs-166151.md)
