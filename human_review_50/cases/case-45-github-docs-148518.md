<a id="case-45"></a>

# Case 45

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-44-github-docs-55027.md) | [Next case](case-46-prisma-prisma-13456.md)

**Dataset:** GitHub Docs  
**Question ID:** `github-docs::148518`  
**Distinct linked documents:** 3  
**Original discussion:** [Source](https://github.com/orgs/community/discussions/148518)  
**Accepted answer:** [Source answer](https://github.com/orgs/community/discussions/148518#discussioncomment-15738167)

**Reviewer:** __________  **Date:** __________

### Question

```text
Is it intended that 2 mutations (markNotificationAsDone, unsubscribeFromNotifications) stopped showing up around Dec 2024?
Select Topic Area
Bug
I noticed that as of sometime within the last month or two, two mutations markNotificationAsDone and unsubscribeFromNotifications don't seem to show up in GraphQL API introspection and when using the GraphQL Explorer:
This happens despite them being documented, e.g., and I checked and there are only mentions about these mutations being added (1, 2) but no other relevant changes happening.
It's not a particular problem for me, I just wanted to report this in case it's not intended that they've disappeared without notice. Thanks.

Image-derived question evidence:
- [img-69d8e63fa1e2f053] GraphiQL

Cannot query field "markNotificationAsDone" on type "Mutation".

1  mutation {
2    markNotificationAsDone(input:{}) {
3      success
4    }
5  }

{
  "path": [
    "mutation",
    "markNotificationAsDone"
  ],
  "extensions": {
    "code": "undefinedField",
    "typeName": "Mutation",
    "fieldName": "markNotificationAsDone"
  },
  "locations": [
    {
      "line": 2,
      "column": 3
    }
  ],
  "message": "Field 'markNotificationAsDone'\ndoesn't exist on type 'Mutation'"
}
]
}

Variables
Headers
A GraphiQL interface is shown. The left editor contains a five-line mutation query, with markNotificationAsDone underlined in red. A dark notification banner overlays the upper center and displays an error message. The right pane shows a JSON-like error response, with the upper portion partly obscured by the notification banner. A vertical toolbar with icons is visible along the far left, and controls/icons are visible between the query editor and response pane. The bottom-left area contains the labels Variables and Headers.
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

```text
Yes. The accepted answer indicates that both `markNotificationAsDone` and `unsubscribeFromNotifications` were removed from the GraphQL schema and are no longer documented. Their absence from introspection and GraphQL Explorer therefore reflects the schema removal, not an Explorer-specific problem. The answer points to the GraphQL changelog’s schema-changes entry for January 14, 2025, as well as the GraphQL mutation reference, although the supplied local changelog excerpt does not itself contain the removal details.
```

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Changelog](../documents/D019-f61366cb5bbe.md)  
   Document ID: `github-docs::/graphql/overview/changelog`
   Recorded heading(s): Changelog

2. [Reference](../documents/D020-e79e302d47ee.md)  
   Document ID: `github-docs::/graphql/reference`
   Recorded heading(s): Reference

3. [Using the GraphQL API for Discussions](../documents/D018-08cb1713422b.md)  
   Document ID: `github-docs::/graphql/guides/using-the-graphql-api-for-discussions`
   Recorded heading(s): Mutations

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
By now, they both show up as removed under and they're no longer documented at
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-44-github-docs-55027.md) | [Next case](case-46-prisma-prisma-13456.md)
