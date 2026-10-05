<a id="case-05"></a>

# Case 05

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-04-prisma-prisma-13540.md) | [Next case](case-06-github-docs-23381.md)

**Dataset:** Prisma  
**Question ID:** `prisma::prisma-28901`  
**Distinct linked documents:** 2  
**Original discussion:** [Source](https://github.com/prisma/prisma/discussions/28901)  
**Accepted answer:** [Source answer](https://github.com/prisma/prisma/discussions/28901#discussioncomment-15233234)

**Reviewer:** __________  **Date:** __________

### Question

```text
No database tables found. Connect to a database to see your schema. (bunx prisma studio)

Question
Prisma 7.1v
prisma/schema.prisma
generator client {
 provider = "prisma-client"
 output = "../generated/prisma"
 runtime = "bun"
}
datasource db {
 provider = "postgresql"
}
model User {
 id Int @id @default(autoincrement())
 email String @unique
 name String?
 role Role @default(USER)
 posts Post[]
 createAt DateTime @default(now())
}
model Post {
 id Int @id @default(autoincrement())
 createAt DateTime @default(now())
 updateAt DateTime @updatedAt
 published Boolean @default(false)
 title String @db.VarChar(255)
 author User @relation(fields: [authorId], references: [id])
 authorId Int
}
enum Role {
 USER
 ADMIN
}
prisma.config.ts
import "dotenv/config";
import { defineConfig, env } from "prisma/config";
export default defineConfig({
 schema: "./src/prisma/schema.prisma",
 migrations: {
 path: "./src/prisma/migrations",
 seed: "tsx ./src/prisma/seed.ts",
 },
 datasource: {
 url: env("DATABASE_URL"),
 },
});
.env
DATABASE_URL="postgres://postgres:postgres@localhost:51214/template1?sslmode=disable&connection_limit=1&connect_timeout=0&max_idle_connection_lifetime=0&pool_timeout=0&single_use_connections=true&socket_timeout=0"
commands :
bunx prisma migrate dev --name init
bunx prisma generate
bunx prisma db push
bunx prisma studio
How to reproduce (optional)
Expected behavior (optional)
No response
Information about Prisma Schema, Client Queries and Environment (optional)
// Add your schema.prisma
// Add any relevant Prisma Client queries here
OS: Arch linux
Database: PostgreSQL
Node.js version: v24.11.1
Prisma schema loaded from src/prisma/schema.prisma
prisma : 7.1.0
@prisma/client : 7.1.0
Operating System : linux
Architecture : x64
Node.js : v24.11.1
TypeScript : 5.9.3
Query Compiler : enabled
PSL : @prisma/prisma-schema-wasm 7.1.0-6.ab635e6b9d6
06fa5c8fb8b1a7f909c3c3c1c98ba
Schema Engine : schema-engine-cli ab635e6b9d606fa5c8fb8b1a7f90
9c3c3c1c98ba (at node_modules/@prisma/engines/schema-engine-debian-op
enssl-3.0.x)
Default Engines Hash : ab635e6b9d606fa5c8fb8b1a7f909c3c3c1c98ba
Studio : 0.8.2
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

````text
Remove the `max_idle_connection_lifetime` and `single_use_connections` parameters from `DATABASE_URL`. Prisma Studio does not recognize those parameters in the connection URL.

Use, for example:

```env
DATABASE_URL="postgres://postgres:postgres@localhost:51214/template1?sslmode=disable&connection_limit=1&connect_timeout=0&pool_timeout=0&socket_timeout=0"
```

Then run:

```bash
bunx prisma studio
```

After removing those two parameters, Prisma Studio can connect and display the database tables.
````

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [PostgreSQL](../documents/D054-78f918540d86.md)  
   Document ID: `prisma::/docs/orm/v7/core-concepts/supported-databases/postgresql`
   Recorded heading(s): Self-hosted PostgreSQL

2. [Schema API](../documents/D068-e9da09094fef.md)  
   Document ID: `prisma::/docs/orm/v7/reference/prisma-schema-reference`
   Recorded heading(s): Arguments

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
max_idle_connection_lifetime and single_use_connections are configuration parameters that are not recognized in the Prisma Studio console for your DATABASE_URL. After removing them, it works.
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-04-prisma-prisma-13540.md) | [Next case](case-06-github-docs-23381.md)
