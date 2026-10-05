<a id="case-16"></a>

# Case 16

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-15-supabase-supabase-29864.md) | [Next case](case-17-tailwind-css-tailwind-20353.md)

**Dataset:** GitHub Docs  
**Question ID:** `github-docs::5033`  
**Distinct linked documents:** 1  
**Original discussion:** [Source](https://github.com/orgs/community/discussions/5033)  
**Accepted answer:** [Source answer](https://github.com/orgs/community/discussions/5033#discussioncomment-2318478)

**Reviewer:** __________  **Date:** __________

### Question

```text
Support --ignore-revs-file for blame view to support automated code formatters
When using automated code formatters to format a legacy project (read: code not matching an automated code formatter's style) it would be splendid to be able to make sure the commits related to the reformatting wouldn't be taken into account in GitHub's blame page.
Here's some background in the docs for Python's popular "black" code formatter: 
A long-standing argument against moving to automated code formatters like Black is that the migration will clutter up the output of git blame. This was a valid argument, but since Git version 2.23, Git natively supports ignoring revisions in blame with the --ignore-rev option. You can also pass a file listing the revisions to ignore using the --ignore-revs-file option. The changes made by the revision will be ignored when assigning blame. Lines modified by an ignored revision will be blamed on the previous revision that modified those lines.
In case anyone wants to spread the call for this feature in their network, feel free to retweet 🥳
NOTE: Please use the arrow in the top left corner (on Desktop) or below the text (on mobile) to upvote this, in addition to the 👍🏻!
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

```text
Yes. GitHub’s blame view supports this through a repository-root file named `.git-blame-ignore-revs`.

1. Create `.git-blame-ignore-revs` in the root of the repository.
2. Add the commit hashes for formatter or other large-scale reformatting commits, optionally with comments describing each commit.
3. Commit and push the file.

GitHub will load the blame view using Git’s `--ignore-revs-file` behavior and exclude the listed revisions when assigning blame. The blame page displays an “Ignoring revisions in .git-blame-ignore-revs” banner when this is active. A revision can still appear if it was the last commit to modify a line. The same file can be used locally with `git blame --ignore-revs-file .git-blame-ignore-revs`.
```

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Viewing and understanding files](../documents/D031-2d25f2a351a8.md)  
   Document ID: `github-docs::/repositories/working-with-files/using-files/viewing-and-understanding-files`
   Recorded heading(s): Ignore commits in the blame view

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
Update:
Ignoring commits in the blame view is available as a public beta to anyone now 🎉 For more information see the documentation.
Hey everyone 👋 we have an early version available in a private beta and would love to get a few more thoughts. If anyone is interested in trying it out early, please let me know with a comment below and we'll enable it for you or your organization account.
Once enabled, you must add a file called .git-blame-ignore-revs to the root level of your repository. That file must contain the revisions (commit hashes) you want to ignore. The blame view of the repository will then be loaded with the --ignore-revs-file parameter and ignores the specified revisions.
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-15-supabase-supabase-29864.md) | [Next case](case-17-tailwind-css-tailwind-20353.md)
