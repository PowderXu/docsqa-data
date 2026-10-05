<a id="case-03"></a>

# Case 03

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-02-prisma-prisma-12782.md) | [Next case](case-04-prisma-prisma-13540.md)

**Dataset:** Tailwind CSS  
**Question ID:** `tailwind-css::tailwind-15809`  
**Distinct linked documents:** 2  
**Original discussion:** [Source](https://github.com/tailwindlabs/tailwindcss/discussions/15809)  
**Accepted answer:** [Source answer](https://github.com/tailwindlabs/tailwindcss/discussions/15809#discussioncomment-11944454)

**Reviewer:** __________  **Date:** __________

### Question

```text
Error while Migrate from TailwindCSS V3 to V4 using `npx @tailwindcss/upgrade`

i tried to upgrade from tailwindcss v3 to v4 using npx @tailwindcss/upgrade --force I got this error
PS C:\Users\name\Projects\portfolio> npx @tailwindcss/upgrade --force 
(node:50016) ExperimentalWarning: CommonJS module C:\Users\name\AppData\Roaming\npm\node_modules\npm\node_modules\debug\src\node.js is loading ES Module C:\Users\name\AppData\Roaming\npm\node_modules\npm\node_modules\supports-color\index.js using require().
Support for loading ES Module in require() is an experimental feature and might change at any time
(Use `node --trace-warnings ...` to show where the warning was created)
≈ tailwindcss v4.0.0
│ Searching for CSS files in the current directory and its subdirectories…
│ ↳ Linked `.\tailwind.config.ts` to `.\src\styles\globals.css` 
│ Migrating JavaScript configuration files…
│ ↳ Could not load the configuration file: `addUtilities({ ':root' : … })` defines an invalid utility selector. Utilities must be a single class name and start with a lowercase letter, eg. 
│ `.scrollbar-none`.
I saw many were having the same issue, especially on Windows #15220 if any anyone know a solution pls tell me
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

```text
The failure is caused by a plugin in `tailwind.config.ts`/`tailwind.config.js` that registers `:root` through `addUtilities(...)`. During the v3-to-v4 migration, remove the plugin entries from the config and run the upgrade again.

Then add the functionality back using the v4 CSS-based approach:

- If the `:root` block contains global/default styles, move it into your CSS file as ordinary CSS, optionally inside `@layer base`.
- If it is meant to be a reusable utility, give it a class-based name and migrate it to the v4 `@utility` directive. A utility must represent a class name; `:root` is a global selector, not a utility class.
- If the plugin itself is still needed, load the legacy plugin from CSS with the v4 `@plugin` directive, then migrate its custom utilities separately as needed.

The accepted resolution for this error is therefore: temporarily remove the plugins from the Tailwind config, complete the migration, and re-add them using the Tailwind v4 directives and CSS structure.
```

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Functions and directives](../documents/D079-0d439f9c59d6.md)  
   Document ID: `tailwind-css::/docs/functions-and-directives`
   Recorded heading(s): Directives; Compatibility

2. [Adding custom styles](../documents/D077-4b6db9902f3a.md)  
   Document ID: `tailwind-css::/docs/adding-custom-styles`
   Recorded heading(s): Using custom CSS; Simple utilities

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
Hello @codezeros
I had this same problem and i tried removing plugins from tailwindcss.config.ts or tailwindcss.config.js and it worked after removing them :) and you can add back based on the new tailwindcss v4 refer: and
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-02-prisma-prisma-12782.md) | [Next case](case-04-prisma-prisma-13540.md)
