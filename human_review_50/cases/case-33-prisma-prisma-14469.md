<a id="case-33"></a>

# Case 33

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-32-github-docs-147941.md) | [Next case](case-34-prisma-prisma-3163.md)

**Dataset:** Prisma  
**Question ID:** `prisma::prisma-14469`  
**Distinct linked documents:** 2  
**Original discussion:** [Source](https://github.com/prisma/prisma/discussions/14469)  
**Accepted answer:** [Source answer](https://github.com/prisma/prisma/discussions/14469#discussioncomment-3215434)

**Reviewer:** __________  **Date:** __________

### Question

```text
Creating two one-to-many relationship between two tables

I need to make this one-to-many relationship between two tables, but there is two relations between the table referring to the same field. So this is my model. As you can see, I have both departure_station_id and return_station_id in Journey model. How can I now create a relationship between those fields with the Station model referring to the station_id field?
model Station {
 id Int @id @default(autoincrement())
 name String
 address String
 city String
 operator String
 capacity Int
 lon Float
 lat Float
}
model Journey {
 departure_time DateTime
 return_time DateTime
 departure_station String
 departure_station_id Int
 return_station String
 return_station_id Int
 duration Float
 covered_distance Float
 month String
 id Int @id @default(autoincrement())
}
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

````text
Define two explicitly named relations, because both foreign keys on `Journey` reference the same `Station` model. In the schema shown, the referenced `Station` field is `id`—there is no `station_id` field.

```prisma
model Station {
  id       Int    @id @default(autoincrement())
  name     String
  address  String
  city     String
  operator String
  capacity Int
  lon      Float
  lat      Float

  departureJourneys Journey[] @relation("DepartureStation")
  returnJourneys    Journey[] @relation("ReturnStation")
}

model Journey {
  departure_time     DateTime
  return_time        DateTime
  departure_station  String
  departure_station_id Int
  return_station     String
  return_station_id  Int
  duration           Float
  covered_distance   Float
  month              String
  id                 Int      @id @default(autoincrement())

  departureStation Station @relation("DepartureStation", fields: [departure_station_id], references: [id])
  returnStation    Station @relation("ReturnStation", fields: [return_station_id], references: [id])
}
```

`departure_station_id` and `return_station_id` are the foreign-key fields on the many side. Each relation points to `Station.id`; the two relation names keep Prisma from confusing the departure and return relationships. If the actual database column is named `station_id`, map it separately as needed, but the Prisma reference shown here remains `references: [id]` unless the `Station` model is changed to define a different key field.
````

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Relational data modeling](../documents/D046-b0aa728832d7.md)  
   Document ID: `prisma::/docs/orm/data-modeling/relational-databases`
   Recorded heading(s): One-to-many; How relations are declared

2. [What is introspection?](../documents/D064-bdabae0f67b9.md)  
   Document ID: `prisma::/docs/orm/v7/prisma-schema/introspection`
   Recorded heading(s): Disambiguating relations

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
Hey, I found the answer in the documentation. Please check this.
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-32-github-docs-147941.md) | [Next case](case-34-prisma-prisma-3163.md)
