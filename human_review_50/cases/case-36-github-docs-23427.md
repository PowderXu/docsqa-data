<a id="case-36"></a>

# Case 36

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-35-supabase-supabase-45668.md) | [Next case](case-37-github-docs-22539.md)

**Dataset:** GitHub Docs  
**Question ID:** `github-docs::23427`  
**Distinct linked documents:** 1  
**Original discussion:** [Source](https://github.com/orgs/community/discussions/23427)  
**Accepted answer:** [Source answer](https://github.com/orgs/community/discussions/23427#discussioncomment-3240318)

**Reviewer:** __________  **Date:** __________

### Question

```text
What event is triggered for turning a Draft PR into a PR?
Hopefully a simple question: What event is triggered when you turn a Draft PR into a PR? Is there even any event fired? And if so, will it be visible in 
I participate in a GitHub Action to display the latest activities you made on GitHub and this question came up, so I wanted to ask here in the hope that there is a good answer.
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

```text
Yes. Turning a draft pull request into a non-draft pull request triggers a pull request webhook. Inspect the webhook payload’s `action` field; it records state changes between draft and non-draft states. Whether this appears in your activity display cannot be determined from the question because the destination/interface is unspecified. The supplied evidence confirms the webhook event, but not how a particular activity display presents it.
```

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Webhook events and payloads](../documents/D044-290fa150fadc.md)  
   Document ID: `github-docs::/webhooks/webhook-events-and-payloads`
   Recorded heading(s): About webhook events and payloads

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
Hey @Andre601 ! I think there is a webhook that fires for that:
Check out the action key in the payload, it has support for state changes between draft and non-draft states.
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-35-supabase-supabase-45668.md) | [Next case](case-37-github-docs-22539.md)
