<a id="case-11"></a>

# Case 11

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-10-tailwind-css-tailwind-18456.md) | [Next case](case-12-prisma-prisma-20554.md)

**Dataset:** GitHub Docs  
**Question ID:** `github-docs::120943`  
**Distinct linked documents:** 2  
**Original discussion:** [Source](https://github.com/orgs/community/discussions/120943)  
**Accepted answer:** [Source answer](https://github.com/orgs/community/discussions/120943#discussioncomment-9209743)

**Reviewer:** __________  **Date:** __________

### Question

```text
Maximum Repository Size?
Select Topic Area
Question
Is there any limitation as to how large a single GitHub Repository can be, and are there any differences in that regard for Teams/Enterprise Organisation or Pro-Users compared to non-paying users? I know that there is a limit to how large a singular file can be to be uploaded to GitHub.
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

```text
GitHub does not specify a fixed maximum total size for a single repository. Instead, it recommends keeping repositories ideally below 1 GB and strongly recommends staying below 5 GB. If a repository excessively affects GitHub’s infrastructure, GitHub Support may ask for corrective action.

There is no separate documented repository-total limit for Free, Pro, Team, or Enterprise plans; the plan differences concern individual-file limits. For Git LFS, the documented maximum file sizes are 2 GB for GitHub Free and Pro, 4 GB for GitHub Team, and 5 GB for GitHub Enterprise Cloud. These are per-file limits, not limits on the repository’s total size.
```

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [About Git Large File Storage](../documents/D029-1b8b07e8c621.md)  
   Document ID: `github-docs::/repositories/working-with-files/managing-large-files/about-git-large-file-storage`
   Recorded heading(s): About Git Large File Storage

2. [About large files on GitHub](../documents/D030-e11b141d30e9.md)  
   Document ID: `github-docs::/repositories/working-with-files/managing-large-files/about-large-files-on-github`
   Recorded heading(s): File size limits; Repository size limits

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
The difference between the various github plans refers only to the maximum size of individual files. As regards the maximum repository size, there is no fixed one but the recommendation is to stay under 5GB.
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-10-tailwind-css-tailwind-18456.md) | [Next case](case-12-prisma-prisma-20554.md)
