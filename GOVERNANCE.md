# SINA NEXUS — Governance

## Purpose and authority

SINA NEXUS is the research and innovation division of SINA AI STUDIO. It investigates technologies and develops isolated prototypes. The SINA project owner retains final authority over priorities, external commitments, publication of confidential information, and integration into production products.

## Scope boundaries

- NEXUS owns research records, benchmarks, prototypes, and technical recommendations created in this repository.
- The canonical production platform remains `sina6565/AI_Studio_AI`.
- The separate SINA Pool Network initiative is a distinct product/repository and must not be conflated with NEXUS.
- Research work must not silently modify production systems or remove existing product capabilities.

## Approval requirements

Explicit project-owner approval is required before:
- Spending money, activating a paid subscription, using paid cloud/GPU resources, or accepting a paid trial that can convert to billing.
- Publishing confidential project information or unreleased product plans.
- Sending external messages or making commitments on behalf of SINA.
- Connecting research prototypes to production credentials, databases, deployments, or customer data.
- Transferring or integrating code, models, assets, datasets, or services into a SINA production product.
- Changing repository visibility or granting external collaborators access.

## Research and evidence standards

Every substantial research item must distinguish:
- Verified facts and measured results.
- Vendor or project claims not independently tested.
- Assumptions and hypotheses.
- Unknowns and blocked checks.

Use official documentation and terms for access, pricing, geography, privacy, and licensing. Preserve source URLs and the date checked. If a material point cannot be verified, mark it **Unknown — written confirmation required**.

## Security and privacy

- Never commit API keys, tokens, passwords, private certificates, production connection strings, or personal data.
- Use synthetic or public test data unless explicit approval and safeguards exist.
- Keep prototype secrets separate from production secrets.
- Do not send confidential SINA material to third-party services without explicit approval and a documented data-handling review.
- Report suspected secret exposure immediately; rotate affected credentials rather than merely deleting the visible text.

## Intellectual property and third-party material

For every external dependency, model, dataset, plugin, asset, or code sample, record its origin, version, license/terms, attribution obligations, redistribution rights, and commercial-use restrictions.

A public repository, free account, open-weight model, or successful download does not automatically grant unrestricted commercial rights. When terms are ambiguous, do not integrate the material until clarified.

## Branch and pull request policy

- `main` is the stable documentation and approved research baseline.
- Use one focused branch per workstream or task; avoid mixing unrelated experiments.
- Branch names use the conventions in `WORKSTREAMS.md`.
- Keep pull requests small, descriptive, and linked to a research question or issue.
- Include test/evaluation evidence, known limitations, license notes, and cost implications.
- Do not merge experimental code into `main) until it has been reviewed and its purpose is documented.
- Do not force-push shared branches or rewrite history without explicit approval.

## Decision records

Material decisions must be recorded under `decisions/` with:
- Context and question.
- Options considered.
- Evidence and sources.
- Risks and unresolved issues.
- Decision: Adopt / Prototype Further / Monitor / Reject.
- Approver and date.
- Revisit trigger, if applicable.

## External collaboration

Contributors receive only the access necessary for their assigned work. They may not represent research findings as product commitments or make legal, financial, licensing, or partnership commitments for SINA.

## Incident handling

If a prototype exposes a secret, violates a license, mishandles data, or creates an unexpected charge:
1. Stop the affected experiment.
2. Preserve relevant logs without copying secrets into issues.
3. Notify the project owner.
4. Revoke/rotate credentials or disable the resource as appropriate.
5. Document the incident and corrective action.
