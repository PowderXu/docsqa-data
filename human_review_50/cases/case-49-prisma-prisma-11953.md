<a id="case-49"></a>

# Case 49

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-48-github-docs-167845.md) | [Next case](case-50-github-docs-188227.md)

**Dataset:** Prisma  
**Question ID:** `prisma::prisma-11953`  
**Distinct linked documents:** 1  
**Original discussion:** [Source](https://github.com/prisma/prisma/discussions/11953)  
**Accepted answer:** [Source answer](https://github.com/prisma/prisma/discussions/11953#discussioncomment-2222057)

**Reviewer:** __________  **Date:** __________

### Question

```text
Is there a way to put an object in a model?

Im new at prisma, but i was thinking if it possible to get data like this
{
 id: 1.
 name: 'Vyrek',
 adress: {
 country: 'Mexico',
 ...
 }
}
without making a relation, i dont want another collection just for the same topic as the main model, like this
model User {
 id String @id @map("_id")
 name String
 adress {
 country String
 }
}
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

````text
No—not as an inline nested object in the `User` model. To return an object-shaped `address`, define `Address` separately and relate it to `User`; this stores the address in a separate collection. You can then load it with `include`:

```ts
await prisma.user.findUnique({
  where: { id: id },
  include: { address: true },
});
```

`include` eagerly loads relations, so the returned user can have a nested `address` property.
````

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Prisma Client API](../documents/D067-6305cf51c088.md)  
   Document ID: `prisma::/docs/orm/v7/reference/prisma-client-reference`
   Recorded heading(s): `include`

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
Hey @VyrekXD 👋🏻 ,
Unfortunately that is not possible, to have data in a nested format you would need to have a different collection.
In your case it would be address collection and while fetching data you can fetch address while querying users.
Your query could look like
await prisma.user.findUnique({
 where: {
 id: id,
 },
 include: {
 address: true,
 },
});
Here is a link to include reference
Please let me know if you face any other issues.
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-48-github-docs-167845.md) | [Next case](case-50-github-docs-188227.md)
