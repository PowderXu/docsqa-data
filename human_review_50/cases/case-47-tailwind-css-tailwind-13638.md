<a id="case-47"></a>

# Case 47

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-46-prisma-prisma-13456.md) | [Next case](case-48-github-docs-167845.md)

**Dataset:** Tailwind CSS  
**Question ID:** `tailwind-css::tailwind-13638`  
**Distinct linked documents:** 2  
**Original discussion:** [Source](https://github.com/tailwindlabs/tailwindcss/discussions/13638)  
**Accepted answer:** [Source answer](https://github.com/tailwindlabs/tailwindcss/discussions/13638#discussioncomment-9317258)

**Reviewer:** __________  **Date:** __________

### Question

```text
tailwind intellisense not detecting duplicate utilities when plugin added

In an effort to get variable font weights working, i created a custom plugin exactly as shown here. however tailwinds intellisense still detects the core utilities of the same name...
and the runtime build still seems to compile with the original utilities but just being overridden. Im not entirely sure of the implications of this, but the duplicate intellisense has be concerned there'll inevitably be some weirdness tied to some kind of weird race conditions between my font plugin and the core system. Why aren't my utilities of the same name just outright replacing the core ones?
For context, the environment is a brand new scaffolded remix app, textbook tailwind integration with the custom plugin applied via the link above.
EDIT: just did a quick build to check if this persists into the production css, it does.

Image-derived question evidence:
- [img-29fffab8fa586951] You, 12 minutes ago  1 author (You)
import type { MetaFunction } from "@remix-run/node";

export const meta: MetaFunction = () => {
  return [{ title: "[obscured]", content: "Welcome to Remix!" }]
};

export default functi[obscured]
  return ([obscured]
    <div className="b[obscured]
      <h1 className="font-bold">Welcome to Remix!</h1>
      <ul>
        <li>
          <a target="_blank" href="`https://remix.run/tutorials/blog"` rel="noreferrer">
            15m Quickstart Blog Tutorial
          </a>
        </li>
[partially visible code below]

.font-bold {
  font-weight: 700;
  font-variation-settings: "wght" 700;
}

.font-bold {
  font-weight: 700;
}
A dark-themed code editor is visible with syntax-highlighted TypeScript/JSX code. A dark inspection popup overlays the center-upper portion of the code and shows two `.font-bold` CSS rule blocks. A red hand-drawn bracket/mark appears along the popup's left edge. A yellow marker icon is visible in the left gutter beside the `export default` line. The lower portion of the code continues below the bottom edge of the image.
- [img-b22c3710d88faa43] .font-bold {
    font-weight: 700
}

.uppercase {
    text-transform: uppercase
}

.lowercase {
    text-transform: lowercase
}

.filter {
    filter: var(--tw-blur) var(--tw-brightnes[unreadable/cropped]
}

.font-bold {
    font-weight: 700;
    font-variation-settings: "wght" 700
}
A vertical image displays CSS-style code on a light background. Four code blocks appear in the upper portion, followed by a second `.font-bold` block in the lower portion. Red bracket-like marks are visible along the left side of the first and last `.font-bold` blocks. The `.filter` line extends to the right edge and is cut off.
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

````text
Your plugin is adding another implementation of the utility; it is not disabling Tailwind’s built-in `fontWeight` core plugin. Therefore IntelliSense still offers the core classes, and Tailwind still emits the core rules in the generated CSS. The duplicate `.font-bold` rules shown in the build are expected from that configuration.

For Tailwind v3, disable the core plugin in `tailwind.config.js` so only your plugin’s implementation is generated:

```js
/** @type {import('tailwindcss').Config} */
module.exports = {
  corePlugins: {
    fontWeight: false,
  },
}
```

This is not a runtime race condition. Both rules are static CSS rules with the same selector; the cascade and generated stylesheet order determine which declaration wins. Disabling `fontWeight` removes the ambiguity and also prevents IntelliSense from treating the built-in utilities as available.

If this is Tailwind v4, note that the v3 `corePlugins` option is no longer supported. In v4, custom utilities use the `@utility` API instead, so the v3 configuration above should not be applied there.
````

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Theme variables](../documents/D080-c511d8fc5c84.md)  
   Document ID: `tailwind-css::/docs/theme`

2. [Upgrade guide](../documents/D081-d5d21c07ea46.md)  
   Document ID: `tailwind-css::/docs/upgrade-guide`
   Recorded heading(s): Disabling core plugins; Adding custom utilities

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
You coul disable the core fontWeight plugin so that only the CSS from the plugin is built:
/** @type {import('tailwindcss').Config} */
module.exports = {
 corePlugins: {
 fontWeight: false,
 }
}
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-46-prisma-prisma-13456.md) | [Next case](case-48-github-docs-167845.md)
