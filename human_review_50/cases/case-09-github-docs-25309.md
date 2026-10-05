<a id="case-09"></a>

# Case 09

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-08-prisma-prisma-15898.md) | [Next case](case-10-tailwind-css-tailwind-18456.md)

**Dataset:** GitHub Docs  
**Question ID:** `github-docs::25309`  
**Distinct linked documents:** 2  
**Original discussion:** [Source](https://github.com/orgs/community/discussions/25309)  
**Accepted answer:** [Source answer](https://github.com/orgs/community/discussions/25309#discussioncomment-3247426)

**Reviewer:** __________  **Date:** __________

### Question

```text
Priority for self-hosted runners
Hi,
I have several self-hosted runners (8 cores, and 4 cores machines) and would like to make sure that some machines are prioritized over others because these machines have stronger hardware.
I am not sure tags are the right way to go here because I’d like to have all different jobs always prefer the group with 8 cores and only use the 4-core machines when there are no “fast” ones available.
Any idea how to do that?
Thanks
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

```text
For GitHub Actions, use runner scope rather than labels to create this fallback order:

- Register the 8-core runners as repository-level self-hosted runners.
- Register the 4-core runners as organization-level self-hosted runners, and make sure the repository is allowed to use them.

Repository runners are considered first for workflow jobs. If no repository runner is available, GitHub Actions checks the organization runners. This makes the 8-core machines preferred while retaining the 4-core machines as a fallback.

Labels are useful for restricting jobs to runners with particular characteristics, but they are cumulative filters: a runner must match every label specified by the job. They do not provide this repository-before-organization priority.
```

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Adding self-hosted runners](../documents/D001-71d189e8772d.md)  
   Document ID: `github-docs::/actions/how-tos/manage-runners/self-hosted-runners/add-runners`
   Recorded heading(s): Adding a self-hosted runner to a repository

2. [Using self-hosted runners in a workflow](../documents/D002-83e444fd6568.md)  
   Document ID: `github-docs::/actions/how-tos/manage-runners/self-hosted-runners/use-in-a-workflow`
   Recorded heading(s): Using custom labels to route jobs

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
@taschik,
I am not sure tags are the right way to go here because I’d like to have all different jobs always prefer the group with 8 cores and only use the 4-core machines when there are no “fast” ones available.
If you set a job to run on the self-hosted runner with a specified label, the job will only use the available runners that have the specified label.
By default, the repository runners have the priority to be used for the workflow jobs in a repository. If there is not available repository runners, the jobs will check Organization runners. To view more details, you can see “Routing precedence for self-hosted runners”.
In your case, as a workaround, you can install the 8 cores runners as the repository runners and 4 cores runners as the Organization runners. More details, see “Adding self-hosted runners”.
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-08-prisma-prisma-15898.md) | [Next case](case-10-tailwind-css-tailwind-18456.md)
