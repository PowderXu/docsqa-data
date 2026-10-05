<a id="case-28"></a>

# Case 28

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-27-tailwind-css-tailwind-19697.md) | [Next case](case-29-tailwind-css-tailwind-13967.md)

**Dataset:** GitHub Docs  
**Question ID:** `github-docs::24740`  
**Distinct linked documents:** 4  
**Original discussion:** [Source](https://github.com/orgs/community/discussions/24740)  
**Accepted answer:** [Source answer](https://github.com/orgs/community/discussions/24740#discussioncomment-3245292)

**Reviewer:** __________  **Date:** __________

### Question

```text
Is it possible to find the project boards an issue is associated with using the REST API?
I’m developing a Github webhook that gets notifications on issue updates.
These issues are associated to one of more Github Project Boards
The body payload shows this information related to the updated issue:
image233×640 58 KB
Nothing about issue association with project boards. Is there a way to get this information?

Image-derived question evidence:
- [img-e2813a89bcbb4113] value = {LinkedHashMap...
"url" -> "`https://api.g`...
"repository_url" -> "`https://`...
"labels_url" -> "https:...
"comments_url" -> "h...
"events_url" -> "https...
"html_url" -> "`https://`...
"id" -> {Integer...
"node_id" -> "MDU6S...
"number" -> {Integer...
"title" -> "the issue!"
"user" -> {LinkedHash...
"labels" -> {ArrayList...
"state" -> "open"
"locked" -> {Boolean...
"assignee" -> {Linked...
"assignees" -> {Array...
"milestone" -> null
"comments" -> {Inte...
"created_at" -> "2020...
"updated_at" -> "202...
"closed_at" -> null
"author_association" -> ...
"active_lock_reason" -> ...
"body" -> "issuea"
A vertically cropped dark-themed debugger or object-inspection view shows a top-level `value` entry followed by key-value rows. Each row has a disclosure triangle and a small stacked-line icon. The right side of the values is cut off by the image boundary.
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

```text
The issue response itself does not include the project board association. To find it, use the Projects API to list the cards for each project board, then inspect each card’s `content_url`. If that field points to the issue’s URL, the issue is associated with that board. Repeat this for the boards you need to check.
```

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [REST API endpoints for issues](../documents/D034-43a3e7640973.md)  
   Document ID: `github-docs::/rest/issues`
   Recorded heading(s): REST API endpoints for issues

2. [REST API endpoints for draft Project items](../documents/D035-a556b24052a5.md)  
   Document ID: `github-docs::/rest/projects/drafts`
   Recorded heading(s): REST API endpoints for draft Project items

3. [REST API endpoints for Project fields](../documents/D036-e41de86eb950.md)  
   Document ID: `github-docs::/rest/projects/fields`
   Recorded heading(s): REST API endpoints for Project fields

4. [REST API endpoints for Project items](../documents/D037-3ac95dfdc162.md)  
   Document ID: `github-docs::/rest/projects/items`
   Recorded heading(s): REST API endpoints for Project items

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
👋 hello there @svpr3m0, and welcome to the GitHub Support Community!
Making a request to the REST API for getting an issue will not include the project that an issue is a part of.
Instead, you can go through the list of cards in the project (using the Projects API, specifically the list project cards endpoint).
When you fetch a card, the content_url field will point to an issue if the card was created from an issue. I hope this helps!
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-27-tailwind-css-tailwind-19697.md) | [Next case](case-29-tailwind-css-tailwind-13967.md)
