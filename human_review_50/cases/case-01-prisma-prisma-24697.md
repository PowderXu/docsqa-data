<a id="case-01"></a>

# Case 01

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Next case](case-02-prisma-prisma-12782.md)

**Dataset:** Prisma
**Question ID:** `prisma::prisma-24697`
**Distinct linked documents:** 2
**Original discussion:** [Source](https://github.com/prisma/prisma/discussions/24697)
**Accepted answer:** [Source answer](https://github.com/prisma/prisma/discussions/24697#discussioncomment-9950977)

**Reviewer:** __________  **Date:** __________

### Question

```text
Azure SQL server connection using Azure Directory password

Question
Is it possible to connect to a Azure SQL server using a Active Directory password ? If so can you give an example because i am facing P1000 Error
How to reproduce (optional)
Expected behavior (optional)
No response
Information about Prisma Schema, Client Queries and Environment (optional)
// Add your schema.prisma
// Add any relevant Prisma Client queries here
OS: 
Database: 
Node.js version: 
Run prisma -v to see your Prisma version and paste it
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

````text
Yes. Prisma can connect to SQL Server using an Active Directory username and password by setting `integratedSecurity=true` and supplying `username` and `password` in the SQL Server connection string.

Example:

```text
sqlserver://your-server:1433;database=your-database;integratedSecurity=true;username=your-ad-user;password=your-ad-password;trustServerCertificate=true;
```

Replace the server, database, Active Directory username, and password with your actual values. Store this connection string in the connection URL configuration used by your Prisma setup.

A `P1000` error indicates that authentication failed. Verify that the credentials are valid for the Azure SQL server and that the Active Directory user has access to the target database. Also escape special characters in connection-string values; the documented format uses curly braces around values containing characters such as `:`, `\\`, `=`, `;`, `/`, `[`, `]`, or `{`/`}`. For example:

```text
password={Pass:Word;}
```
````

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [SQL Server](../documents/D055-b76c53ff3ffe.md)  
   Document ID: `prisma::/docs/orm/v7/core-concepts/supported-databases/sql-server`
   Recorded heading(s): Connection details; Windows authentication
2. [Microsoft SQL Server](../documents/D050-350e90ca5fc1.md)
   Document ID: `prisma::/docs/orm/v6/overview/databases/sql-server`
   Recorded heading(s): Using integrated security (Windows only); Connection details

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
Hi @Elucidator2197 👋
It is possible to connect to an Azure SQL server using an Active Directory password. You can use a connection string that includes the integratedSecurity parameter along with the username and password parameters.
Here is an example connection string for connecting to an Azure SQL server using an Active Directory password:
sqlserver://localhost:1433;database=sample;integratedSecurity=true;username=prisma;password=aBcD1234;trustServerCertificate=true;
See this section of the documentation.
Make sure to replace localhost:1433, sample, prisma, and aBcD1234 with your actual server address, database name, Active Directory username, and password respectively. If you are facing the P1000 error, it indicates that the authentication failed. Ensure that the provided database credentials are correct and valid for the database server you are trying to connect to. For Microsoft SQL Server, you must escape special characters in any part of your connection string.
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Next case](case-02-prisma-prisma-12782.md)
