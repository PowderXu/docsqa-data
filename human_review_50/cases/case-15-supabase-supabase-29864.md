<a id="case-15"></a>

# Case 15

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-14-supabase-supabase-34352.md) | [Next case](case-16-github-docs-5033.md)

**Dataset:** Supabase  
**Question ID:** `supabase::supabase-29864`  
**Distinct linked documents:** 2  
**Original discussion:** [Source](https://github.com/orgs/supabase/discussions/29864)  
**Accepted answer:** [Source answer](https://github.com/orgs/supabase/discussions/29864#discussioncomment-10929306)

**Reviewer:** __________  **Date:** __________

### Question

```text
Permission denied to set role 'admin'

I set as admin an user registered, in Supabase it says that he is admin but in my app when I get currentUser.role it says authenticated. Then when I sign out and sign in again now it says admin, and then the error permission denied to set role admin
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

```text
`authenticated` and your application’s `admin` role are different things.

The `role` claim is used by Supabase/Postgres as a database role. If you put `admin` in that claim, PostgreSQL must have a role named `admin`, and that role must be granted appropriately to `authenticator` and have access to the required schemas. Otherwise the request fails with `permission denied to set role 'admin'`.

For application roles, the safer pattern is not to replace the database role with `admin`. Store the role in an application table such as `user_roles`, add it to the JWT as a separate custom claim such as `user_role`, and check that claim in RLS policies. The documented RBAC example defines `admin` as an application enum value in `user_roles`, while authenticated users continue to use the normal `authenticated` database role.

The delayed change is consistent with JWT claims: the custom access-token hook runs before a token is issued. Updating the user’s role does not rewrite an already-issued token; the new claim appears when a new token is issued, such as after signing in again. Your app should therefore read the custom `user_role` claim and use it for application authorization, rather than expecting the database `role` to become `admin`.

To resolve it:

1. Use the documented custom-claims/RBAC design: create `user_roles`, store `admin` there, and configure the Custom Access Token Auth Hook to add `user_role` to the JWT.
2. Grant the hook permission to read `user_roles`, enable the hook, and revoke ordinary client access to that table as shown in the procedure.
3. In RLS, authorize actions from `auth.jwt() ->> 'user_role'`; keep the policy target as `authenticated`.
4. Sign out/sign in, or otherwise obtain a newly issued token, after changing the role. Inspect `user_role`, not the database `role`.

Only use `admin` as the JWT/database `role` if you intentionally created a PostgreSQL role named `admin` and granted it the required access. Otherwise, do not attempt to set the database role to `admin`; use the separate application claim.
```

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Custom Claims & Role-based Access Control (RBAC)](../documents/D069-17bdfddbba3d.md)  
   Document ID: `supabase::/docs/guides/api/custom-claims-and-role-based-access-control-rbac`
   Recorded heading(s): Custom Claims & Role-based Access Control (RBAC); Create Auth Hook to apply user role; Create a table to track user roles and permissions; Accessing custom claims in RLS policies

2. [Custom Roles](../documents/D076-c24b074a8e6d.md)  
   Document ID: `supabase::/docs/guides/storage/schema/custom-roles`

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
Are you using a guide for this?
How are you setting the role claim?
Also you can't just change the role claim to anything. There has to be a Postgres role defined with that name and granted access to the authenticator role and granted access to the database schemas.
In general using a postgres role and the role claim is not the recommended way to do custom roles. Here is one guide from Supabase on roles (but not using the role claim). 
Link with a bit of info on doing the Postgres role approach:
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-14-supabase-supabase-34352.md) | [Next case](case-16-github-docs-5033.md)
