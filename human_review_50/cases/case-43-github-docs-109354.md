<a id="case-43"></a>

# Case 43

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-42-github-docs-88452.md) | [Next case](case-44-github-docs-55027.md)

**Dataset:** GitHub Docs  
**Question ID:** `github-docs::109354`  
**Distinct linked documents:** 1  
**Original discussion:** [Source](https://github.com/orgs/community/discussions/109354)  
**Accepted answer:** [Source answer](https://github.com/orgs/community/discussions/109354#discussioncomment-11151835)

**Reviewer:** __________  **Date:** __________

### Question

```text
Scheduled Github Action stops working if last committer deletes their accounts
Select Topic Area
Bug
I noticed this issue when merging my personal and work account. My previous work account was the latest committer of the workflows, and now when I deleted that account, the scheduled workflows are not running any more. If this is intended, I think there should be a warning displayed or a mail sent to other active users of the repository.
Thanks!
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

```text
Yes—this behavior is documented for enterprises using Enterprise Managed Users. A scheduled workflow requires its associated `actor` account to be active; if that account is deleted or deprovisioned by the identity provider, the scheduled workflow will not run. This is tied to the account’s status, not merely to whether the user remains a member of the organization.

To reactivate a deactivated scheduled workflow, a user with `write` permission can commit a change to the workflow’s `cron` schedule. That user then becomes the actor for subsequent scheduled runs. The documentation also states that scheduled-workflow notifications are sent to the user who last modified the cron syntax; it does not document a warning or email to other active repository users when that account is deleted.

If the repository does not use Enterprise Managed Users, the supplied documentation only specifically says that removing a user from an organization does not prevent scheduled workflows from running, so the account-deletion scenario would need separate investigation.
```

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Events that trigger workflows](../documents/D006-b5a97cbc3e86.md)  
   Document ID: `github-docs::/actions/reference/workflows-and-actions/events-that-trigger-workflows`
   Recorded heading(s): `actor` for scheduled workflows

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
This behaviour is documented in the workflows documentation now, see
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-42-github-docs-88452.md) | [Next case](case-44-github-docs-55027.md)
