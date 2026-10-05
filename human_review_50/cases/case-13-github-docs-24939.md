<a id="case-13"></a>

# Case 13

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-12-prisma-prisma-20554.md) | [Next case](case-14-supabase-supabase-34352.md)

**Dataset:** GitHub Docs  
**Question ID:** `github-docs::24939`  
**Distinct linked documents:** 1  
**Original discussion:** [Source](https://github.com/orgs/community/discussions/24939)  
**Accepted answer:** [Source answer](https://github.com/orgs/community/discussions/24939#discussioncomment-3245934)

**Reviewer:** __________  **Date:** __________

### Question

```text
Public GitHub Package couldn't found via GitHub Actions in the same Organisation
Hi,
I recently started using GitHub Packages. The GitHub repositories are publicly accessible and should therefore be easy to use. Unfortunately, these are not found, for example in the IDE I am using, IntelliJ, but also not found in GitHub Actions.
GitHub Package: Package dev.minecode.core.api · MineCodeDEV/Core · GitHub
pom.xml: Coins/pom.xml at d40fe0d1297ebd93b6e22748e7e151aad2aa9596 · MineCodeDEV/Coins · GitHub
Does anyone know why the dependency can’t be found?
Regards
Jerome
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

```text
The package being public does not make its Maven artifacts anonymously downloadable. GitHub Packages requires authentication to install public packages, so Maven in IntelliJ and the GitHub Actions runner will fail to resolve the dependency if no GitHub Packages credentials are configured.

Configure the consuming Maven project with the GitHub Packages Maven repository and authenticate using a personal access token (classic) with the `read:packages` scope. In Maven, the repository’s `<id>` must match the `<id>` of the credential entry in `~/.m2/settings.xml`. The package dependency must also use the exact published `groupId`, `artifactId`, and `version`; enable snapshots if the referenced version is a `SNAPSHOT`.

For GitHub Actions, provide the same kind of token to Maven—typically a personal access token (classic) with `read:packages`—and write it to the runner’s Maven settings before running the build. `GITHUB_TOKEN` is supported when the workflow repository is associated with the package and has been granted package read access.

Thus, being in the same organization and having public repositories is not by itself sufficient; the missing GitHub Packages authentication is the issue indicated by the package and `pom.xml` setup. The supplied references do not show enough of the POM to identify any additional coordinate or repository-URL error.
```

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Working with the Apache Maven registry](../documents/D025-2857bdac83ff.md)  
   Document ID: `github-docs::/packages/working-with-a-github-packages-registry/working-with-the-apache-maven-registry`
   Recorded heading(s): Authenticating to GitHub Packages; Installing a package

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
Unfortunately even public Maven packages still require authentication for download. The “Authenticating to GitHub Packages” section in this document explains how to do that:
 docs.github.com
Configuring Apache Maven for use with GitHub Packages - GitHub Docs
//docs.github.com/en/packages/guides/configuring-apache-maven-for-use-with-github-packages
AFAIK that applies to GitHub packages in general, only GHCR allows downloads of public images without any authentication.
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-12-prisma-prisma-20554.md) | [Next case](case-14-supabase-supabase-34352.md)
