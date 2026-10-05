<a id="case-29"></a>

# Case 29

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-28-github-docs-24740.md) | [Next case](case-30-prisma-prisma-14086.md)

**Dataset:** Tailwind CSS  
**Question ID:** `tailwind-css::tailwind-13967`  
**Distinct linked documents:** 1  
**Original discussion:** [Source](https://github.com/tailwindlabs/tailwindcss/discussions/13967)  
**Accepted answer:** [Source answer](https://github.com/tailwindlabs/tailwindcss/discussions/13967#discussioncomment-9989299)

**Reviewer:** __________  **Date:** __________

### Question

```text
How to add more variants other than dark?

Hi need some help.
In my app I have multiple themes: dark, light, foo, bar
I want to apply styles like
// does not work 
<div className="rounded-md foo:rounded-lg" />
// works
<div className="rounded-md dark:rounded-lg" />
is this possible?
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

````text
Yes—Tailwind can support additional theme prefixes such as `foo:` and `bar:` by registering `foo` and `bar` as custom variants in a Tailwind plugin. After registration, the intended markup is conceptually:

```jsx
<div className="rounded-md foo:rounded-lg" />
<div className="rounded-md bar:rounded-lg" />
```

Each custom variant must be associated with however that theme is activated in your app—for example, the selector or state used for the `foo` and `bar` themes. The supplied information does not include a version-specific plugin API or those activation selectors, so this is the supported approach rather than verified executable configuration. To provide the exact setup, the Tailwind version and the way each theme is activated are needed.
````

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Adding custom styles](../documents/D077-4b6db9902f3a.md)  
   Document ID: `tailwind-css::/docs/adding-custom-styles`
   Recorded heading(s): Using variants

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
Yes! Consider registering some custom variants in a Tailwind plugin.
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-28-github-docs-24740.md) | [Next case](case-30-prisma-prisma-14086.md)
