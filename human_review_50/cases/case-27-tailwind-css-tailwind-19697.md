<a id="case-27"></a>

# Case 27

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-26-supabase-supabase-4133.md) | [Next case](case-28-github-docs-24740.md)

**Dataset:** Tailwind CSS  
**Question ID:** `tailwind-css::tailwind-19697`  
**Distinct linked documents:** 1  
**Original discussion:** [Source](https://github.com/tailwindlabs/tailwindcss/discussions/19697)  
**Accepted answer:** [Source answer](https://github.com/tailwindlabs/tailwindcss/discussions/19697#discussioncomment-15850861)

**Reviewer:** __________  **Date:** __________

### Question

```text
How do replace @apply when it comes to spacing?

I've begun updating my project from TW 3 to TW 4.
The most annoying thing is the inability to use @apply inside vue style components without adding @reference "tailwindcss" everywhere.
So with the push to not use @apply I started updating those css rules (which I need because I'm overriding a few 3rd party components which I cannot update the HTML for) to using CSS Variables.
It's easy for @apply text-red-500 I can do color: var(--color-red-500). But how do I deal with spacing such as w-xx or pt-XX?
Is my only solution to do width: calc(var(--spacing) * 60)?! It feels like I should instead be able to do width: var(--width-60) no?
Thanks!
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

````text
Use Tailwind’s build-time `--spacing()` function for spacing-based utilities. For example:

```css
.third-party-component {
  width: --spacing(60);
  padding-top: --spacing(4);
}
```

Replace `60` and `4` with the numeric values corresponding to your `w-XX` and `pt-XX` utilities. Tailwind v4 expands these to a calculation based on the theme’s `--spacing` variable—for example, `--spacing(4)` becomes `calc(var(--spacing) * 4)`.

The spacing scale is intentionally generated from the shared `--spacing` variable, so the corresponding representation is `--spacing(60)`, not a width-specific variable such as `var(--width-60)`. You can place these declarations in selectors targeting the third-party components, so the HTML does not need to change.

If you continue using `@apply` or `@variant` inside a Vue `<style>` block, Tailwind’s documented approach is still to add `@reference` for your main stylesheet (or directly reference `tailwindcss` when using only the default theme).
````

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Functions and directives](../documents/D079-0d439f9c59d6.md)  
   Document ID: `tailwind-css::/docs/functions-and-directives`
   Recorded heading(s): Functions; Directives

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
You can use the --spacing() helper function:
.my-element {
 width: --spacing(60);
}
V4 changed how some of these utilities work, opting to have an infinite spacing scale rather than set values. Thus, in this new system, var(--spacing) is multiplied to give the equivalents of the spacing values in v3.
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-26-supabase-supabase-4133.md) | [Next case](case-28-github-docs-24740.md)
