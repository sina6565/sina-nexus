# SINA AI POOL NETWORK — Architecture Charter

**A shared capability and compute network connecting providers with requesters**

Status: Proposed architecture / research baseline  
Owner: SINA AI STUDIO project owner  
Target implementation repository: `sina6565/sina-pool-network`  
Research home: `sina6565/sina-nexus`

## 1. Vision

SINA AI POOL NETWORK is a unified network where independent providers can contribute capabilities or resources and requesters can discover and use them through one consistent SINA interface.

The network is more than a directory or simple marketplace. It is a coordinated pool with registration, validation, matching, scheduling, execution tracking, quality controls, usage metering, and transparent provider/requester policies.

## 2. Network participants

### Providers

Providers may contribute one or more of:
- GPU or CPU compute capacity.
- Hosted or locally operated AI model endpoints.
- Image, video, audio, speech, 3D, or game-generation capabilities.
- APIs, tools, plugins, and specialist agents.
- Storage or other explicitly supported infrastructure capabilities.

Providers control what they offer, availability, geographic/data constraints, capacity, usage limits, and any compensation terms they choose to publish.

### Requesters / Consumers

Requesters may be:
- SINA AI STUDIO users.
- Developers and application builders.
- Organizations and teams.
- Authorized agents acting within user-granted permissions.

A requester submits a job or capability request with required capability, input/output contract, quality target, latency expectation, region/data constraints, and budget or quota policy where applicable.

### SINA Pool Engine

SINA operates the coordination and trust layer:
- Provider and capability registry.
- Provider onboarding and validation.
- Health, availability, and capacity tracking.
- Capability discovery and matching.
- Scheduling, routing, retries, and fallback.
- Job state, result delivery, and provenance.
- Quality measurement and reputation.
- Usage metering, quota enforcement, and settlement records.
- Security policy, audit logs, and dispute workflows.

## 3. Initial capability pools

1. **Image Pool** — image generation, editing, and understanding.
2. **Video Pool** — video generation, editing, and analysis.
3. **Audio Pool** — speech, transcription, sound, and music capabilities.
4. **3D & Game Pool** — assets, characters, environments, animation, and game-building tools.
5. **Model Pool** — language, vision, multimodal, and specialist models.
6. **Agent & API Pool** — tools, APIs, plugins, and specialist agents.
7. **Compute & GPU Pool** — CPU/GPU execution capacity and worker nodes.

Pools are logical capability groups. A provider may participate in multiple pools; a requester should use one unified request interface.

## 4. Core request lifecycle

1. Requester submits a typed job through the unified API.
2. SINA authenticates the requester and validates permissions, input limits, and policy.
3. Pool Engine resolves the required capability and eligible providers.
4. Matching evaluates capability fit, health, capacity, latency, region, quality evidence, quota, and requester policy.
5. Scheduler selects a provider or an approved fallback.
6. Provider accepts or declines the job; the scheduler may select another eligible provider.
7. Execution runs in an isolated environment with bounded access to inputs and outputs.
8. SINA verifies the result contract and records provenance, quality signals, and usage.
9. Result is delivered to the requester; usage and settlement records are updated according to the agreed policy.
10. Provider and requester may submit feedback or dispute a result.

## 5. Matching and scheduling principles

Matching must be capability-based, not brand-based. Candidate selection should consider:
- Capability and contract compatibility.
- Provider health and recent reliability.
- Available capacity and queue depth.
- Quality evidence and task-specific benchmarks.
- Latency and geographic constraints.
- Data residency and privacy requirements.
- Requester plan, quotas, and explicit budget.
- Provider terms and consent.

Do not silently route private or sensitive inputs to an unapproved provider. Do not treat the cheapest provider as automatically best. Keep policy decisions explainable and auditable.

## 6. Trust, safety, and isolation

- Strong provider and requester identities.
- Least-privilege credentials and short-lived execution tokens.
- Per-job isolation and explicit input/output boundaries.
- No access to other providers' or requesters' data.
- Signed job/result metadata where practical.
- Audit trail for routing, execution, approval, and settlement events.
- Abuse detection, rate limits, quotas, and provider suspension controls.
- Human approval for sensitive actions and external side effects.
- Clear data retention and deletion policies.

## 7. Economics and governance

The architecture may support free contributions, quota-based access, paid services, or other owner-approved settlement models. These are policy options, not an instruction to activate billing.

Initial implementation must:
- Avoid mandatory tokens, cryptocurrency, or blockchain.
- Avoid paid infrastructure and paid provider activation without explicit project-owner approval.
- Show costs or quota consumption before a requester commits to a charge.
- Record provider terms and requester consent.
- Keep settlement modular so the network can launch with non-monetary or manually reconciled usage.

## 8. Proposed service boundaries

- Identity & Access Service
- Provider Registry
- Capability Catalog
- Pool Engine / Matching Service
- Scheduler & Job Router
- Provider Connector Runtime
- Job & Result Service
- Health / Quality / Reputation Service
- Metering & Quota Service
- Settlement Ledger (policy-gated)
- Audit & Governance Service
- Unified Public API and Provider Console

## 9. Suggested MVP sequence

### MVP 0 — Protocol and contracts
Define provider manifest, capability schema, job schema, result schema, health protocol, and error model.

### MVP 1 — Trusted small pool
Register a small number of explicitly approved providers; support one or two capability types; implement job submission, matching, execution, and result delivery.

### MVP 2 — Multi-provider resilience
Add health-aware routing, provider failover, queue limits, metering, quality signals, and provider console.

### MVP 3 — Multi-pool network
Expand to image, video, audio, 3D/game, models, agents/APIs, and compute/GPU using versioned adapters.

### MVP 4 — Open provider participation
Add self-service onboarding, validation, reputation, policy-based settlement, and stronger abuse controls after security review.

## 10. Non-goals and boundaries

- This network does not replace the SINA AI STUDIO product repository.
- It does not replace the SINA NEXUS research repository.
- It does not require one model vendor or one cloud provider.
- It does not assume all providers are trusted or always available.
- It does not automatically grant providers access to user data or production systems.
- It does not require blockchain, tokens, or speculative decentralization.
- It does not authorize paid services, subscriptions, or infrastructure by default.

## 11. Relationship to the other SINA repositories

- `AI_Studio_AI`: product experience, user accounts, projects, jobs, and the canonical product Orchestrator.
- `sina-nexus`: research, prototypes, benchmarks, and architecture decision records.
- `sina-pool-network`: provider/requester network implementation, provider protocol, pools, matching, scheduling, metering, and network operations.

The product should integrate through versioned APIs and provider adapters. The pool network must not take ownership of the main SINA Orchestrator or weaken existing product capabilities.

## 12. First architecture decisions to resolve

1. Provider-operated nodes vs. centrally hosted connectors vs. a hybrid model.
2. Whether providers execute jobs locally or through isolated SINA-managed workers.
3. Initial supported capability pool for MVP.
4. Provider verification and minimum trust requirements.
5. Data handling, region constraints, and retention defaults.
6. Free/quota-based MVP policy and future optional settlement model.
7. Job cancellation, retries, dispute handling, and result validation.
8. Whether provider discovery is public, invite-only, or approval-gated at launch.

No implementation status should be claimed until code, tests, and deployment evidence exist.
