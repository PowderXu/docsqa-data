<a id="case-12"></a>

# Case 12

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-11-github-docs-120943.md) | [Next case](case-13-github-docs-24939.md)

**Dataset:** Prisma  
**Question ID:** `prisma::prisma-20554`  
**Distinct linked documents:** 3  
**Original discussion:** [Source](https://github.com/prisma/prisma/discussions/20554)  
**Accepted answer:** [Source answer](https://github.com/prisma/prisma/discussions/20554#discussioncomment-6638190)

**Reviewer:** __________  **Date:** __________

### Question

```text
Prisma Client Extension not called for nested creates?

Question
I'm currently building a chat-app, which features conversations and conversationParts (i.e. messages etc.).
My goal is to create a property lastConvoPartSentAtMillis on a conversation (it should be an actualy property, for performance reasons), which is updated to the millis, when the last message was sent automatically, I intend to use client extensions for that.
My initial idea was, to add queries to create and createMany, for the conversationPart object, and then update the conversation, i.e.:
async create({ model, operation, args, query }) {
 const result = await query(args);
 // am I allowed to do this?
 await prisma.conversation.update({
 where: {
 id: result.conversationId,
 },
 data: {
 lastConvoPartSentAtMillis: result.createdAt
 ? result.createdAt
 : new Date(),
 },
 });
 return result;
},
async createMany({ model, operation, args, query }) {
// omitted for brevity, but does the same thing as create, but for 'createMany'
The problem is, when creating a conversation, with nested ConversationPart creates, those methods are not called at all.
const createdConversation = await prisma.conversation.create({
 data: {
 Team: {
 connect: { id: team.id },
 },
 ConversationPart: {
 createMany: {
 data: createdMessages.map((message) => {
 return {
 type: ConversationPartType.MESSAGE,
 conversationPartMessageId: message.id,
 createdAt: message.date,
 };
 }),
 },
 },
 },
});
Is this a bug, or does it work as intended? Also, what would be the ideal approach to achieve, what I'm trying?
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

````text
This is expected behavior, not a bug. Prisma Client query extensions run for the top-level query, but they do not currently run for nested operations. Therefore, a `conversation.create()` containing a nested `ConversationPart.createMany()` does not invoke the `ConversationPart` `create` or `createMany` extension.

The practical approach is to update the parent explicitly after the conversation and its parts have been created:

```ts
const createdConversation = await prisma.conversation.create({
  data: {
    Team: {
      connect: { id: team.id },
    },
    ConversationPart: {
      createMany: {
        data: createdMessages.map((message) => ({
          type: ConversationPartType.MESSAGE,
          conversationPartMessageId: message.id,
          createdAt: message.date,
        })),
      },
    },
  },
});

const lastMessageDate = createdMessages[createdMessages.length - 1].date;

await prisma.conversation.update({
  where: { id: createdConversation.id },
  data: {
    lastConvoPartSentAtMillis: lastMessageDate,
  },
});
```

If both writes must succeed or fail together, put them in an interactive transaction and use the transaction client for both operations:

```ts
await prisma.$transaction(async (tx) => {
  const conversation = await tx.conversation.create({
    data: {
      Team: { connect: { id: team.id } },
      ConversationPart: {
        createMany: {
          data: createdMessages.map((message) => ({
            type: ConversationPartType.MESSAGE,
            conversationPartMessageId: message.id,
            createdAt: message.date,
          })),
        },
      },
    },
  });

  await tx.conversation.update({
    where: { id: conversation.id },
    data: {
      lastConvoPartSentAtMillis:
        createdMessages[createdMessages.length - 1].date,
    },
  });
});
```

For a batch containing messages with different dates, select the timestamp according to your definition of “last” (for example, the greatest `createdAt`), rather than assuming the input array is ordered.
````

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Custom validation](../documents/D051-19c1f9045abc.md)  
   Document ID: `prisma::/docs/orm/v6/prisma-client/queries/custom-validation`
   Recorded heading(s): Input validation with Prisma Client extensions

2. [Transactions](../documents/D049-477b0bd6a9a7.md)  
   Document ID: `prisma::/docs/orm/fundamentals/transactions`

3. [Transactions and batch queries](../documents/D060-4c1a7523a475.md)  
   Document ID: `prisma::/docs/orm/v7/prisma-client/queries/transactions`
   Recorded heading(s): Interactive transactions; Transactions and batch queries

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
Hello @Tobjoern 👋
Based on this reference, this behaviour is expected.
As a workaround, after creating the conversation and its conversationPart, you can immediately update the lastConvoPartSentAtMillis property of the conversation model.
It could look something like this:
const createdConversation = await prisma.conversation.create({
 data: {
 Team: {
 connect: { id: team.id },
 },
 ConversationPart: {
 createMany: {
 data: createdMessages.map((message) => {
 return {
 type: ConversationPartType.MESSAGE,
 conversationPartMessageId: message.id,
 createdAt: message.date,
 };
 }),
 },
 },
 },
});
// After creating the conversation and its parts, update the conversation
const lastMessageDate = createdMessages[createdMessages.length - 1].date;
await prisma.conversation.update({
 where: {
 id: createdConversation.id,
 },
 data: {
 lastConvoPartSentAtMillis: lastMessageDate,
 },
});
You can also wrap this logic in interactive transactions to ensure that conversation model gets correctly updated.
```

#### Existing image-derived text attached to the accepted answer

Evidence ID: `img-6ee7a92b86fb4d3a`

```text
Query extensions do not currently work for nested operations. In this example,
validations are only run on the top level data object passed to methods such as
prisma.product.create(). Validations implemented this way do not automatically
run for nested writes.
A white rectangular screenshot contains a vertical rounded yellow bar on the left and a four-line paragraph in large gray-blue text. The code-like text "prisma.product.create()" appears in a light gray rounded rectangle. The words "nested writes" are blue and underlined, indicating a link.
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-11-github-docs-120943.md) | [Next case](case-13-github-docs-24939.md)
