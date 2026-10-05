<a id="case-46"></a>

# Case 46

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-45-github-docs-148518.md) | [Next case](case-47-tailwind-css-tailwind-13638.md)

**Dataset:** Prisma  
**Question ID:** `prisma::prisma-13456`  
**Distinct linked documents:** 2  
**Original discussion:** [Source](https://github.com/prisma/prisma/discussions/13456)  
**Accepted answer:** [Source answer](https://github.com/prisma/prisma/discussions/13456#discussioncomment-2854663)

**Reviewer:** __________  **Date:** __________

### Question

```text
Issue when migrating DB changes in production on AWS

Hi everyone.
I'm deploying an app with CodeBuild, RDS, and ECS. My CICD (CodeBuild) is in one AWS account, and other services (RDS and ECS) are in another AWS account. I'm not sure where I should put the npx prisma migrate deploy in the CICD to migrate the changes to the DB in RDS? Is it possible to only run it after the ECS container deploys successfully?
Thank you.
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

```text
Run `npx prisma migrate deploy` as a step in the automated CI/CD pipeline, rather than from a developer’s local environment. The pipeline should include the `prisma/migrations` directory and provide the production `DATABASE_URL` securely to the migration step.

You can place the migration step after the ECS deployment step and configure it to run only when that deployment succeeds, provided your CI/CD system supports ordered, success-gated steps. The exact placement is platform-dependent; Prisma’s deployment guidance shows `migrate deploy` as a pipeline or release-phase step.

Conceptually, the flow is:

1. Build and deploy the ECS container.
2. Wait for the ECS deployment step to succeed.
3. Run `npx prisma migrate deploy` with the production RDS connection string supplied securely.

Do not temporarily put the production connection string in a local `.env` file or run the production migration manually from a workstation. Prisma recommends an automated CI/CD pipeline for this operation.
```

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Deploy migrations from a local environment](../documents/D058-eccc4a48c875.md)  
   Document ID: `prisma::/docs/orm/v7/prisma-client/deployment/deploy-migrations-from-a-local-environment`
   Recorded heading(s): Local CI/CD pipeline

2. [Deploying database changes with Prisma Migrate](../documents/D057-6c8c66797fcf.md)  
   Document ID: `prisma::/docs/orm/v7/prisma-client/deployment/deploy-database-changes-with-prisma-migrate`
   Recorded heading(s): Deploying database changes with Prisma Migrate; Deploying database changes using GitHub Actions

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
Hey @lequydinh 👋
It's recommended that the npx prisma migrate deploy command should be a part of an automated CI/CD pipeline, and we do not generally recommend running this command locally to deploy changes to a production database (for example, by temporarily changing the DATABASE_URL environment variable). It is not generally considered good practice to store the production database URL locally.
Here's the reference on how database changes should be deployed with Prisma Migrate: Reference
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-45-github-docs-148518.md) | [Next case](case-47-tailwind-css-tailwind-13638.md)
