<a id="case-35"></a>

# Case 35

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-34-prisma-prisma-3163.md) | [Next case](case-36-github-docs-23427.md)

**Dataset:** Supabase  
**Question ID:** `supabase::supabase-45668`  
**Distinct linked documents:** 2  
**Original discussion:** [Source](https://github.com/orgs/supabase/discussions/45668)  
**Accepted answer:** [Source answer](https://github.com/orgs/supabase/discussions/45668#discussioncomment-16839725)

**Reviewer:** __________  **Date:** __________

### Question

```text
The API documentation page cannot be found in the `supabase/studio:2026.05.04-sha-e540f90`

The API documentation page cannot be found in the supabase/studio:2026.05.04-sha-e540f90
在 supabase/studio:2026.05.04-sha-e540f90 这个版本中找不到 API 文档页面。
There is no "API Docs" option in the sidebar, nor is it available in the preview feature.
侧边栏中没有 API Docs 选项了，预览特性中也没有：
I really need this button!
我真的很需要这个按钮！

Image-derived question evidence:
- [img-f1d49a0012c2e989] 客户关系管理
Connect
Project Overview
Table Editor
SQL Editor
Database
Authentication
Storage
Edge Functions
Realtime
Advisors
Logs
Integrations
Project Settings
A dark-themed application sidebar is visible. At the top left is a green lightning-shaped logo, followed by the title “客户关系管理”. At the top right is a rounded button labeled “Connect” with a link/connection icon. The navigation menu is divided by horizontal separator lines. “Project Overview” is highlighted with a darker rounded rectangle and a home icon. The remaining navigation items appear below with icons: “Table Editor”, “SQL Editor”, “Database”, “Authentication”, “Storage”, “Edge Functions”, “Realtime”, “Advisors”, “Logs”, “Integrations”, and “Project Settings”.
- [img-52a7eceaf265e22a] Dashboard feature previews
Get early access to new features and give feedback
RLS Tester
NEW
Column-level privileges
RLS Tester
Give feedback
Disable feature

Verify if your RLS policies have been set up properly by running queries as a specific user. While role impersonation isn't a new feature on the dashboard, we've built a dedicated UI for this which will also show what policies are evaluated for the query.

What data can my users see?
See what data a user is allowed to read based on your RLS policies
Test as
Anonymous user
Not logged in
Authenticated user
A specific logged in user
Select which user to test as
test001@gmail.com
Query
1  select * from blog_posts;

Summary
CAN ACCESS
Policies applied
Data preview
Ran as test001@gmail.com
ID: 8db26d9c-544e-4a3a-9232-7b59644a548c
Table access
public.blog_posts
1 policy applies for the authenticated role on this table. Only rows that match this condition are returned.
1 POLICY APPLIED
Blog posts: select own
Show rows where: (author = ( SELECT auth.uid() AS uid))

Enabling this preview will:
• Show the "Test" button on the Authentication Policies page
A dark modal titled "Dashboard feature previews" is open. A close X appears in the upper-right corner. The left navigation lists "RLS Tester" as the selected item with a green eye icon and a "NEW" badge, and "Column-level privileges" below it with a green eye icon. The main panel is titled "RLS Tester" and has "Give feedback" and "Disable feature" buttons. A descriptive paragraph appears above a large embedded dark UI screenshot. The screenshot shows a user-testing form on the left and a results panel on the right. Below the screenshot is the heading "Enabling this preview will:" followed by one visible bullet item. A vertical scrollbar is visible on the right side of the modal, with additional content below the visible area.
- [img-c81064923643ca19] 客户关系管理
Connect

Project Overview
Table Editor
SQL Editor

Database
Authentication
Storage
Edge Functions
Realtime

Advisors
Logs
API Docs
Integrations

Project Settings

Authentication
MANAGE
Users
CONFIGURATION
Policies

Users
Email address
Search
UID

Total: 68 users

API Docs
JS

Connect
User Management
Tables & Views
Introduction
Generating Types
GraphQL vs PostgREST

Stored Procedures
Storage
Edge Functions
Realtime

GraphiQL
GraphiQL guide

Documentation
REST guide

Introduction
All views and tables in the public schema, and those accessible by the active database role for a request are available for querying via the API.
If you don't want to expose tables in your API, simply add them to a different schema (not the public schema).

Generating Types
Supabase APIs are generated from your database, which means that we can use database introspection to generate type-safe API definitions.
You can generate types from your database either through the Supabase CLI, or by downloading the types file via the button on the right and importing it in your application within src/index.ts.

Docs
Generate and download types
Remember to re-generate and download this file as you make changes to your tables.

GraphQL vs PostgREST
If you have a GraphQL backend, you might be wondering if you can fetch your data in a single round-trip.
The answer is yes! The syntax is very similar. This example shows how you might achieve the same thing with Apollo GraphQL and Supabase.
Still want GraphQL? If you still want to use GraphQL, you can. Supabase provides you with a full Postgres database, so as long as your middleware can connect to the database then you can still use the tools you love.
You can find the database connection details in the settings.

// With Apollo GraphQL
const { loading, error, data } = useQuery(gql`
  query GetDogs {
    dogs {
      id
      breed
      owner {
        id
        name
      }
    }
  }
`)

// With Supabase
const { data, error } = await supabase
  .from('dogs')
  .select(`
    id, breed,
      owner (id, name)
  `)
A dark-themed web application is visible. The left sidebar shows project navigation, with Authentication selected. The center-left area shows an Authentication/Users page dimmed in the background, including a user list and a horizontal scrollbar. A tall API Docs navigation panel is open in the middle, with Tables & Views highlighted and Introduction, Generating Types, and GraphQL vs PostgREST listed beneath it. The main right panel displays documentation sections titled Introduction, Generating Types, and GraphQL vs PostgREST, along with two code examples. A red vertical arrow points upward toward the “Generate and download types” button. Two circular floating icons are visible on the right side.
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

```text
The API documentation location changed in this version; it is no longer accessed from the sidebar or the preview-feature menu. Open **Integrations → Data API → Docs**, then select **Introduction** under **Tables and Views**. This UI change also applies to self-hosted Supabase and Supabase CLI environments.
```

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Self-Hosting](../documents/D074-e1584f449a40.md)  
   Document ID: `supabase::/docs/guides/self-hosting`
   Recorded heading(s): How self-hosted Supabase differs

2. [Local Development & CLI](../documents/D073-58c4035c17d8.md)  
   Document ID: `supabase::/docs/guides/local-development`
   Recorded heading(s): Local Development & CLI

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
This part of the UI has changed on the platform, and consequently in self-hosted Supabase (and CLI). Check: Integrations > Data API > Docs (see Introduction in "Tables and Views," etc.)
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-34-prisma-prisma-3163.md) | [Next case](case-36-github-docs-23427.md)
