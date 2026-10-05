<a id="case-14"></a>

# Case 14

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-13-github-docs-24939.md) | [Next case](case-15-supabase-supabase-29864.md)

**Dataset:** Supabase  
**Question ID:** `supabase::supabase-34352`  
**Distinct linked documents:** 1  
**Original discussion:** [Source](https://github.com/orgs/supabase/discussions/34352)  
**Accepted answer:** [Source answer](https://github.com/orgs/supabase/discussions/34352#discussioncomment-12592647)

**Reviewer:** __________  **Date:** __________

### Question

```text
Select certain foreign key field causes 403 error

Hi, I'm having trouble with creating an appropriate row-level security policy for a table for messages sent between a sender and receiver.
For context, I have defined a notes table with an id, note (text), author_id (foreign key to auth.users.id) and receiver_id (foreign key to auth.users.id). I have added the following select security policy:
alter policy "Enable users to view their own data only"
on "public"."notes"
to authenticated
using (
 ((( SELECT auth.uid() AS uid) = author_id) OR (( SELECT auth.uid() AS uid) = receiver_id))
);
When I attempt to impersonate one of the users in the SQL Editor, and use the following query, it succeeds fine:
select id, note from notes;
However, once I try using this query, I get this error:
select id, note, receiver_id from notes;
-- ERROR: 42501: permission denied for table notes
Could someone please explain why this is happening, and how I can fix this (either by fixing the policy, or designing the schema differently).
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

```text
The failure is caused by column-level privileges, not by the `receiver_id` foreign key or by the `USING` expression in the RLS policy.

Your RLS policy controls which rows an authenticated user may see: rows where `auth.uid()` matches either `author_id` or `receiver_id`. RLS does not, by itself, control which columns can be selected. PostgreSQL column-level privileges can independently allow or deny access to individual columns. Therefore, the first query succeeds because its selected columns are permitted, while adding `receiver_id` fails with PostgreSQL error `42501` (surfaced by the client as a 403-style permission error).

To fix it, open the table's **Column Privileges** settings, select schema `public`, table `notes`, and role `authenticated`, then enable **Select** for `receiver_id`. The accepted resolution indicates that Select needed to be enabled on all fields used by the query editor. Keep the existing RLS policy so it continues to restrict the visible rows.

Alternatively, if column-level restrictions are intentional, grant Select only for the specific columns clients should read and query those columns explicitly. Do not rely on the RLS policy to grant column access; it only supplies the row-level condition.
```

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Column Level Security](../documents/D070-428d142a47b9.md)  
   Document ID: `supabase::/docs/guides/database/postgres/column-level-security`
   Recorded heading(s): Column Level Security; Policies at the row level; Privileges at the column level

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
It appears that the solution is to configure "Column Level Security" (which is a feature in Alpha, so it's disabled by default).
Find out more on this page about how to use CLS - 
In short, I had to enable "Select" on all fields of the table for "select" to work in the query editor.
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-13-github-docs-24939.md) | [Next case](case-15-supabase-supabase-29864.md)
