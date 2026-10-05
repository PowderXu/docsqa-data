<a id="case-22"></a>

# Case 22

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-21-github-docs-166561.md) | [Next case](case-23-tailwind-css-tailwind-16506.md)

**Dataset:** GitHub Docs  
**Question ID:** `github-docs::26686`  
**Distinct linked documents:** 3  
**Original discussion:** [Source](https://github.com/orgs/community/discussions/26686)  
**Accepted answer:** [Source answer](https://github.com/orgs/community/discussions/26686#discussioncomment-3396593)

**Reviewer:** __________  **Date:** __________

### Question

```text
How to get just the tag name?
I trigger my workflow using
on:
 push:
 tags:
and I just want the name of the current tag that is just building.
Sadly, the github context variable’s ref has this value:
"ref": "refs/tags/0.3.1"
However, I only want the last part, 0.3.1.
There exists no function in GitHub Actions that allows me to extract that.
Am I overlooking something? How do I get that?
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

````text
Use the short ref name instead of `github.ref`:

```yaml
on:
  push:
    tags:
      - '*'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Print tag name
        run: |
          echo "Tag name: $GITHUB_REF_NAME"
          echo "Tag name: ${{ github.ref_name }}"
```

For a tag ref of `refs/tags/0.3.1`, both forms produce `0.3.1`. `github.ref_name` and `GITHUB_REF_NAME` are the short name of the branch or tag that triggered the workflow, while `github.ref` is the fully formed ref.
````

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Store information in variables](../documents/D003-1757879fe796.md)  
   Document ID: `github-docs::/actions/how-tos/write-workflows/choose-what-workflows-do/use-variables`
   Recorded heading(s): Using the `env` context to access environment variable values

2. [Contexts reference](../documents/D005-74153039e7b0.md)  
   Document ID: `github-docs::/actions/reference/workflows-and-actions/contexts`
   Recorded heading(s): `github` context

3. [Variables reference](../documents/D007-b49372994f6a.md)  
   Document ID: `github-docs::/actions/reference/workflows-and-actions/variables`
   Recorded heading(s): Default environment variables

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
Since this page shows up surprisingly high in Google search , here is the 2022 answer in "How to get a tag name in GitHub Actions"
on:
 push:
 tags:
 - '*'
jobs:
 github-example-tags:
 steps:
 - name: GitHub Tag Name example
 run: |
 echo "Tag name from GITHUB_REF_NAME: $GITHUB_REF_NAME"
 echo "Tag name from github.ref_name: ${{ github.ref_name }}"
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-21-github-docs-166561.md) | [Next case](case-23-tailwind-css-tailwind-16506.md)
