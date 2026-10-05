<a id="case-21"></a>

# Case 21

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-20-prisma-prisma-11775.md) | [Next case](case-22-github-docs-26686.md)

**Dataset:** GitHub Docs  
**Question ID:** `github-docs::166561`  
**Distinct linked documents:** 1  
**Original discussion:** [Source](https://github.com/orgs/community/discussions/166561)  
**Accepted answer:** [Source answer](https://github.com/orgs/community/discussions/166561#discussioncomment-13796314)

**Reviewer:** __________  **Date:** __________

### Question

```text
How to fix this error when adding a custom domain to GitHub Pages?
Select Topic Area
Question
How do I fix this error when adding a custom domain to my GitHub repo sunflowerthomas/website-redesign?
I have attached a picture of my DNS configuration below if that helps any bit.

Image-derived question evidence:
- [img-11f85517fa4d70e0] sunflowertomas.xyz is improperly configured
Domain does not resolve to the GitHub Pages server. For more information, see
documentation (NotServedByPagesError).
Check again
A pale yellow warning banner spans the image. On the left is an outlined warning icon containing an exclamation mark. The banner contains three lines of text, with “documentation” shown in blue, and a “Check again” button on the right.
- [img-ee70771c15f42cf4] Type | Name | Content | Proxy status | TTL | Actions
CAA | www | 0 issue letsencrypt.org | DNS only | Auto | Edit
CNAME | www | sunflowerthomas.github.io | Proxied | Auto | Edit
MX | sunflowerthomas.xyz | eforward3.registrar-serve... | 10 | DNS only | Auto | Edit
MX | sunflowerthomas.xyz | eforward2.registrar-serve... | 10 | DNS only | Auto | Edit
MX | sunflowerthomas.xyz | eforward1.registrar-serve... | 10 | DNS only | Auto | Edit
MX | sunflowerthomas.xyz | eforward4.registrar-serve... | 15 | DNS only | Auto | Edit
MX | sunflowerthomas.xyz | eforward5.registrar-serve... | 20 | DNS only | Auto | Edit
NS | sunflowerthomas.xyz | dns2.registrar-servers.com | DNS only | Auto | Edit
NS | sunflowerthomas.xyz | dns1.registrar-servers.com | DNS only | Auto | Edit
TXT | _github-pages-challen... | "[redacted]" | DNS only | Auto | Edit
TXT | sunflowerthomas.xyz | "v=spf1 include:spf.efwd.reg... | DNS only | Auto | Edit
A DNS-record table is visible with columns for Type, Name, Content, Proxy status, TTL, and Actions. Each row has a checkbox on the left and an Edit control on the right. The first row is highlighted light blue. The CNAME row shows an orange cloud icon and the status Proxied. The other visible rows show DNS only. A small blue icon appears beside the CNAME type. The TXT content in the _github-pages-challen... row is covered by a black redaction.
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

```text
The error indicates that the domain is not resolving to GitHub Pages. Also verify the spelling: the screenshot shows `sunflowertomas.xyz`, while the repository owner and accepted configuration use `sunflowerthomas.xyz`. These are different domains.

For the intended domain `sunflowerthomas.xyz`:

1. In your DNS provider, add four `A` records for the apex/root domain:
   - Name: `@`
   - Content: `185.199.108.153`
   - Content: `185.199.109.153`
   - Content: `185.199.110.153`
   - Content: `185.199.111.153`
   Set these records to DNS-only if your provider offers proxying.

2. Change the `www` CNAME from **Proxied** to **DNS only** (gray cloud). Keep it pointing to `sunflowerthomas.github.io`.

3. In `sunflowerthomas/website-redesign`, open **Settings > Pages** and set the custom domain to `www.sunflowerthomas.xyz` (or use the apex domain if that is the address you want as primary), then save it.

4. After DNS updates propagate, select **Check again** in GitHub Pages. Enable **Enforce HTTPS** once GitHub has verified the domain.

The apex domain uses `A` records, while the `www` subdomain uses a `CNAME`; GitHub Pages supports configuring both so they can redirect between the apex and `www` domain.
```

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [About custom domains and GitHub Pages](../documents/D026-d982d56deb25.md)  
   Document ID: `github-docs::/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages`
   Recorded heading(s): Using an apex domain for your GitHub Pages site; Using a subdomain for your GitHub Pages site

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
Your custom domain setup is almost correct, but here’s what you need to fix:
🔧 1. Point your root domain (sunflowerthomas.xyz) to GitHub Pages
You need to add A records for @ in your DNS provider (e.g. Cloudflare):
Type: A
Name: @
Content:
 185.199.108.153
 185.199.109.153
 185.199.110.153
 185.199.111.153
Proxy status: DNS only (no orange cloud)
These are the official GitHub Pages IPs:
👉 
🟠 2. Disable Cloudflare Proxy for the www subdomain
Your CNAME www is currently proxied (orange cloud), which can prevent GitHub from verifying it.
Go to your DNS settings.
Find the CNAME for www.
Click the orange cloud to make it gray: DNS only
⚙️ 3. Set your domain in GitHub Pages settings
In your repo (sunflowerthomas/website-redesign):
Go to Settings > Pages
In the custom domain field, enter:
www.sunflowerthomas.xyz or sunflowerthomas.xyz
Click Save
Then enable Enforce HTTPS
🔁 (Optional) Redirect root domain to www
If you want sunflowerthomas.xyz to redirect to www.sunflowerthomas.xyz, keep the A records above and use www.sunflowerthomas.xyz as the primary domain in GitHub.
✅ Final checklist:
 A records added for root domain @
 Cloudflare Proxy disabled (DNS only) for CNAME
 Domain added in GitHub Pages settings
 HTTPS enforced (optional)
After these changes, wait a few minutes and hit “Check again” in the GitHub Pages settings.
Let me know if it still doesn’t work!
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-20-prisma-prisma-11775.md) | [Next case](case-22-github-docs-26686.md)
