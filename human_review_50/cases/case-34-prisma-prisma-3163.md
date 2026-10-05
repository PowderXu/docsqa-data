<a id="case-34"></a>

# Case 34

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-33-prisma-prisma-14469.md) | [Next case](case-35-supabase-supabase-45668.md)

**Dataset:** Prisma  
**Question ID:** `prisma::prisma-3163`  
**Distinct linked documents:** 2  
**Original discussion:** [Source](https://github.com/prisma/prisma/discussions/3163)  
**Accepted answer:** [Source answer](https://github.com/prisma/prisma/discussions/3163#discussioncomment-43857)

**Reviewer:** __________  **Date:** __________

### Question

```text
Prisma application on Cpanel hosted nodejs application

Most of the web hosting available are of the type shared. I wonder if prisma application can be deployed in cpanel hosting environment while developing Node.js application.
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

```text
Yes. A Prisma application can be deployed as a Node.js application on cPanel-hosted shared hosting; the deployment is generally the same as for a traditional Node.js app. The important Prisma-specific step is to generate or include the query-engine binary for the hosting server’s operating system. Configure the appropriate `binaryTargets` value in the Prisma generator—rather than relying only on `native` generated on your local machine—and run `npx prisma generate` during the build/deployment process. The supplied information confirms general feasibility, but whether a particular shared host supports your application depends on that host’s Node.js, database, and permission configuration.
```

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Generators](../documents/D065-1cc69fe7614a.md)  
   Document ID: `prisma::/docs/orm/v7/prisma-schema/overview/generators`
   Recorded heading(s): `prisma-client-js` (Deprecated); 2. Generate Prisma Client

2. [Generators](../documents/D053-6a15355bc94b.md)  
   Document ID: `prisma::/docs/orm/v6/prisma-schema/overview/generators`
   Recorded heading(s): Binary targets

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
Hey @saugatdai 👋
Yes it can be. Deploying a Prisma application is no different than deploying a traditional Node app to Cpanel :)
You would just need to add the specific binary target as deined here based on the operating system.
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-33-prisma-prisma-14469.md) | [Next case](case-35-supabase-supabase-45668.md)
