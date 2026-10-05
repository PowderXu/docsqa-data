<a id="case-25"></a>

# Case 25

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-24-prisma-prisma-9691.md) | [Next case](case-26-supabase-supabase-4133.md)

**Dataset:** GitHub Docs  
**Question ID:** `github-docs::166151`  
**Distinct linked documents:** 7  
**Original discussion:** [Source](https://github.com/orgs/community/discussions/166151)  
**Accepted answer:** [Source answer](https://github.com/orgs/community/discussions/166151#discussioncomment-13764050)

**Reviewer:** __________  **Date:** __________

### Question

```text
Security Logs
Hi,
Can someone help with the following questions please
Which logs in GitHub are related to security? (Eg: Audit logs, security logs, action logs etc.)
Apart from audit logs can any other logs be streamed directly or via third-party apps to the S3 bucket? If yes, please share the documentation or steps for it.
Are there any log schemas available?
Thanks.
```

### Reference answer to review

Judge the normalized benchmark answer below. The original community answer is retained at the end for provenance, not as a second item to score.

```text
The GitHub logs and event sources relevant to security are:

- **Audit logs**: organization, enterprise, and repository audit activity, including changes to settings and access, membership changes, app permissions, and related activity. Enterprise audit-log streaming also includes Git events. [github-docs::/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise#about-audit-log-streaming]
- **User security logs**: account-level events such as logins and logouts, failed authentication, password or SSH-key changes, two-factor-authentication events, and OAuth-token grants or revocations. The security-log reference groups events by category and operation type. [accepted_answer] [github-docs::/authentication/keeping-your-account-and-data-secure/security-log-events#document-overview] [github-docs::/authentication/keeping-your-account-and-data-secure/security-log-events#about-security-log-events]
- **Security alerts**: Dependabot, code-scanning/CodeQL, and secret-scanning events are security-relevant events. They can be forwarded through applicable webhooks. [accepted_answer]
- **Webhooks and API activity**: webhooks can notify a server about selected repository, organization, or enterprise events and can be used as an alternative to audit-log searching or API polling for some use cases. [github-docs::/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise#document-overview] [github-docs::/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/audit-log-events-for-your-organization#document-overview]

The supplied material does not identify “Actions logs” as a separate security-log category. Treat Actions-related activity as relevant only where it appears in the applicable audit events or is exposed through an appropriate webhook or integration.

**Streaming to Amazon S3**

1. **Audit logs** can be streamed directly to Amazon S3 using GitHub’s enterprise audit-log-streaming procedure. The stream exports compressed JSON files, with filenames in the form `YYYY/MM/HH/MM/<uuid>.json.gz`. The procedure supports configuring Amazon S3 as a destination and also lists Datadog, Splunk, Google Cloud Storage, Azure Blob Storage, and Azure Event Hubs as provider options. [github-docs::/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise#setting-up-audit-log-streaming] [github-docs::/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise#about-audit-log-streaming]
2. **Other event sources** can be sent to S3 indirectly through webhooks: subscribe to the required repository, organization, or enterprise events, receive the webhook at an API Gateway or other endpoint, and use a service such as Lambda to write the payload to S3. This is an integration pattern rather than the documented audit-log stream. [accepted_answer] [github-docs::/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise#document-overview]
3. **Third-party integrations** such as Splunk, Datadog, and Sumo Logic may collect GitHub audit logs and, in some cases, security-alert events, then forward them to S3 or retain them in their own storage. The exact availability depends on the integration and event type. [accepted_answer]

For a webhook-based design, configure the webhook for the desired event types, receive it through an API Gateway, reverse proxy, or application, validate the webhook signature using a secret token, and then write the validated payload to S3. GitHub’s documentation specifically recommends validating the cryptographic hash included with signed webhook payloads before processing them. [github-docs::/webhooks/using-webhooks/delivering-webhooks-to-private-systems#securing-traffic-to-your-reverse-proxy] [github-docs::/webhooks/using-webhooks/delivering-webhooks-to-private-systems#validating-webhook-payloads]

**Available schemas and event references**

- **Organization and enterprise audit-log event references** define events using a `category.operation` form, such as `repo.create`, and document the event fields and categories. [github-docs::/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/audit-log-events-for-your-organization#about-audit-log-events-for-your-organization] [accepted_answer]
- **User security-log event reference** lists the categories and operations that can appear in a user’s security log. [github-docs::/authentication/keeping-your-account-and-data-secure/security-log-events#about-security-log-events] [accepted_answer]
- **Webhook payload schemas** are documented per webhook event type in the Webhooks reference; security-alert payloads are one example. [accepted_answer]

The applicable local documents are **Streaming the audit log for your enterprise**, **Audit log events for your organization**, **Security log events**, and the **Webhooks** documentation.
```

### Provided documentation

Judge the pages listed here **together**. Open the full local pages; titles or matching keywords alone do not establish coverage.

1. [Streaming the audit log for your enterprise](../documents/D009-e5fce18ad07b.md)  
   Document ID: `github-docs::/admin/monitoring-activity-in-your-enterprise/reviewing-audit-logs-for-your-enterprise/streaming-the-audit-log-for-your-enterprise`
   Recorded heading(s): Streaming the audit log for your enterprise; About audit log streaming; Setting up audit log streaming

2. [Reviewing your security log](../documents/D011-43d840c54fbc.md)  
   Document ID: `github-docs::/authentication/keeping-your-account-and-data-secure/reviewing-your-security-log`

3. [Security log events](../documents/D012-92eeba5bdca3.md)  
   Document ID: `github-docs::/authentication/keeping-your-account-and-data-secure/security-log-events`
   Recorded heading(s): Security log events; About security log events

4. [Audit log events for your organization](../documents/D022-d725eb87262e.md)  
   Document ID: `github-docs::/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/audit-log-events-for-your-organization`
   Recorded heading(s): About audit log events for your organization

5. [Using the GitHub CLI to forward webhooks for testing](../documents/D041-3715d8da2458.md)  
   Document ID: `github-docs::/webhooks/testing-and-troubleshooting-webhooks/using-the-github-cli-to-forward-webhooks-for-testing`

6. [Automatically redelivering failed deliveries for a GitHub App webhook](../documents/D042-4bd7437ade86.md)  
   Document ID: `github-docs::/webhooks/using-webhooks/automatically-redelivering-failed-deliveries-for-a-github-app-webhook`

7. [Delivering webhooks to private systems](../documents/D043-f9c833c6b3f0.md)  
   Document ID: `github-docs::/webhooks/using-webhooks/delivering-webhooks-to-private-systems`
   Recorded heading(s): Securing traffic to your reverse proxy; Validating webhook payloads

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
Security-related logs in GitHub
Audit logs (organization, enterprise, repository) record who changed settings, permissions, memberships, OAuth app grants, and more.
GitHub Docs
GitHub Docs
Security logs (user security log) record login and logout events, failed authentication attempts, password or SSH key changes, 2FA events, and OAuth token grants or revocations.
GitHub Docs
Code Security Alerts include Dependabot (dependency alerts), Code Scanning (CodeQL/SAST results), and Secret Scanning events.
GitHub Docs
Webhooks and API logs capture any webhook delivery failures or API access events via Webhooks or the Audit Log API.
GitHub Docs
Streaming logs beyond the Audit Log
Audit Log to S3: GitHub Enterprise Cloud and Server can stream audit log data to Amazon S3 using AWS access keys or OpenID Connect. See “Streaming the audit log for your enterprise” for step-by-step setup.
GitHub
GitHub Docs
Webhooks to S3 (or any endpoint): You can subscribe to specific events, such as push, pull request, and security alert, via organization or repository Webhooks and forward payloads through an AWS API Gateway and Lambda that writes to S3. Docs: Webhooks.
GitHub Docs
Third-party integrations like Splunk, Datadog, and Sumo Logic all have GitHub connectors to pull Audit Logs and, in some cases, security alerts to push them to S3 or their own storage.
Available log schemas
Audit Log Events Schema is detailed in “Audit log events for your organization” and lists every {category}.{action} along with field definitions.
GitHub Docs
Security Log Events Schema is documented in “Security log events,” which groups all user-level events by category and operation type.
GitHub Docs
Webhooks Payload Schema: Each webhook type has its own JSON schema in the Webhooks docs, such as the Security Alert webhook.
Useful Links
Review Security Log: 
Audit Log Streaming to S3: 
Audit Log Events List: 
Security Log Events List: 
Webhooks Reference: 
sorry if i made any sapling mistake :)
( If it helped you even a bit, could you please accept it as the answer? I'm trying to get the Galaxy Brain achievement. Thank you! )
```

</details>

[Summary](../README.md#case-index) | [Instructions](../INSTRUCTIONS.md) | [Previous case](case-24-prisma-prisma-9691.md) | [Next case](case-26-supabase-supabase-4133.md)
