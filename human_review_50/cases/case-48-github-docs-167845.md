<a id="case-48"></a>

# Case 48

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-47-tailwind-css-tailwind-13638.md) | [Next case](case-49-prisma-prisma-11953.md)

**Dataset:** GitHub Docs  
**Question ID:** `github-docs::167845`  
**Distinct linked documents:** 1  
**Original discussion:** [Source](https://github.com/orgs/community/discussions/167845)  
**Accepted answer:** [Source answer](https://github.com/orgs/community/discussions/167845#discussioncomment-13922282)

**Reviewer:** __________  **Date:** __________

### Question

```text
What is "Installation object"?
Select Topic Area
Question
I am developing project with GitHub App, and was looking at installation webhook event. ( 
So, when the user installs my GitHub app, GitHub will fire installation event to the app's webhook URL. My backend server is going to handle this webhook request.
However I have no clue how installation JSON object field looks like.
{
 "action": "created",
 // 👇 the installation object
 "installation": {
 "id": 78035...,
 "client_id": "Iv23liS1n.....",
 "account": {
 "login": "nyhryan",
 // ...
 },
 "repository_selection": "selected",
 "access_tokens_url": " 
// ...
I just created a test app and fired the installation webhook.
Does anyone know where can I find schema for installation object?

Image-derived question evidence:
- [img-055fc95d92499106] Webhook payload object for installation

Action type: created

Someone installed a GitHub App on a user or organization accou…

Webhook request body parameters

action    string    Required
Value: created

enterprise    object
An enterprise on GitHub. Webhook payloads contain the enterp…
on an enterprise account or an organization's that's part of an ent…
"About enterprise accounts."

installation    object    Required
Installation

organization    object
A documentation-style page is visible. At the top is a heading, followed by an action-type dropdown set to "created." A section titled "Webhook request body parameters" lists parameter entries. The "installation" entry is surrounded by a red rectangular outline. The right side of several lines is cut off by the image boundary.
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

```text
The `installation` object represents the GitHub App installation on a user, organization, or enterprise account. In an installation webhook payload, it uses the same object structure as the installation returned by the REST API; the webhook’s `action` (`created`, `deleted`, `suspend`, etc.) indicates what happened.

The schema and complete field definition are documented in the REST API documentation for GitHub App installations, under the procedure for getting an installation for the authenticated app. Common fields include:

- `id`: the installation ID used in API calls
- `account`: the user or organization that installed the app
- `repository_selection`: `all` or `selected`
- `access_tokens_url`: endpoint for generating installation access tokens
- `permissions`: permissions granted to the app
- `target_type`: `User` or `Organization`

The webhook documentation identifies `installation` as a required object in the request body, but its detailed structure is defined by the REST API installation object.
```

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [REST API endpoints for {% data variables.product.prodname_github_app %} installations](../documents/D032-d63cb0a2b236.md)  
   Document ID: `github-docs::/rest/apps/installations`
   Recorded heading(s): About GitHub App installations

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
Installation object schema isn't in that webhook docs page, it's in the REST API docs, maybe check here: 
The webhook payload uses the same installation object structure as the REST API response
Key fields you'll see:
id - Installation ID (need this for API calls)
account - User/org that installed the app
repository_selection - "all" or "selected"
access_tokens_url - For generating installation tokens
permissions - What your app can access
target_type - "User" or "Organization"
The installation object is the same across all installation webhook events (created, deleted, suspend, etc.); just the action field changes
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-47-tailwind-css-tailwind-13638.md) | [Next case](case-49-prisma-prisma-11953.md)
