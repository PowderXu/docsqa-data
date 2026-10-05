<a id="case-17"></a>

# Case 17

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-16-github-docs-5033.md) | [Next case](case-18-prisma-prisma-29524.md)

**Dataset:** Tailwind CSS  
**Question ID:** `tailwind-css::tailwind-20353`  
**Distinct linked documents:** 1  
**Original discussion:** [Source](https://github.com/tailwindlabs/tailwindcss/discussions/20353)  
**Accepted answer:** [Source answer](https://github.com/tailwindlabs/tailwindcss/discussions/20353#discussioncomment-17789418)

**Reviewer:** __________  **Date:** __________

### Question

```text
What is the official v4 way to do the v3 max-w-screen-*

Hello,
in Tailwind v3 to set max width of element to some breakpoint value, you would use max-w-screen-* 
For example max-w-screen-lg for max width of 1024px.
And I wonder what is the recommended way to achieve the same results in v4.
Currently I use: max-w-(--breakpoint-lg) which achieves the same thing.
But I am not sure if this is considered workaround because it uses CSS variable and if there is any more "official" way to do it.
I was thinking for example direct class like max-w-breakpoint-lg which would be similar to the old max-w-screen-lg but I cant find anything like that.
So what is the current correct way to do this?
Thanks.
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

```text
In Tailwind CSS v4, use `max-w-(--breakpoint-lg)`—this is the intended, documented approach, not a workaround. The `--breakpoint-*` values are theme variables, and the `max-w-(...)` syntax pulls a theme variable into a utility.

There is no corresponding built-in `max-w-breakpoint-lg` utility in v4. Also note that bare `max-w-screen` means `max-width: 100vw`; it is not the breakpoint-specific equivalent of the old `max-w-screen-lg`. If you define theme variables that reference other variables, use the `inline` option with `@theme` as documented in the “Referencing other variables” section.
```

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Theme variables](../documents/D080-c511d8fc5c84.md)  
   Document ID: `tailwind-css::/docs/theme`
   Recorded heading(s): Referencing other variables; Default theme variable reference

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
max-w-(--breakpoint-lg) is not a workaround, it's intended
--breakpoint-* are theme variables emitted to :root, and max-w-(--some-var) is the documented syntax for pulling a theme variable into a utility (no built-in max-w-breakpoint-* class in v4)
The @theme snippet from wongjn works
also the docs recommend @theme inline when a theme variable references another variable, and bare max-w-screen already exists in v4 meaning max-width: 100vw
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-16-github-docs-5033.md) | [Next case](case-18-prisma-prisma-29524.md)
