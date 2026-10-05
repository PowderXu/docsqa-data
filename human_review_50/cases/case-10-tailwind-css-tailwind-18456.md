<a id="case-10"></a>

# Case 10

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-09-github-docs-25309.md) | [Next case](case-11-github-docs-120943.md)

**Dataset:** Tailwind CSS  
**Question ID:** `tailwind-css::tailwind-18456`  
**Distinct linked documents:** 1  
**Original discussion:** [Source](https://github.com/tailwindlabs/tailwindcss/discussions/18456)  
**Accepted answer:** [Source answer](https://github.com/tailwindlabs/tailwindcss/discussions/18456#discussioncomment-13670919)

**Reviewer:** __________  **Date:** __________

### Question

```text
Not able to apply dynamic value to className on the basis of condition

What version of Tailwind CSS are you using?
v4.01.10
What build tool (or framework if it abstracts the build tool) are you using?
Vite 6.3.5
What version of Node.js are you using?
For example: v22.16.0
What browser are you using?
Chrome
What operating system are you using?
Windows
Code
export interface UserAvatarProps {
 src: string | null | undefined;
 firstName: string;
 lastName: string | null | undefined;
 className?: string;
 showOnOff?: boolean;
 isOnline?: boolean;
 size?: number;
 contentSize?: string;
 borderSize?: number;
 background?: string;
 content?: string;
}
const UserAvatar = (props: UserAvatarProps) => {
 const {
 src,
 firstName,
 lastName,
 size = 10,
 contentSize = "sm",
 background = "bg-accent",
 content = "text-accent-content",
 borderSize,
 className,
 showOnOff,
 isOnline,
 } = props;
 return (
 <div
 className={`avatar avatar-placeholder ${
 showOnOff ? (isOnline ? "avatar-online" : "avatar-offline") : ""
 } ${className ? className : ""}`}
 >
 <div
 className={`overflow-hidden rounded-full size-${size} ${
 borderSize ? `border-${borderSize}` : ""
 } ${background} ${content}`}
 >
 {src ? (
 <img src={src} alt={`Avatar ${firstName} ${lastName}`} />
 ) : (
 <span className={`text-${contentSize}`}>
 {firstName[0]}
 {lastName && lastName[0]}
 </span>
 )}
 </div>
 </div>
 );
};
export default UserAvatar;
Describe your issue
Not assigning the size-32 and border-2 class if the size value change to 32 and border value to 2 and also not showing class even when inspect.
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

````text
Tailwind does not reliably generate utilities whose names are constructed with interpolation, such as `size-${size}` and `border-${borderSize}`. Map each supported prop value to a complete class name that appears literally in the source.

```tsx
const sizeClasses: Record<number, string> = {
  10: "size-10",
  32: "size-32",
};

const borderClasses: Record<number, string> = {
  1: "border-1",
  2: "border-2",
};

const UserAvatar = (props: UserAvatarProps) => {
  const {
    src,
    firstName,
    lastName,
    size = 10,
    contentSize = "sm",
    background = "bg-accent",
    content = "text-accent-content",
    borderSize,
    className,
    showOnOff,
    isOnline,
  } = props;

  const sizeClass = sizeClasses[size] ?? sizeClasses[10];
  const borderClass = borderSize ? borderClasses[borderSize] ?? "" : "";

  return (
    <div
      className={`avatar avatar-placeholder ${
        showOnOff ? (isOnline ? "avatar-online" : "avatar-offline") : ""
      } ${className ?? ""}`}
    >
      <div
        className={`overflow-hidden rounded-full ${sizeClass} ${borderClass} ${background} ${content}`}
      >
        {src ? (
          <img src={src} alt={`Avatar ${firstName} ${lastName}`} />
        ) : (
          <span className={`text-${contentSize}`}>
            {firstName[0]}
            {lastName && lastName[0]}
          </span>
        )}
      </div>
    </div>
  );
};
```

With `size={32}` and `borderSize={2}`, the inner `<div>` receives `size-32 border-2`. Those complete class names are statically detectable, so Tailwind can generate their CSS. The original interpolation may still produce the text `size-32` at runtime, but Tailwind scans source text rather than evaluating JavaScript, so it cannot infer all possible resulting class names. Also inspect the inner `<div>`: that is where the size and border classes are assigned in the supplied component.
````

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Detecting classes in source files](../documents/D078-e1e9acd23847.md)  
   Document ID: `tailwind-css::/docs/detecting-classes-in-source-files`
   Recorded heading(s): Dynamic class names; How classes are detected

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
As per the documentation:
Since Tailwind scans your source files as plain text, it has no way of understanding string concatenation or interpolation in the programming language you're using.
❌ Don't construct class names dynamically
<div class="text-{{ error ? 'red' : 'green' }}-600"></div>
In the example above, the strings text-red-600 and text-green-600 do not exist, so Tailwind will not generate those classes.
Instead, make sure any class names you’re using exist in full:
✅ Always use complete class names
<div class="{{ error ? 'text-red-600' : 'text-green-600' }}"></div>
If you're using a component library like React or Vue, this means you shouldn't use props to dynamically construct classes:
❌ Don't use props to build class names dynamically
function Button({ color, children }) {
 return <button className={`bg-${color}-600 hover:bg-${color}-500 ...`}>{children}</button>;
}
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-09-github-docs-25309.md) | [Next case](case-11-github-docs-120943.md)
