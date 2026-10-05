<a id="case-32"></a>

# Case 32

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-31-prisma-prisma-27294.md) | [Next case](case-33-prisma-prisma-14469.md)

**Dataset:** GitHub Docs  
**Question ID:** `github-docs::147941`  
**Distinct linked documents:** 1  
**Original discussion:** [Source](https://github.com/orgs/community/discussions/147941)  
**Accepted answer:** [Source answer](https://github.com/orgs/community/discussions/147941#discussioncomment-11666988)

**Reviewer:** __________  **Date:** __________

### Question

```text
Loading failed for the <script> with source “https://samikhan69420.github.io/flutter_bootstrap.js”.
Select Topic Area
Question
I made a repo to host my portfolio website and at first, I was using the main branch to host the source code for my site but I made this site in flutter so it didn't show the source code it only showed the compiled javascript, so I made a separate branch for the compiled javascript source code and wanted to push the flutter source code on the main branch, the original link for the website was but after adding the new branch and changing the repository name to "portfolio", it changed to ﻿ and then it started giving an error which says "Loading failed for the <script> with source “ notice how it does not include the "/portfolio" extention. How do I make it so it changes back to without the "portfolio" extention.
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

```text
Rename the GitHub repository currently named `portfolio` back to its original name. GitHub Pages uses the repository name in the default URL for a project site, so renaming it to `portfolio` adds `/portfolio` to the site path. Your Flutter output still requests `flutter_bootstrap.js` from the site root, which causes the script-loading failure when the site is actually being served under that subdirectory.

If the intended site is a user site at the root of your account’s `github.io` domain, the repository must use the account’s required `<owner>.github.io` name. After restoring the original repository name, allow GitHub Pages to republish the site and use the resulting root-level address.
```

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [What is {% data variables.product.prodname_pages %}?](../documents/D027-f51085d973aa.md)  
   Document ID: `github-docs::/pages/getting-started-with-github-pages/what-is-github-pages`
   Recorded heading(s): Types of GitHub Pages sites

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
You have to rename your repo name back to what it originally was. The reason was that, when you host a website on GitHub Pages under a project repo (i.e., not a repository named username.github.io), GitHub will try to serve the site under a URL that includes the repo name as a subdirectory, in your case.
source:
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-31-prisma-prisma-27294.md) | [Next case](case-33-prisma-prisma-14469.md)
