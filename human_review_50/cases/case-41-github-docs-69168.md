<a id="case-41"></a>

# Case 41

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-40-github-docs-64750.md) | [Next case](case-42-github-docs-88452.md)

**Dataset:** GitHub Docs  
**Question ID:** `github-docs::69168`  
**Distinct linked documents:** 2  
**Original discussion:** [Source](https://github.com/orgs/community/discussions/69168)  
**Accepted answer:** [Source answer](https://github.com/orgs/community/discussions/69168#discussioncomment-7185113)

**Reviewer:** __________  **Date:** __________

### Question

````text
Why I cant create task list?
Select Topic Area
Question
Feature Area
Issues
Hello all,
I am trying to apply this documentation 
When I apply the documentation the resault is;
However in the documentation;
So what I missing?
Guidelines
 I have read the above statement and can confirm my post is relevant to the GitHub feature areas Issues and/or Projects.

Image-derived question evidence:
- [img-c86d018e3c84c0c5] tracking issue: test #2

Open

aecceyhan opened this issue 22 minutes ago · 0 comments

Write
Preview

```[tasklist]
### Tasks
- [ ] Draft task
```

Attach files by dragging & dropping, selecting or pasting them.

Cancel
Update comment
A dark-themed issue page is shown. The issue title appears at the top, followed by a green Open status indicator and issue metadata. Below, a comment editor is open with Write selected and Preview beside it. The editor contains a fenced task-list block with a Tasks heading and one unchecked Draft task item. A formatting toolbar is visible above the editor. At the bottom are attachment instructions and Cancel and Update comment buttons.
- [img-43a70c14f5ed04a5] tracking issue: test #2

Open
aecceyhan opened this issue 20 minutes ago · 0 comments

aecceyhan commented 20 minutes ago · edited

### Tasks
– [ ] Draft task
Dark-themed issue page. The title appears at the top, followed by a green Open status badge and issue metadata. A comment card by aecceyhan contains a dark text block with a Tasks heading and one unchecked task item. A circular avatar is visible to the left of the comment card, and a small circular icon appears below the text block.
- [img-0fcfd8288a8fd7d4] Adding draft tasks

Draft tasks are text items that are added to your tasklist. Draft tasks appear in your tasklist with a checkbox. You can use draft tasks to quickly sketch out the requirements and subtasks for your project and, optionally, later convert them into issues.

1  If the text field is not already focused, click Add item to Tasks.

[Embedded image]
octocat commented 2 weeks ago • edited
Tasks
Beta
Give feedback
No tasks being tracked yet.
Add item to Tasks
Add tasklist
A dark-themed document page is shown. At the top is the large heading “Adding draft tasks” followed by a chain/link icon and a horizontal divider. Below is a paragraph explaining draft tasks. A numbered instruction, “1”, appears next, followed by the sentence about clicking “Add item to Tasks.”

An embedded screenshot below shows a white comment/card interface. The top bar contains an octocat avatar, the text “octocat commented 2 weeks ago • edited,” a dropdown arrow, and an ellipsis menu. Inside the card is a Tasks section with a green task icon, a “Beta” badge, “Give feedback,” and an ellipsis menu. The card states “No tasks being tracked yet.” Below that is a bordered input/control labeled “Add item to Tasks” with a plus sign. At the bottom are an “Add tasklist” button with a plus sign and a circular smiley-face button.
````

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

````text
You are encountering two separate issues:

1. The newer task-list interface shown in the documentation was in private beta, so it was not available to every account.
2. If you use the older Markdown task-list format, put the first task on the line immediately after the heading:

```markdown
### Tasks
- [ ] #243
- [ ] #242
- [ ] Draft task
```

Thus, what is missing is access to the private-beta interface, or—when using the legacy format—the required line break between the heading and the first task. Where supported, the legacy Markdown syntax remains an alternative. The current **About tasklists** documentation also says tasklist blocks have been retired and identifies sub-issues as their replacement; a sub-issue can be created from an issue with **Create sub-issue**.
````

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Adding sub-issues](../documents/D021-b29136fb4de3.md)  
   Document ID: `github-docs::/issues/tracking-your-work-with-issues/using-issues/adding-sub-issues`
   Recorded heading(s): Creating a sub-issue

2. [About tasklists](../documents/D017-b3731f26535a.md)  
   Document ID: `github-docs::/get-started/writing-on-github/working-with-advanced-formatting/about-tasklists`
   Recorded heading(s): About tasklists

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
Two things:
Taskslists as shown in your screenshot are in private beta, please see the note at the top of the page: 
You can still use the previous tasklists, but your formatting is wrong. There should be a line break between the heading and the task
### Tasks
- [ ] #243
- [ ] #242
- [ ] Draft task
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-40-github-docs-64750.md) | [Next case](case-42-github-docs-88452.md)
