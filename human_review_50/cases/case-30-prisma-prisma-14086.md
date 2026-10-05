<a id="case-30"></a>

# Case 30

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-29-tailwind-css-tailwind-13967.md) | [Next case](case-31-prisma-prisma-27294.md)

**Dataset:** Prisma  
**Question ID:** `prisma::prisma-14086`  
**Distinct linked documents:** 2  
**Original discussion:** [Source](https://github.com/prisma/prisma/discussions/14086)  
**Accepted answer:** [Source answer](https://github.com/prisma/prisma/discussions/14086#discussioncomment-3061282)

**Reviewer:** __________  **Date:** __________

### Question

```text
The expected type comes from property 'data' which is declared here on type

Hi, i'm new to Prisma and am getting an error in my seed file:
The expected type comes from property 'data' which is declared here on type '{ select?: TemplateSelect; include?: TemplateInclude; data: (Without<TemplateCreateInput, TemplateUncheckedCreateInput> & TemplateUncheckedCreateInput) | (Without<...> & TemplateCreateInput); }'
await prisma.template.create({
 data: templates,
 });
schema:
// This is your Prisma schema file,
// learn more about it in the docs: 
generator client {
 provider = "prisma-client-js"
 previewFeatures = ["referentialIntegrity"]
}
datasource db {
 provider = "mysql"
 url = env("DATABASE_URL")
 referentialIntegrity = "prisma"
}
model User {
 id Int @id @default(autoincrement())
 email String @unique
 name String?
 role Role @default(USER)
 templates Template[]
 profile Profile?
}
model Component {
 id String @id @default(uuid())
 name String
 description String @default("")
 prettyName String
 type String
 settings Json
 templates Template[] @relation(references: [id])
}
model Template {
 id String @id @default(uuid())
 name String
 description String?
 components Component[]
 author User @relation(fields: [authorId], references: [id])
 authorId Int
}
model Profile {
 id Int @id @default(autoincrement())
 bio String
 user User @relation(fields: [userId], references: [id])
 userId Int
 image String?
}
model Inquiry {
 id Int @default(autoincrement()) @id
 name String
 email String
 subject String?
 message String
}
enum Role {
 USER
 ADMIN
}
full seed.ts
import { components } from "../data/components";
import { templates } from "../data/templates";
import prisma from "../lib/prisma";
const load = async () => {
 try {
 await prisma.component.deleteMany();
 console.log("Deleted records in component table");
 await prisma.template.deleteMany();
 console.log("Deleted records in template table");
 await prisma.$queryRaw`ALTER TABLE Template AUTO_INCREMENT = 1`;
 console.log("reset template auto increment to 1");
 await prisma.$queryRaw`ALTER TABLE Component AUTO_INCREMENT = 1`;
 console.log("reset component auto increment to 1");
 await prisma.component.createMany({
 data: components,
 });
 console.log("Added category data");
 await prisma.template.create({
 data: templates,
 });
 console.log("Added product data");
 } catch (e) {
 console.error(e);
 process.exit(1);
 } finally {
 await prisma.$disconnect();
 }
};
load();
tempates.js
mport { v4 as uuidv4 } from "uuid";
export const templates = [
 {
 id: uuidv4(),
 name: "Some Template Name",
 description: "Some Template Description",
 components: [
 {
 id: "1234-456676-5665544",
 name: "previewCopy",
 description:
 "Preview copy is the first piece of text that displays right after the subject line in ESP preview pane. It is not visible in the body of the email.",
 settings: {
 copy: "This is the preview copy",
 },
 },
 {
 id: "1234-456676-123456",
 name: "header",
 description:
 "The email header is the first visual element your customer will see. This is typically where your company logo will be.",
 settings: {
 backgroundColor: "#fff",
 },
 },
 ],
 authorId: "1234-456676-123456",
 author: "John Doe",
 },
];
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

````text
`prisma.template.create()` creates **one** `Template`, but `templates` is an array. In addition, the relation fields in each object do not have the shape expected by Prisma.

Your schema requires:

- `Template.authorId` to be an `Int`, but the data contains a string.
- `author` to be a relation object, not the string `"John Doe"`.
- `components` to use nested relation syntax such as `connect` or `create`.
- Each component to contain the required `prettyName`, `type`, and `settings` fields.

Since your seed already inserts components with `createMany`, connect those existing components when creating each template. Also create the templates one at a time:

```ts
for (const template of templates) {
  await prisma.template.create({
    data: {
      id: template.id,
      name: template.name,
      description: template.description,

      author: {
        connect: {
          id: EXISTING_USER_ID, // a numeric User.id
        },
      },

      components: {
        connect: template.components.map((component) => ({
          id: component.id,
        })),
      },
    },
  });
}
```

Replace `EXISTING_USER_ID` with the numeric ID of a user that already exists. Do not pass `author: "John Doe"`; if you want to create a user as part of the same operation, use a nested `create`, otherwise use `author.connect`.

Therefore, replace:

```ts
await prisma.template.create({
  data: templates,
});
```

with the loop above, and make sure the component records inserted by `createMany` include the required `prettyName` and `type` fields. If the components are not inserted separately, use `components: { create: [...] }` instead of `components: { connect: [...] }`.

Prisma nested writes use `create` for related records that should be created and `connect` for records that already exist. They must be placed inside the relation field, such as `components` or `author`.
````

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Relations and joins](../documents/D048-97243d4508f1.md)  
   Document ID: `prisma::/docs/orm/fundamentals/relations-and-joins`

2. [Relation queries](../documents/D059-ee0f569f320d.md)  
   Document ID: `prisma::/docs/orm/v7/prisma-client/queries/relation-queries`
   Recorded heading(s): Nested writes

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
Hi @akarpov91 👋
There are a few things wrong with your approach. Firstly two suggestions for your schema:
model User {
 id Int @id @default(autoincrement())
 email String @unique
 name String?
 role Role @default(USER)
 templates Template[]
 profile Profile?
}
model Component {
 id String @id @default(uuid())
 name String
 description String @default("")
 prettyName String
 type String
 settings Json
 templates Template[] // @relation attribute with references is not necessary for implicit many-to-many
}
model Template {
 id String @id @default(uuid())
 name String
 description String?
 components Component[]
 author User @relation(fields: [authorId], references: [id])
 authorId Int
}
model Profile {
 id Int @id @default(autoincrement())
 bio String
 user User @relation(fields: [userId], references: [id])
 userId Int @unique // this need to be unique to ensure that each `Profile` is related to a single `User` 
 image String?
}
model Inquiry {
 id Int @id @default(autoincrement())
 name String
 email String
 subject String?
 message String
}
enum Role {
 USER
 ADMIN
}
Now there are a few things wrong with your template.create() call:
You're trying to pass in an array of template objects where template.create expects a single template instance, whereas you're passing an array.
The way you are trying to do relation queries (create or connect to relations like components and Author is wrong).
If you want to connect to an existing relation, you have to use the relationName.connect keyword.
If you want to create new records in a relation, you have to use the relationName.create keyword.
Here's a modification of your existing template.create call that demonstrates all this:
export const template = // templates has been renamed to template and is a single object instead of an array of objects
{
 name: "Some Template Name",
 description: "Some Template Description",
 components: [
 {
 id: "1234-456676-5665544",
 name: "previewCopy",
 description:
 "Preview copy is the first piece of text that displays right after the subject line in ESP preview pane. It is not visible in the body of the email.",
 settings: {
 copy: "This is the preview copy",
 },
 type: "foo", // type is a mandatory field according to your schema. 
 prettyName: "bar", // prettyName is a mandatory field according to your schema. 
 },
 {
 id: "1234-456676-123456",
 name: "header",
 description:
 "The email header is the first visual element your customer will see. This is typically where your company logo will be.",
 settings: {
 backgroundColor: "#fff",
 },
 type: "foo",
 prettyName: "bar",
 },
 ],
 authorId: 4 // authorId should be a number, not a string based on your schema
};
async function example() {
 const { name, description, components } = template;
 await prisma.template.create({
 data: {
 name,
 description,
 components: { // creating new component records and then connecting it to this template record. 
 create: components.map((component) => { return { ...component } })
 },
 author: { // connecting to an existing user record 
 connect: {
 id: 6,
 }
 }
 },
 });
}
Note that I'm assuming you're trying to create new records in the components relation. If you're simply trying to connect to existing component records, use the connect syntax similar to what is shown for author.
There's more info about handling nested relations in writes in the nested writes section in the Prisma docs.
Let me know if you need further clarification on anything.
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-29-tailwind-css-tailwind-13967.md) | [Next case](case-31-prisma-prisma-27294.md)
