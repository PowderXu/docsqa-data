<a id="case-26"></a>

# Case 26

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-25-github-docs-166151.md) | [Next case](case-27-tailwind-css-tailwind-19697.md)

**Dataset:** Supabase  
**Question ID:** `supabase::supabase-4133`  
**Distinct linked documents:** 1  
**Original discussion:** [Source](https://github.com/orgs/supabase/discussions/4133)  
**Accepted answer:** [Source answer](https://github.com/orgs/supabase/discussions/4133#discussioncomment-1720436)

**Reviewer:** __________  **Date:** __________

### Question

```text
storage.remove not removing item

Per the documentation found here:
I'm currently calling:
const { data, error } = await supabase
.storage
.from('avatars')
.remove(['folder/avatar1.png'])
with the correct bucket and file path for my app. This seems to be successful, returning:
{ "data": [], "error": null }
but when I visit the supabase website the file is still there. I imagine this is due to the lack of a policy. Is there documentation on policies somewhere that provides more examples than the few templates available?
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

````text
You are probably missing a `DELETE` policy. The `remove` operation requires a policy that allows deletion; without one, the request may return no deleted items, as indicated by `data: []`.

In the Supabase dashboard, open **Storage → Policies**, select the `avatars` bucket, create a policy, choose the **DELETE** operation, and provide a SQL condition matching the files the user may delete.

For example, the accepted policy pattern is:

```sql
((bucket_id = 'test-bucket'::text)
 AND (storage.extension(name) = 'png'::text)
 AND (lower((storage.foldername(name))[1]) = 'test-folder'::text))
```

Adapt the bucket, extension, and folder values to your case—for example, the `avatars` bucket and the `folder` path component. Do not use the example unchanged unless those values actually match your storage objects.

For additional policy examples, use the **Storage** documentation's access-control material (the section historically titled “Allow individual access to a file”) and the dashboard's **View templates** option when creating a policy. Storage policies control operations such as `SELECT`, `INSERT`, `UPDATE`, and `DELETE`, so make sure `DELETE` is selected rather than only a read or upload operation.
````

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Storage](../documents/D075-a9c1d1ac6843.md)  
   Document ID: `supabase::/docs/guides/storage`
   Recorded heading(s): Key features

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
You are probably missing the policy for DELETE. Here's an example SQL expression for DELETE policy that works:
((bucket_id = 'test-bucket'::text) AND (storage.extension(name) = 'png'::text) AND (lower((storage.foldername(name))[1]) = 'test-folder'::text))
You can go to Storage > Policies to create policies for your bucket,
For this case you need to use DELETE for allowed operations and provide the above SQL expression:
Depending on who you want to allow to access, here are more examples:
```

#### Existing image-derived text attached to the accepted answer

Evidence ID: `img-bb63136ebaf5c2a7`

```text
Storage policies
Safeguard your files with policies that define the operations allowed for your users at the bucket level.

test-bucket
New policy

Give anon users access to PNG images in folder zfkm11_0    SELECT
Give anon users access to PNG images in folder zfkm11_1    INSERT
Give anon users access to PNG images in folder zfkm11_2    UPDATE
Give anon users access to PNG images in folder zfkm11_3    DELETE

4 policies in test-bucket
A dark-themed interface displays a "Storage policies" page. Beneath the heading is explanatory text. A bordered panel for the bucket "test-bucket" contains a "New policy" button and four policy rows. Each row has a description on the left and a green operation label near the center: SELECT, INSERT, UPDATE, and DELETE. The panel footer states "4 policies in test-bucket".
```

Evidence ID: `img-d349339e9dbced01`

```text
Adding new policy to $test-bucket

Policy name
A descriptive name for your policy.
0/50

Allowed operations
Based on the operations you have selected,
you can use any of the highlighted functions
in the supabase-js Javascript library

SELECT
INSERT
UPDATE
DELETE

copyObject
createObject
deleteObject
deleteObjects
getObject
getSignedObject
getSignedUrl
listObjects
moveObjects
updateObject

Policy definition
Provide a SQL conditional expression that
returns a boolean.

1

View templates
Review
A dark modal dialog is open. The heading reads “Adding new policy to $test-bucket”. A blank Policy name input appears at the top right with a visible “0/50” counter. The Allowed operations section shows four unchecked-looking boxes labeled SELECT, INSERT, UPDATE, and DELETE. Below them are function labels arranged in rows; most are dimmed, while “getSignedObject” is highlighted in green. The Policy definition section contains a large dark code editor with line number “1” and no visible code. At the bottom right are buttons labeled “View templates” and “Review”. A close X icon is visible in the upper-right corner.
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-25-github-docs-166151.md) | [Next case](case-27-tailwind-css-tailwind-19697.md)
