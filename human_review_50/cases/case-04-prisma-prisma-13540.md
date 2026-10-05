<a id="case-04"></a>

# Case 04

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-03-tailwind-css-tailwind-15809.md) | [Next case](case-05-prisma-prisma-28901.md)

**Dataset:** Prisma  
**Question ID:** `prisma::prisma-13540`  
**Distinct linked documents:** 1  
**Original discussion:** [Source](https://github.com/prisma/prisma/discussions/13540)  
**Accepted answer:** [Source answer](https://github.com/prisma/prisma/discussions/13540#discussioncomment-3054827)

**Reviewer:** __________  **Date:** __________

### Question

```text
why doesn't _count show in some include fields.

Prisma Schema
model Author {
 id String @id @default(uuid())
 display_name String @unique
 web_url String?
 details String? @db.Text
 logo String?
 status author_status
 exclusive Boolean
 type author_type
 message String? @db.Text
 work_type author_work_type
 accepted_terms author_accepted_terms
 fee_id Int
 fee Author_Fee? @relation(fields: [fee_id], references: [id], onDelete: Cascade, onUpdate: Cascade)
 support_type author_support_type @default(none)
 external_url String? @db.Text
 response_time author_response_time @default(not_specified)
 createdAt DateTime @default(now())
 user User[]
 product Products[]
 followers Author_Followers[]
 sales Sales[]
 payouts payout_accounts?
}
model Author_Followers {
 id Int @id @default(autoincrement())
 nsid String
 user User @relation(fields: [nsid], references: [nsid], onDelete: Cascade, onUpdate: Cascade)
 authorId String
 author Author @relation(fields: [authorId], references: [id], onDelete: Cascade, onUpdate: Cascade)
 createdAt DateTime @default(now())
 @@unique([authorId, nsid])
}
model Sales {
 id String @id
 nsid String
 user User @relation(fields: [nsid], references: [nsid], onDelete: Cascade, onUpdate: Cascade)
 product_id String
 product Products @relation(fields: [product_id], references: [id], onDelete: Cascade, onUpdate: Cascade)
 creation_time DateTime @default(now())
 purchase_type purchase_type
 support_type support_type
 valid_until DateTime
 purchase_code String
 author_id String
 author Author @relation(fields: [author_id], references: [id], onDelete: Cascade, onUpdate: Cascade)
 url String @db.Text
 notify_email Int @default(1)
 currency_id Int @default(1)
 author_fee_id Int
 discount String
 receipt_id String
 transaction Transactions @relation(fields: [receipt_id], references: [receipt_id], onDelete: Cascade, onUpdate: Cascade)
 ratings Ratings[]
}
When i try the following"
 const author = await prisma.author!.findUnique({
 where: {
 id: req.query.userId as string,
 },
 include: {
 user: true,
 product: true,
 sales: {
 select: {
 _count: true,
 },
 },
 followers: {
 select: {
 //Error is on the next line: 
 // Type '{ _count: true; }' is not assignable to type 'Author_FollowersSelect'. 
 //Object literal may only specify known properties, and '_count' does not exist in type 'Author_FollowersSelect'
 _count: true,
 },
 },
 },
 })
Why does the _count in followers error whereas in sales it doesnt?
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

````text
`_count` is relative to the model level where it appears.

In your nested `sales.select`, `_count` refers to relations of `Sales` records. Since `Sales` has the list relation `ratings`, Prisma can generate an `_count` field for `SalesSelect`.

`Author_Followers` has no list-valued relation of its own—`user` and `author` are singular relations—so its generated `Author_FollowersSelect` does not expose `_count`. It therefore rejects `_count: true` there.

If you want the number of `sales` and `followers` belonging to the `Author`, put `_count` in the parent `include`, alongside those relations:

```ts
const author = await prisma.author.findUnique({
  where: {
    id: req.query.userId as string,
  },
  include: {
    user: true,
    product: true,
    _count: {
      select: {
        sales: true,
        followers: true,
      },
    },
  },
});
```

The result contains counts at the author level, such as `author._count.sales` and `author._count.followers`. Prisma documents `_count` as a selectable relation count and shows it under the parent record's `select` or `include`, rather than as a field used to count the parent relation from inside each related record.
````

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Prisma Client API](../documents/D067-6305cf51c088.md)  
   Document ID: `prisma::/docs/orm/v7/reference/prisma-client-reference`
   Recorded heading(s): `select`; `include`

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
Hey 👋🏽
To select a _count on relations, move the _count property to the include property. Here's an example of what the query would look like:
const author = await prisma.author.findUnique({
 where: {
 id: '',
 },
 include: {
 user: true,
 product: true,
 _count: {
 select: {
 sales: true,
 followers: true,
 }
 },
 },
})
We have docs on selecting a _count on relations, which should help. Don't hesitate to reach out in case you get stumped. 🙂
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-03-tailwind-css-tailwind-15809.md) | [Next case](case-05-prisma-prisma-28901.md)
