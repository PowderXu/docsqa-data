<a id="case-31"></a>

# Case 31

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-30-prisma-prisma-14086.md) | [Next case](case-32-github-docs-147941.md)

**Dataset:** Prisma  
**Question ID:** `prisma::prisma-27294`  
**Distinct linked documents:** 2  
**Original discussion:** [Source](https://github.com/prisma/prisma/discussions/27294)  
**Accepted answer:** [Source answer](https://github.com/prisma/prisma/discussions/27294#discussioncomment-13409100)

**Reviewer:** __________  **Date:** __________

### Question

```text
Do I need special copy rules for the query engine DLL when specifying a client generation output path in src/ ?

Question
I'm trying the new prisma client generator (prisma-client instead of prisma-client-js) and am also specifying the output dir for the first time. My config is similar to the example in the documentation for the new generator.
generator client {
 provider = "prisma-client"
 output = "../src/db/prisma"
 moduleFormat = "esm"
}
When I build my app with tsc, I notice that query_engine-windows.dll.node is not copied to the build output directory ./build/db/prisma. Then, when I deliver the built app to a new directory or host, the DLL is not copied. When delivered to a directory on the same host, I was surprised to find the application loaded the DLL from the original source directory. For example, in this procmon screenshot, you can see the built application is in D:\Webroot and the original source directory is within C:\Jenkins.
This is a problem when the delivered app is running and I try to delete/change the source directory. Is the expectation that I write a custom build step to copy that DLL? If I were to run npx prisma generate in the directory where the app is intended to run, it would create TypeScript source in ./src/db/prisma which I don't want alongside my built application in ./build.
How to reproduce (optional)
No response
Expected behavior (optional)
I expected the DLL in node_modules\@prisma\engines\query_engine-windows.dll.node would be used instead of the DLL in the original source directory.
Information about Prisma Schema, Client Queries and Environment (optional)
OS: Windows 11
Database: PostgreSQL
Node.js version: 20
> npx prisma -v
Environment variables loaded from .env
Prisma schema loaded from prisma\schema.prisma
prisma : 6.8.2
@prisma/client : 6.8.2
Computed binaryTarget : windows
Operating System : win32
Architecture : x64
Node.js : v20.19.2
TypeScript : 5.8.3
Query Engine (Node-API) : libquery-engine 2060c79ba17c6bb9f5823312b6f6b7f4a845738e (at node_modules\@prisma\engines\query_engine-windows.dll.node)
Schema Engine : schema-engine-cli 2060c79ba17c6bb9f5823312b6f6b7f4a845738e (at node_modules\@prisma\engines\schema-engine-windows.exe)
Schema Wasm : @prisma/prisma-schema-wasm 6.8.0-43.2060c79ba17c6bb9f5823312b6f6b7f4a845738e
Default Engines Hash : 2060c79ba17c6bb9f5823312b6f6b7f4a845738e
Studio : 0.511.0

Image-derived question evidence:
- [img-a8ca29cec1df1d4f] Event Properties

Event | Process | Stack

Image
Node.js JavaScript Runtime
Node.js

Name: node.exe
Version: 20.19.2
Path: C:\Program Files\nodejs\node.exe
Command Line: node.exe "C:\Program Files\nodejs\interceptor.js" "D:\Webroot\[black redacted region]\app.cjs"

PID: 7812
Parent PID: 716
Session ID: 0
User: [black redacted region]
Auth ID: [black redacted region]
Started: 5/30/2025 6:58:42 AM

Architecture: 64-bit
Virtualized: False
Integrity: High
Ended: (Running)

Modules:
Module | Address | Size | Path | Company | Version | Times...
node.exe | 0x7f6aed70000 | 0x4682000 | C:\Program Files\nodejs\node.exe | Node.js | 20.19.2 | 5/14/...
query_engine-win... | 0x7f858910000 | 0x13ec000 | C:\Jenkins\workspace\[black redacted region]\src\db\prisma\query_engine-windows.dll.node
cryptnet.dll | 0x7f8789f0000 | 0x31000 | C:\WINDOWS\SYSTEM32\cryptnet.dll | Microsoft Corpor... | 10.0.20348.1 (...) | 10/2/...
[partially visible module row ending in “.dll”]

Next Highlighted
Copy All
Close
A Windows-style “Event Properties” window is open. The “Process” tab is selected, with “Event” and “Stack” tabs beside it. The upper section identifies a Node.js JavaScript Runtime process and shows process metadata, including a command line, PID, architecture, virtualization state, integrity, start time, and running status. The User and Auth ID values are covered by black rectangles. A Modules table occupies the lower portion of the window; one row is highlighted in blue. Some table columns and row contents are clipped horizontally or vertically. Navigation arrow buttons, a “Next Highlighted” checkbox, “Copy All” button, and “Close” button are visible at the bottom.
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

```text
Yes. With the `prisma-client` generator output under `src/`, TypeScript compilation does not automatically copy the native query-engine DLL into the corresponding `build` directory. Add a custom build step that copies `query_engine-windows.dll.node` into the generated Prisma client directory in the build artifact—for example, alongside `build/db/prisma`—and include that file in deployment.

The process loaded the DLL from `C:\Jenkins\...\src\db\prisma`, as shown by the module path, because the generated client was still resolving the engine from the source-side generated-client location. Consequently, the delivered application can continue to work on the same host while unintentionally depending on the original source tree; it should instead receive its own copied DLL with the build.

You do not need to run `prisma generate` in the deployment directory. Generate the client during the normal build, compile the TypeScript, copy the required DLL as part of packaging, and deploy the resulting build directory. The accepted guidance notes that this native-DLL copying requirement is expected to go away when using the WASM/Query Compiler approach, because the WASM modules are imported from the shared `@prisma/client` package rather than copied separately.
```

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Database polyfills](../documents/D061-1bbd03bcf4c9.md)  
   Document ID: `prisma::/docs/orm/v7/prisma-client/setup-and-configuration/database-polyfills`
   Recorded heading(s): Database polyfills

2. [No Rust engine](../documents/D052-6154cdc2153f.md)  
   Document ID: `prisma::/docs/orm/v6/prisma-client/setup-and-configuration/no-rust-engine`
   Recorded heading(s): No Rust engine

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
I just checked with the team internally. Currently, you would need to write a custom build step to copy over the DLL file.
This pain point goes away with WASM (since we import the WASM modules from the shared @prisma/client package and not copy them anywhere), so it’s not going to be a problem anymore with QueryCompiler.
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-30-prisma-prisma-14086.md) | [Next case](case-32-github-docs-147941.md)
