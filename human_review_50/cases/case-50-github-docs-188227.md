<a id="case-50"></a>

# Case 50

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-49-prisma-prisma-11953.md)

**Dataset:** GitHub Docs  
**Question ID:** `github-docs::188227`  
**Distinct linked documents:** 2  
**Original discussion:** [Source](https://github.com/orgs/community/discussions/188227)  
**Accepted answer:** [Source answer](https://github.com/orgs/community/discussions/188227#discussioncomment-15950948)

**Reviewer:** __________  **Date:** __________

### Question

```text
Most Elegant Way To Transfer Repositories From Personal Account To Organization
Select Topic Area
Question
Hello,
I currently have a couple of projects I'd like to move to my new organization. I think what I am looking for is confirmation on several potential pitfalls. One of which, I assume, is that the Packages (aka Docker Images from GHCR) won't be migrated. Is this still the expected behaviour or are the threads I've read stale?
Additionally, if I were to do such a thing and move the repositories, what would be the best way to go about it with minimal chaos. I want to plan this move first so that I don't run into more gotchas than a manageable amount. My projects are still early enough that a lot of users are not downloading said packages but let's say they are and they come looking, should I just have a new repository of the same name (after migration) that sends them to the one on the organization?
It's unclear and I don't want to jump into it without doing thorough research hence this thread. I also feel this is a huge security flaw and opens the door for potential (albeit a lot of hoops might be required to get there) repojacking or name hijacking since a lot can happen if you let go of a name. Again, the chances are low but not non-zero.
I have been reading the documentation as well as threads here and there. But perhaps, my question is,
what is the best way to most elegantly transfer a repository and if waiting would be better if this is about to become seamless at some point in the near future?
Cheers and thanks in advance.
Some notable references I've read:
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

```text
The GHCR package/image does **not automatically transfer with the repository**. Treat the repository move and package handling as separate, coordinated operations. A package can be migrated by unlinking it from the old repository and linking it to the new organization repository, but that repository-link operation is distinct from changing the package namespace or image reference.

A low-disruption plan is:

1. **Inventory dependencies first.** Identify workflows, deployment manifests, package permissions, pull secrets, webhooks, deploy keys, and any environment or organization-level configuration that refers to the old owner or image path. Private-package consumers are the ones most likely to require new credentials or permission changes; public consumers still need the new image path and a migration notice if the namespace changes.
2. **Verify transfer prerequisites.** You need administrator access to the repository and permission to create repositories in the target organization. The organization must not already contain a repository with the same name or a fork in the same network.
3. **Schedule the move.** From the repository's **Settings → Danger Zone → Transfer**, select the organization as the new owner and confirm the transfer. Issues, pull requests, wiki, stars, watchers, releases, projects, commit information, webhooks, services, secrets, and deploy keys remain with the repository as documented; Git LFS objects are also moved, although that can occur in the background. When moving from a personal account to an organization, issue assignments to people outside the organization are cleared.
4. **Reconnect the package.** After the repository transfer, unlink the package from the old repository and link it to the new organization repository. Check its visibility and access settings afterward, because unlinking can affect access when the package inherits permissions from its repository.
5. **Update consumers and publishing systems.** If the image reference changes from the personal namespace to the organization namespace, update GitHub Actions, deployment configuration, publishing workflows, and pull credentials as needed. Test publishing and pulling during the maintenance window, and notify users of the new repository and package locations.
6. **Update local Git remotes.** GitHub redirects clone, fetch, push, and Web links from the old repository location, but existing clones should be changed explicitly with `git remote set-url origin NEW_URL`.

Do not create a replacement or “tombstone” repository with the old name. Creating a repository or fork at the previous location permanently removes GitHub's redirects. Therefore, leave the old location unused after the transfer rather than using it to redirect users manually. GitHub may also permanently retire the old owner/name combination for repositories meeting its documented Marketplace or activity criteria, preventing that combination from being reused.

The supplied guidance does not establish that a seamless combined repository-and-package transfer is imminent. If the projects are ready, plan the move around the current separate repository and package steps instead of waiting for an assumed future feature.
```

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Connecting a repository to a package](../documents/D024-fdb5d127fe64.md)  
   Document ID: `github-docs::/packages/learn-github-packages/connecting-a-repository-to-a-package`
   Recorded heading(s): Unlinking a repository from a package on GitHub; Migrating a package to another repository

2. [Transferring a repository](../documents/D028-0e7916fb4725.md)  
   Document ID: `github-docs::/repositories/creating-and-managing-repositories/transferring-a-repository`
   Recorded heading(s): About repository transfers; Transferring a repository owned by your personal account; What's transferred with a repository?

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
Subject: Best Practices for Repository and GHCR Package Migration to Organizations
Hello,
Moving projects to a new organization is a common milestone, but you are correct to be cautious about the "connective tissue" like GitHub Packages (GHCR) and security implications. Based on current GitHub behavior and documentation, here is a detailed breakdown of how to handle this elegantly.
The "Package" Pitfall: GHCR Migration
You are correct: Packages (Docker images in GHCR) do not automatically move with the repository. When you transfer a repository, the GitHub Container Registry (GHCR) remains linked to the original namespace (your personal account) unless explicitly migrated. To move them:
Manual Migration: You must use the GitHub API or CLI to connect the package to the repository after the repo has moved.
Permissions: Ensure the Organization has "Write" access to the package. If the package is currently "Private," you will need to re-configure the pull secrets in your deployment environments (K8s, CI/CD, etc.) because the namespace in the image path will change from ghcr.io/old-username/repo to ghcr.io/new-org/repo.
Minimizing "Chaos" during Transfer
GitHub handles repository redirects very well, but there are manual steps to ensure a "zero-downtime" feel:
Git Remotes: GitHub will automatically redirect git clone and git push requests from the old URL to the new one. However, it is best practice for contributors to update their remotes manually: git remote set-url origin [new-url].
Action Secrets: Repository-level secrets move with the repo, but Environment secrets and Organization-level secrets do not. You must recreate any CI/CD secrets in the new Organization.
Pages: If you use GitHub Pages, the custom domain will transfer, but the underlying *.github.io URL will change immediately.
Addressing Security: Name Hijacking (Repojacking)
Your concern regarding "repojacking" is valid. When you transfer a repository, GitHub creates a redirect. However, if you or someone else creates a new repository with the old name in your personal account, that redirect is broken.
The Elegant Solution:
Instead of leaving a "tombstone" repository (a repo with a README pointing to the new one), rely on GitHub’s built-in redirect system. To prevent hijacking:
Perform the transfer.
Do not create any new repositories with the old name.
GitHub protects the namespace of a transferred repository as long as you don't manually interfere with it by creating a new repo of the same name.
Is "Seamless" Migration Coming?
Currently, GitHub focuses on repository integrity (stars, issues, PRs), while Packages are treated as separate entities tied to a namespace. There is no official "one-click" repo + package migration on the immediate public roadmap that would automate the renaming of Docker image manifests.
Recommended Action Plan:
Audit CI/CD: Update your GitHub Action workflows to reference the new ghcr.io/new-org/... paths.
Pre-Pull: If you have production services running, ensure they have the images cached or update their pull configs immediately after the move.
Transfer: Use the GitHub UI/Settings to transfer the repo.
Reconnect Packages: Go to the Package settings in your personal account and change the "Inherit access from repository" to the new repo location in the Org.
The most "elegant" way is to treat this as a scheduled maintenance window: Update the repo, reconnect the package, and update your image paths in one clean sweep.
Cheers!
source:
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-49-prisma-prisma-11953.md)
