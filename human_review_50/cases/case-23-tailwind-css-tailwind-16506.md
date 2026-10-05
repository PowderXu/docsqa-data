<a id="case-23"></a>

# Case 23

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-22-github-docs-26686.md) | [Next case](case-24-prisma-prisma-9691.md)

**Dataset:** Tailwind CSS  
**Question ID:** `tailwind-css::tailwind-16506`  
**Distinct linked documents:** 1  
**Original discussion:** [Source](https://github.com/tailwindlabs/tailwindcss/discussions/16506)  
**Accepted answer:** [Source answer](https://github.com/tailwindlabs/tailwindcss/discussions/16506#discussioncomment-12189055)

**Reviewer:** __________  **Date:** __________

### Question

```text
Hover property doesn't work on mobile device in chrome browser

So i was trying to make button with hover property
In desktop, the hover work normally as i wish
but in mobile or more specifically in chrome browser, the hover won't work
In mobile device, hover only not working on chrome browser but working normally when using other browser
the below one is a part of my codes
<li class="py-2 px-2 mx-2 rounded-lg border w-fit h-fit flex justify-center border-sky-500 hover:border-sky-800 hover:bg-slate-800 hover:text-gray-500 transition-all duration-150">
 <i class="fa-solid fa-house"></i>
 </li>
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

````text
If you are using Tailwind CSS v4, this is expected behavior rather than a problem with the classes. Tailwind now generates `hover` styles only when the primary input device supports hovering, effectively placing rules such as these inside `@media (hover: hover)`. A touch screen does not have a true hover state, so Chrome on the device may not apply those classes even if another mobile browser appears to do so.

For a touch-friendly solution, do not make the button depend on `hover`; treat the hover appearance as an enhancement and provide the intended action through tapping. If you specifically need the old behavior where tapping can trigger `:hover`, override Tailwind’s variant in your CSS:

```css
@custom-variant hover (&:hover);
```

Place this in the CSS where your Tailwind configuration/custom variants are defined. This restores the old `hover` variant implementation, although relying on hover for touch interaction can result in sticky or inconsistent states.
````

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Upgrade guide](../documents/D081-d5d21c07ea46.md)  
   Document ID: `tailwind-css::/docs/upgrade-guide`
   Recorded heading(s): Hover styles on mobile

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
Hey! In Tailwind CSS v4 hover styles only apply on devices that actually support hover to avoid sticky hover states:
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-22-github-docs-26686.md) | [Next case](case-24-prisma-prisma-9691.md)
