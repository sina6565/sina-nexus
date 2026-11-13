# SINA NEXUS — Roadmap

This roadmap defines the order of work for the SINA NEXUS research and innovation division. It is a plan, not a claim that any listed capability has already been implemented.

## Operating priorities

1. Establish governance, research records, and reproducible evaluation.
2. Verify the initial research targets using official sources.
3. Run small, isolated experiments against measurable use cases.
4. Identify original SINA opportunities and document technical decisions.
5. Transfer only approved, tested results to the appropriate product repository.

## Phase 0 — Repository foundation

- [x] Establish the NEXUS mission and research charter in README.
- [ ] Publish governance, contribution, and decision-making rules.
- [ ] Publish workstream ownership, branch conventions, and acceptance criteria.
- [ ] Add reusable research, evaluation, benchmark, and integration-proposal templates.
- [ ] Confirm repository visibility and access policy with the project owner.

**Exit criteria:** contributors can identify the scope, rules, workflow, and required evidence for every research task.

## Phase 1 — Research discovery and verification

### Workstream A: AI & multimodal systems
- Inventory candidate open-weight and open-source models for text, image, video, audio, speech, and multimodal tasks.
- Record hardware requirements, model licenses, commercial restrictions, inference methods, and free/local options.
- Compare small models (SLMs) and larger models by task; do not assume one model should act as the central orchestrator.
- Deliver a verified candidate matrix and prioritized experiments.

### Workstream B: Game technology
- Evaluate Unreal Engine 5, Unity, Godot 4, Phaser, Three.js, and React Three Fiber against SINA's browser and 3D game-builder requirements.
- Compare editor/runtime workflows, export, scripting, physics, camera/movement systems, platform support, licensing, and device requirements.
- Deliver an engine decision matrix and a recommended prototype path.

### Workstream C: 3D worlds, characters, and animation
- Investigate generation, retopology, rigging, animation, materials, scene assembly, and export pipelines.
- Test interoperability and runtime suitability rather than judging only by preview quality.
- Deliver a reproducible asset-to-scene workflow and limitations report.

### Workstream D: Agents and orchestration
- Research planning, routing, tool registries, memory, execution, reflection, MCP, approvals, and observability.
- Map findings against the existing AI_Studio_AI architecture before proposing changes.
- Deliver architecture notes and non-invasive adapter/prototype proposals.

### Workstream E: Creative technology
- Evaluate AI-assisted website/app creation, image/video/audio production, motion graphics, and animation workflows.
- Record editability, exportability, commercial rights, and whether results can be maintained after export.
- Deliver workflow comparisons and reusable pipeline proposals.

### Workstream F: Infrastructure and model engineering
- Compare local-first inference, GPU/compute options, serving, queues, storage, and deployment patterns.
- Prioritize free/open-source and low-cost paths; no paid resources without explicit approval.
- Deliver measured resource profiles, deployment options, and cost/risk comparisons.

**Exit criteria:** every active research track has official sources, a clear question, an evaluation record, known unknowns, and a next-step recommendation.

## Phase 2 — Initial named product investigations

Investigate Playhouse, Unity Spark, and the exact Google Playground product referred to by the project owner.

For each, verify from official sources:
- Exact product identity, current status, and official URLs.
- Access requirements, waitlists, account and age requirements.
- Country availability and any geographic restrictions.
- Pricing, free tier, usage limits, and potential paid requirements.
- Export formats, API availability, data handling, and lock-in.
- License, ownership, and commercial-use rights.
- Practical fit for SINA use cases.

**Deliverable:** one research report per product, ending in Adopt / Prototype Further / Monitor / Reject. Do not represent an unverified feature or access claim as fact.

## Phase 3 — Controlled prototypes and benchmarks

- Select only experiments with a written hypothesis and acceptance criteria.
- Keep prototypes isolated from production credentials, databases, deployments, and user data.
- Record source commit, dependency versions, hardware, test inputs, methodology, outputs, and limitations.
- Benchmark quality, reliability, latency, resource use, and cost.
- Stop experiments that require unapproved spending or create unacceptable legal, privacy, or security risks.

**Exit criteria:** a third party can reproduce the result and understand its limitations.

## Phase 4 — Original SINA technology

- Identify capability gaps that cannot be solved adequately by adopting an existing tool.
- Design SINA-owned components only where there is a measurable product advantage.
- Record architecture, interfaces, IP provenance, tests, and maintenance burden.
- Keep research prototypes separate until approved for productization.

## Phase 5 — Controlled integration

- Submit an integration proposal to the correct product repository.
- Obtain explicit project-owner approval.
- Review architecture compatibility, security, privacy, license, operating cost, tests, and rollback.
- Integrate through a reviewed PR or documented API/adapter.
- Verify that no existing SINA AI STUDIO capability is removed or weakened.

## Prioritization

Use this order unless the project owner changes it:

1. High relevance to current SINA product goals.
2. Free/local or low-cost feasibility.
3. Clear commercial and licensing position.
4. Reproducible evidence and practical export/integration.
5. High potential to create durable SINA-owned capability.

## Status vocabulary

- **Not started** — no research work has begun.
- **In progress** — active investigation or prototype.
- **Blocked** — a named dependency or unresolved requirement prevents progress.
- **Verified** — supported by recorded evidence and reproducible checks.
- **Recommended** — evidence supports a proposed next step; approval may still be required.
- **Integrated** — merged into the target product and verified there.

Never mark an item Verified or Integrated based only on a demo, marketing page, or untested code.

## Phase 6 — Autonomous Computer Use & Execution

- **NEX-09 — SINA Computer Use Lab:** end-to-end observe/plan/act/verify experiments.
- **NEX-10 — SINA Autonomous Desktop Agent:** task execution across desktop applications.
- **NEX-11 — SINA Vision & GUI Understanding:** screen perception, UI element grounding, and state recognition.
- **NEX-12 — SINA Browser & App Automation:** browser and application workflows, preferring official APIs when suitable.
- **NEX-13 — SINA Action & Execution Engine:** safe action dispatch, retries, state checks, and recovery.
- **NEX-14 — SINA Agent Orchestration:** coordination of planner, executor, tools, and specialist agents.
- **NEX-15 — SINA Human Approval & Security:** permissions, approval gates, audit trails, and sandbox boundaries.

**Exit criteria:** reproducible task success measurements, explicit permission boundaries, safe handling of sensitive actions, and documented failure/recovery behavior.

## Phase 7 — Hybrid Cloud & Private Compute

- **NEX-16 — SINA Hybrid Cloud Infrastructure:** local-first control plane with optional elastic cloud execution.
- **NEX-17 — SINA GPU Compute Network:** evaluate compatible GPU resources and workload placement.
- **NEX-18 — SINA Cloud Worker System:** stateless, queue-driven workers for scalable jobs.
- **NEX-19 — SINA Local AI Runtime:** local model and tool runtime with provider-independent interfaces.
- **NEX-20 — SINA Compute Orchestrator:** resource-aware scheduling across local and remote compute.
- **NEX-21 — SINA Auto Scaling & Load Management:** backpressure, concurrency limits, health-aware scaling, and graceful degradation.
- **NEX-22 — SINA Infrastructure Cost Optimizer:** budgets, quotas, usage visibility, and cost-aware routing.

**Constraints:** prioritize free/open-source and local-first options. Do not provision paid cloud resources or activate paid services without explicit approval. Cloud execution must be optional; core control and provider independence remain under SINA governance.

**Exit criteria:** measured workload profiles, tested local/cloud failover behavior, queue and concurrency tests, and a transparent cost model.

## Phase 8 — Product Integration & Shared Network Research

- **NEX-23 — SINA Core Integration Gateway:** define versioned contracts, adapters, compatibility checks, and a controlled path for approved NEXUS capabilities to reach the main SINA product.
- **NEX-24 — SINA AI POOL NETWORK Research:** define the shared provider/requester network, capability pools, matching and scheduling, validation, metering, reputation, and governance. Implementation belongs in the separate sina-pool-network repository.

The pool network connects providers (GPU/compute, models, APIs, tools, and agents) with requesters (users, organizations, developers, and authorized agents) through a SINA-managed registry and pool engine. Initial implementation must not depend on blockchain or tokens. Pricing and settlement remain explicit design decisions and must not trigger spending without approval.

**Exit criteria:** an architecture decision record, threat model, API contracts, provider/requester lifecycle, and a staged MVP plan approved by the project owner.
