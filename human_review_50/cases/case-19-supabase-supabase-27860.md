<a id="case-19"></a>

# Case 19

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-18-prisma-prisma-29524.md) | [Next case](case-20-prisma-prisma-11775.md)

**Dataset:** Supabase  
**Question ID:** `supabase::supabase-27860`  
**Distinct linked documents:** 2  
**Original discussion:** [Source](https://github.com/orgs/supabase/discussions/27860)  
**Accepted answer:** [Source answer](https://github.com/orgs/supabase/discussions/27860#discussioncomment-12245215)

**Reviewer:** __________  **Date:** __________

### Question

```text
Question on best practice for Supabase branching for development and production

Hi guys! I'm seeking clarification on the best practice for implementing Supabase branching in my project. The documentation warns against using branching in a "production setting," but also describes merging branches within a single project. I'm unsure whether I should create two separate Supabase projects (one for production and one for development with branches) or use a single project with a main "production" branch and separate development branches. My app is still in the development stage, but I want to set up a proper workflow that separates development and production environments while leveraging the new branching feature. How should I structure my Supabase project(s) to best utilize branching while following best practices for development and eventual production use? Thank you so much for your help!
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

```text
The recommended setup is a **single Supabase production project with branching enabled**, rather than a separate development project whose branches are later promoted to another project.

Use the project’s main branch as the production environment. For each change, create a development branch—typically through a pull request. Each branch is an isolated Supabase environment with its own instance and API credentials, so you can test schema, configuration, and application changes without affecting production. Preview branches are temporary and are deleted when the pull request is merged or closed; if you need a long-lived development or staging environment, use a persistent branch instead.

Put every database change in a migration file and submit it through the pull request. When the pull request is merged into the main project, Supabase automatically applies the migration changes to the production project. This gives you development isolation while keeping production as the deployment target.

A practical workflow is:
1. Develop locally and create migration files.
2. Open a pull request, which creates an isolated preview branch.
3. Test the application and migrations against that branch.
4. Merge the pull request only after review and testing.
5. Let the branching deployment workflow apply the migrations and deploy the changes to the main production project.

The warning about using branching in a production setting should therefore be understood in the context of how branches are used: do not treat a production branch as an experimental environment. Keep production on the main project and use its isolated development or staging branches for testing, then merge approved changes into production.
```

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Branching](../documents/D071-37d756506496.md)  
   Document ID: `supabase::/docs/guides/deployment/branching`
   Recorded heading(s): Branching; How branching works; Deploying to production

2. [Database Migrations](../documents/D072-0f266915840d.md)  
   Document ID: `supabase::/docs/guides/deployment/database-migrations`
   Recorded heading(s): Working with a team

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
Hi @wusixuan0, we have updated our branching docs recently to clarify the best practices for development and promoting to production. Typically we would recommend
A single production project with branching enabled.
Each pull request creates a development branch.
Add all database migrations through PRs.
When you merge a PR, branching will automatically apply changes from your migration files to your production project.
Feel free to reach out if you have other questions.
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-18-prisma-prisma-29524.md) | [Next case](case-20-prisma-prisma-11775.md)
