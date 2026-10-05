<a id="case-06"></a>

# Case 06

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-05-prisma-prisma-28901.md) | [Next case](case-07-prisma-prisma-5982.md)

**Dataset:** GitHub Docs  
**Question ID:** `github-docs::23381`  
**Distinct linked documents:** 1  
**Original discussion:** [Source](https://github.com/orgs/community/discussions/23381)  
**Accepted answer:** [Source answer](https://github.com/orgs/community/discussions/23381#discussioncomment-3240167)

**Reviewer:** __________  **Date:** __________

### Question

```text
Verifying github.io domains for orginizations
I want to verify my org domain, which is default pages domain, user.github.io, but how do I verify the name on GitHub? Will github support creating a txt file on the repo? And is it okay to make this public?
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

```text
For organization identity verification, click the **Verified** label on the organization’s profile to open GitHub’s information about the process. The documented verification flow is:

1. Open the organization’s **Settings**.
2. In **Security**, select **Verified and approved domains**.
3. Click **Add a domain** and enter the domain.
4. GitHub provides instructions for adding a **DNS TXT record** through the domain’s hosting/DNS provider.
5. After DNS propagation—possibly up to 72 hours—return to the pending domain and choose **Continue verifying**, then **Verify**.

This requires access to modify the domain’s DNS records. The TXT record is a DNS record, not a `.txt` file stored in a repository, so creating one in the repo is not the documented method. The documentation also says the DNS TXT entry may optionally be deleted after the Verified badge appears.

The supplied documentation does not establish that the default `user.github.io` Pages hostname can be verified this way, nor does it require making a repository public. If you mean a custom domain used by GitHub Pages, the documentation says custom Pages domains can be verified; use the DNS-based process above. The question of repository visibility is therefore not applicable to the documented verification method.
```

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Verifying or approving a domain for your organization](../documents/D023-e0558135c957.md)  
   Document ID: `github-docs::/organizations/managing-organization-settings/verifying-or-approving-a-domain-for-your-organization`
   Recorded heading(s): Verifying a domain for your organization; About domain verification

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
Sorry, I though by org you meant the profile website for an organization on GitHub.
If you click on the Verified label you find a link for more info on how it works:
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-05-prisma-prisma-28901.md) | [Next case](case-07-prisma-prisma-5982.md)
