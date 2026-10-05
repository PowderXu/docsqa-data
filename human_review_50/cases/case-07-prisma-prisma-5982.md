<a id="case-07"></a>

# Case 07

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-06-github-docs-23381.md) | [Next case](case-08-prisma-prisma-15898.md)

**Dataset:** Prisma  
**Question ID:** `prisma::prisma-5982`  
**Distinct linked documents:** 1  
**Original discussion:** [Source](https://github.com/prisma/prisma/discussions/5982)  
**Accepted answer:** [Source answer](https://github.com/prisma/prisma/discussions/5982#discussioncomment-431972)

**Reviewer:** __________  **Date:** __________

### Question

```text
Prisma VSCode extension doesn't auto-complete. Not sure what I'm doing wrong.

I'm working on a project with nextJS and prisma and trying to understand what I perceive to be inconsistent behavior from the official VSCode extension. In the generated prisma directory, I created a PrismaClient and then export it. Inside that file, all the VSCode auto-completion/suggestion works. However, when I import the client into my graphql API, the auto-completion/suggestion stops working. I did this because according to the documentation on "Instantiating the Client" you should only create one prisma instance.
If I'm missing something extremely obvious, I apologize. I just can't figure out why the extension isn't working as I expect.
If it matters, I'm using
macOS 10.15.7 Catalina
VSCode 1.53.2
prisma extension v2.18.1
Thanks for any help you can offer!
Examples:
/prisma
|_ prisma.js
/pages
|_ /api
 |_ graphql.js
// /prisma/prisma.js
import { PrismaClient } from '@prisma/client'
const prisma = new PrismaClient()
export default prisma
As opposed to
// /pages/api/graphql.js
// other imports for apollo server...
import prisma from '../../prisma/prisma'
const resolvers = {
 Query: {
 users: (_, args, { prisma } ) => {
 // prisma is added via ApolloServer context
 // however auto-complete/suggest doesn't work here
 }
 }
}

Image-derived question evidence:
- [img-3d2564cc5dc92289] sma > prisma.js > ...

1  import { PrismaClient } from '@prisma/client'
2
3  const prisma = new PrismaClient()
4
5  prisma.
6
7  export

$disconne...    (method) PrismaClient<Prism...
$executeRaw
$on
$queryRaw
$transaction
$use
sequence
technique
techniquesOnSequences
user
PrismaClient
A dark-themed code editor is shown with a JavaScript file named "prisma.js". The editor displays import and PrismaClient initialization code. On line 5, "prisma." has been typed, with an autocomplete suggestion panel open below it. The first suggestion is highlighted. A partial "export" is visible on line 7 behind the suggestion panel. The top-left breadcrumb is cropped and begins with "sma >", followed by "prisma.js > ...".
- [img-610afc882fa7ded0] 24    [partial pink code text visible near the top, appears to include `})`]
25
26    prisma.
27
28    // crea[partially obscured]
29    const e[partially obscured]
30    retur[partially obscured]
31    cur[partially obscured]
32    nod[partially obscured]
33    }
34    })

Autocomplete suggestions:
ApolloServer
COOKIE_KEY
Cookies
Cors
Date
Error
Mutation
Object
Query
VERCEL_ENV

[partially visible tab text]MINAL
PROBLEMS
2
[partially visible text]C
/Projects/martia[partially visible]
A dark-themed code editor is shown with line numbers 24 through 34 visible. On line 26, `prisma.` is typed and has a red wavy underline. An autocomplete popup overlays the right side of the editor, listing identifier suggestions in order: ApolloServer, COOKIE_KEY, Cookies, Cors, Date, Error, Mutation, Object, Query, and VERCEL_ENV. The lower panel shows a partially clipped terminal tab, a PROBLEMS tab with a yellow count of 2, and a partially visible orange-highlighted path beginning `/Projects/martia`.
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

````text
The issue is the resolver context, not that you created a single shared `PrismaClient`. In JavaScript, VS Code does not know the type of the `context`/`ctx` object passed to the resolver, so it cannot infer that `ctx.prisma` is a `PrismaClient` and therefore cannot provide Prisma suggestions.

Add a JSDoc typedef for the generated `PrismaClient` type and annotate the resolver's context parameter. Following the documented procedure:

```js
/**
 * @typedef { import("../prisma/generated/client").PrismaClient } Prisma
 */

const resolvers = {
  Query: {
    /**
     * @param {any} parent
     * @param {any} args
     * @param {{ prisma: Prisma }} ctx
     */
    users: (parent, args, ctx) => {
      return ctx.prisma.user.findMany()
    },
  },
}
```

Use the import path that points to your generated Prisma client in your project. The important parts are the `@typedef` importing `PrismaClient` and the context annotation declaring that `ctx.prisma` has type `Prisma`. After that, suggestions such as `ctx.prisma.user.findMany()` should be available in the resolver.
````

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [GraphQL autocompletion](../documents/D056-86f950bab509.md)  
   Document ID: `prisma::/docs/orm/v7/more/troubleshooting/graphql-autocompletion`
   Recorded heading(s): GraphQL autocompletion; Solution; Complete example; Problem

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
@aberkow 👋
As you're using JavaScript, you would need to follow this guide to make autocomplete work in the resolver's context.
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-06-github-docs-23381.md) | [Next case](case-08-prisma-prisma-15898.md)
