<a id="case-20"></a>

# Case 20

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-19-supabase-supabase-27860.md) | [Next case](case-21-github-docs-166561.md)

**Dataset:** Prisma  
**Question ID:** `prisma::prisma-11775`  
**Distinct linked documents:** 2  
**Original discussion:** [Source](https://github.com/prisma/prisma/discussions/11775)  
**Accepted answer:** [Source answer](https://github.com/prisma/prisma/discussions/11775#discussioncomment-2178559)

**Reviewer:** __________  **Date:** __________

### Question

```text
Unable to filter an array inside of a related model.

I'm trying to check if the provided value exists inside of an array. I've been trying to figure this one out and from what I gathered, I have to use has. The array I'm trying to filter is inside of a related model. I tried looking for a solution, but couldn't find much on this subject. Am I doing something wrong? Is it at all possible to filter an array inside of a related model?
Here's my schema. Job and Company models are related, and inside Company we have a parking array.
model Company {
 id Int @id @default(autoincrement())
 name String @db.VarChar(200)
 state String @db.VarChar(30)
 parking String[]
 ...
 createdAt DateTime @default(now())
 updated_at DateTime @updatedAt
 @@map(name: "company")
}
model Job {
 id Int @id @default(autoincrement())
 type String
 company Company @relation(fields: [company_id], references: [id])
 company_id Int
 createdAt DateTime @default(now())
 updated_at DateTime @updatedAt
 UserJobs UserJobs[]
 @@map(name: "job")
}
Below, I'm trying to find many jobs which match various values. One of the values I'm trying to match is inside of an array in the related Company model. Here's what I tried:
 const jobs = await prisma.job.findMany({
 where: {
 AND: [
 {
 type: {
 contains: req.body.type,
 }
 },
 {
 company: {
 state: {
 contains: req.body.state
 }
 }
 },
 ...
 {
 company: {
 parking: {
 has: req.body.parkingState
 }
 }
 }
 ]
 },
 include: {
 company: true,
 }
 })
Edit: removed most of the unrelated code, marked with ...
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

````text
Yes. Filter the related `Company` through a relation filter, then apply the scalar-list filter to `parking`. Because `Job.company` is a to-one relation, use `is`:

```ts
const jobs = await prisma.job.findMany({
  where: {
    type: {
      contains: req.body.type,
    },
    company: {
      is: {
        state: {
          contains: req.body.state,
        },
        parking: {
          has: req.body.parkingState,
        },
      },
    },
  },
  include: {
    company: true,
  },
});
```

`has` checks whether the supplied value exists in the `parking` scalar list. `is` applies the nested conditions to the related `Company` record. Thus, the relevant correction to the shown query is to put the `state` and `parking` conditions inside `company.is`. `include` only controls which related data is returned; it does not perform the filtering.
````

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Relations and joins](../documents/D048-97243d4508f1.md)  
   Document ID: `prisma::/docs/orm/fundamentals/relations-and-joins`

2. [Prisma Client API](../documents/D067-6305cf51c088.md)  
   Document ID: `prisma::/docs/orm/v7/reference/prisma-client-reference`
   Recorded heading(s): Relation filters; `include`; `has`

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
You would need to use relation filters. Have you tried using them?
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-19-supabase-supabase-27860.md) | [Next case](case-21-github-docs-166561.md)
