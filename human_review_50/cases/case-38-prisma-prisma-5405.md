<a id="case-38"></a>

# Case 38

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-37-github-docs-22539.md) | [Next case](case-39-github-docs-132566.md)

**Dataset:** Prisma  
**Question ID:** `prisma::prisma-5405`  
**Distinct linked documents:** 2  
**Original discussion:** [Source](https://github.com/prisma/prisma/discussions/5405)  
**Accepted answer:** [Source answer](https://github.com/prisma/prisma/discussions/5405#discussioncomment-329792)

**Reviewer:** __________  **Date:** __________

### Question

```text
findUnique with more than one arg

Hello Prisma, I ran into an issue where I need to check if a user exists by his username and email since both are unique fields in the database, but I got an error.
Argument where of type UserWhereUniqueInput needs exactly one argument, but you provided username and email. Please choose one.
so, is there a way to execute this query just once?. instead of running one for each like the following
const user = await prisma.user.findUnique({
 where: {
 username,
 email,
 },
 });
and not like this
const user = await prisma.user.findUnique({
 where: {
 username,
 },
 });
const user = await prisma.user.findUnique({
 where: {
 email,
 },
 });
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

````text
Yes. Use `findFirst()` with both fields in the `where` clause. This executes one query and returns the matching user, or `null` if no record matches both values:

```ts
const user = await prisma.user.findFirst({
  where: {
    username,
    email,
  },
});
```

`findUnique()` is intended for a unique lookup, whereas `findFirst()` accepts general filter criteria such as multiple fields.
````

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Reading data](../documents/D047-c7a4e0f85472.md)  
   Document ID: `prisma::/docs/orm/fundamentals/reading-data`

2. [Prisma Client API](../documents/D067-6305cf51c088.md)  
   Document ID: `prisma::/docs/orm/v7/reference/prisma-client-reference`
   Recorded heading(s): `findFirst()`

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
@ahmdtalat 👋
In this case, you need to use findFirst. So your query would be:
const user = await prisma.user.findFirst({
 where: {
 username,
 email,
 },
});
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-37-github-docs-22539.md) | [Next case](case-39-github-docs-132566.md)
