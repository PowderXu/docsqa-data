<a id="case-37"></a>

# Case 37

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-36-github-docs-23427.md) | [Next case](case-38-prisma-prisma-5405.md)

**Dataset:** GitHub Docs  
**Question ID:** `github-docs::22539`  
**Distinct linked documents:** 2  
**Original discussion:** [Source](https://github.com/orgs/community/discussions/22539)  
**Accepted answer:** [Source answer](https://github.com/orgs/community/discussions/22539#discussioncomment-3237250)

**Reviewer:** __________  **Date:** __________

### Question

```text
Login not possible in Eclipse
Hey there,
I want to import a project from an existing git repostitory in Eclipse via URI. The Problem is that my git password and user are not accepted. I double checked username and password multiple times but nothing happens.
Anyone an idea why this happens?
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

```text
The problem is likely that GitHub no longer accepts an account password for Git operations over HTTPS. In Eclipse/EGit, when the import asks for a password, enter a GitHub personal access token (PAT) instead of your normal GitHub password.

To resolve it:
1. In GitHub, open **Settings → Developer settings → Personal access tokens → Fine-grained tokens → Generate new token**.
2. Select the appropriate resource owner and grant the token access to the repository you are importing. Choose only the permissions needed for the operation.
3. Copy the token when it is generated; it will not be available to view again.
4. Retry the Eclipse import using the repository’s HTTPS URI. Supply your GitHub username when requested, and paste the PAT into the password field.

If Eclipse keeps retrying the old credentials, remove the saved GitHub credential from the credential storage used by Eclipse/Git, then retry so that it prompts for the PAT again. The supplied documentation specifically recommends using a credential helper or cached credentials for repeated HTTPS operations; it does not establish the exact Eclipse credential-storage steps, so those depend on the Eclipse/EGit setup.
```

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Managing your personal access tokens](../documents/D010-f9c27f15bc10.md)  
   Document ID: `github-docs::/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens`
   Recorded heading(s): Creating a fine-grained personal access token

2. [Why is Git always asking for my credentials?](../documents/D014-7416520c7b45.md)  
   Document ID: `github-docs::/get-started/git-basics/why-is-git-always-asking-for-my-credentials`
   Recorded heading(s): Why is Git always asking for my credentials?

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
You can’t use your password for Git operations, as described in the documentation. You need to create a PAT and provide that when asked for your password. Your PAT should have the repo and (if you use Actions) workflow scopes.
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-36-github-docs-23427.md) | [Next case](case-38-prisma-prisma-5405.md)
