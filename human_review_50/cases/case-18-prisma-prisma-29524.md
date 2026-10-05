<a id="case-18"></a>

# Case 18

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-17-tailwind-css-tailwind-20353.md) | [Next case](case-19-supabase-supabase-27860.md)

**Dataset:** Prisma  
**Question ID:** `prisma::prisma-29524`  
**Distinct linked documents:** 2  
**Original discussion:** [Source](https://github.com/prisma/prisma/discussions/29524)  
**Accepted answer:** [Source answer](https://github.com/prisma/prisma/discussions/29524#discussioncomment-16771216)

**Reviewer:** __________  **Date:** __________

### Question

```text
What's the best practice for deploying migrations to an existing database without syncing schema to prisma?

Question
Background
My team is working on a new backend application for our multi-tenant platform. We have existing DBs (one per tenant) in mysql and we'd like our new application (which uses prisma) to reuse these DBs. There are tradeoffs for this approach which we are willing to accept because we'd like to isolate our customers' data to a single DB and take advantage of our existing infrastructure around that. The new application will only talk to the tables it knowns about and will never query the already existing tables, and vice versa.
We were hoping to only define the new tables in the prisma schema and for the shared DBs to be an implementation detail that the app doesn't need to know too much about. The problem with this is when we run prisma migrate deploy for one of our tenants we get an error Error: P3005: The database schema is not empty. Prisma assumes that the DB will be empty before deploying migrations for the first time.
We don't want to pull down the schema because we don't want this new application to know anything about it and introduce the risk of someone querying tables from the old application. Also, we don't want to maintain the schema in two different places.
Question
We realized one workaround is to create the _prisma_migrations table ahead of time before running prisma migrate deploy. If that table exists, then the error is not thrown and the migrations deploy just fine. But this feels really fragile. Does anyone know of a better way to handle this? Is our setup just fundamentally against prisma's use case? Would the prisma team be open to us contributing a PR to add a flag to prisma migrate deploy that ignores a non-empty DB when deploying migrations for the first time?
How to reproduce (optional)
Create a DB and add a table
Setup a simple prisma schema with a different table
Configure prisma to use the existing DB
Run prisma migrate deploy
Expected behavior (optional)
No response
Information about Prisma Schema, Client Queries and Environment (optional)
Database: MySQL
Node.js version: 24.13.0
Prisma version: 7.3.0
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

````text
Use Prisma Migrate baselining rather than manually creating `_prisma_migrations`.

For the existing tenant databases:

1. Add a committed, no-op baseline migration as the first migration, for example `prisma/migrations/0_existing_database_baseline/migration.sql`. Because the legacy tables are intentionally outside Prisma's ownership, this migration can contain only a comment explaining that it represents the pre-existing database.
2. For each tenant database, mark that baseline as already applied:

```bash
npx prisma migrate resolve --applied 0_existing_database_baseline
```

3. Run the normal deployment:

```bash
npx prisma migrate deploy
```

`migrate resolve --applied` records the baseline in `_prisma_migrations`; do not insert that row manually. `migrate deploy` then skips the applied baseline and applies only later migrations, such as migrations for the new tables defined in your Prisma schema.

This lets the application keep the legacy tables out of `schema.prisma`, so you do not need to introspect or maintain their schema in Prisma. Keep the baseline migration committed and use the same migration history for all environments, and run the resolve step once for every existing tenant database before its first deployment.

Therefore, this arrangement is supported through baselining; the P3005 error means Prisma sees a non-empty database with no Prisma migration history yet. The supplied documentation supports `migrate resolve` for baselining, but does not establish whether the Prisma team would accept a contribution adding a separate “ignore non-empty database” flag. Such a flag is unnecessary for this workflow.
````

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Baselining a database](../documents/D063-6e0dadd10390.md)  
   Document ID: `prisma::/docs/orm/v7/prisma-migrate/workflows/baselining`
   Recorded heading(s): Baselining a database

2. [resolve](../documents/D045-3df8e36e28da.md)  
   Document ID: `prisma::/docs/cli/v7/migrate/resolve`
   Recorded heading(s): resolve

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
I would not manually create _prisma_migrations. The supported version of that idea is to baseline the existing database with prisma migrate resolve --applied.
P3005 is Prisma Migrate saying: "this database is not empty, but I have no migration history for it yet." That is expected for an existing production/tenant database.
For your case, since you intentionally do not want Prisma to model the legacy tables, I would use a no-op baseline migration for each existing tenant DB, then let Prisma manage only the new tables from that point forward.
Rough shape:
mkdir -p prisma/migrations/0_existing_database_baseline
printf '%s\n' '-- Baseline existing tenant database. Legacy tables are intentionally unmanaged by Prisma.' \
 > prisma/migrations/0_existing_database_baseline/migration.sql
npx prisma migrate resolve --applied 0_existing_database_baseline
npx prisma migrate deploy
Run the resolve --applied step once per existing tenant database before the first migrate deploy.
After that, future migrations that create/change only your Prisma-owned tables should deploy normally.
A few caveats:
Keep the baseline migration committed, so all environments share the same migration history.
Do not manually insert rows into _prisma_migrations; let prisma migrate resolve do it.
Prisma Client will only expose models in your Prisma schema, so leaving legacy tables out of schema.prisma is a reasonable boundary if the new app must not query them.
On MySQL, you do not have PostgreSQL-style schemas to isolate Prisma-owned objects inside the same database, so naming conventions and DB permissions are worth using as extra guardrails.
Docs:
Baselining: 
migrate resolve:
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-17-tailwind-css-tailwind-20353.md) | [Next case](case-19-supabase-supabase-27860.md)
