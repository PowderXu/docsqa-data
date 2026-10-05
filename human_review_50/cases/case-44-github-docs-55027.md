<a id="case-44"></a>

# Case 44

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-43-github-docs-109354.md) | [Next case](case-45-github-docs-148518.md)

**Dataset:** GitHub Docs  
**Question ID:** `github-docs::55027`  
**Distinct linked documents:** 2  
**Original discussion:** [Source](https://github.com/orgs/community/discussions/55027)  
**Accepted answer:** [Source answer](https://github.com/orgs/community/discussions/55027#discussioncomment-5870126)

**Reviewer:** __________  **Date:** __________

### Question

```text
Run workflow only when the previous run is completed
Select Topic Area
Question
Hi Team,
I have a github workflow which will get triggered during on-merge. It has 3 jobs and i have only one runner. Right now manually i need to check whether there's no run in in-progress state, because if i trigger the workflow again then there is possibility that Jobs in Run 2 can pick the runner and job 1 will be in waiting state. Is there a way to stop, queue or disable workflow run if a workflow is already running.
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

````text
Use a workflow-level `concurrency` group so runs of this workflow cannot execute at the same time:

```yaml
concurrency:
  group: ${{ github.workflow }}
```

With this group, one workflow run can be running at a time. A later run waits in the `pending` state until the current run completes. By default, only one pending run is retained; if another run arrives, it replaces the existing pending run.

Choose the behavior you want:

- **Wait, keeping multiple runs:** add `queue: max`. Up to 100 runs can remain pending and will be processed one at a time.
- **Cancel the current run and start the newest:** add `cancel-in-progress: true` instead. This cannot be combined with `queue: max`.

For example, to serialize all runs of this workflow while retaining a queue:

```yaml
concurrency:
  group: ${{ github.workflow }}
  queue: max
```

Concurrency can also be configured on individual jobs, but putting it at the workflow level is the appropriate scope when all three jobs in each run must be protected from overlapping runs. If the restriction should be per branch rather than across all branches, include the branch reference in the group, such as the documented form `${{ github.workflow }}-${{ github.ref }}`.
````

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Control the concurrency of workflows and jobs](../documents/D004-b698d362ce10.md)  
   Document ID: `github-docs::/actions/how-tos/write-workflows/choose-when-workflows-run/control-workflow-concurrency`
   Recorded heading(s): Using concurrency in different scenarios; Example: Only cancel in-progress jobs or runs for the current workflow

2. [Workflow syntax for GitHub Actions](../documents/D008-60718db2d93c.md)  
   Document ID: `github-docs::/actions/reference/workflows-and-actions/workflow-syntax`
   Recorded heading(s): `concurrency`

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
To solve this you can use concurency groups either on the job level or on the workflow level. For you, probably the latter, for example
name: merge ci stuff
concurrency:
 group: ${{ github.workflow }}
which should only let workflows that fit this group run one at a time
you can also cancel runs from the same group when a new one is queued using cancel-in-progress: true
You can find examples for cuncurency groups here
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-43-github-docs-109354.md) | [Next case](case-45-github-docs-148518.md)
