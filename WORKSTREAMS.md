# SINA NEXUS — Workstreams & Branch Plan

This file is the execution map for NEXUS. A workstream is a continuing area of responsibility; a Git branch is a temporary line of development for a specific task. Do not create permanent empty branches merely to represent every lab.

## Workstream register

| ID | Workstream | Suggested branch prefix | Main responsibility | Required outputs |
|---|---|---|---|---|
| NEX-01 | AI & Multimodal | `research/ai-multimodal/*` | Models for text, image, video, audio, speech, SLM/LLM, local inference | Candidate matrix, license/cost checks, benchmark reports |
| NEX-02 | Game Technology | `research/game-tech/*` | Unreal Engine 5, Unity, Godot 4, Phaser, Three.js/R3F | Engine comparison, export/runtime tests, prototype recommendation |
| NEX-03 | 3D Worlds & Characters | `research/3d-worlds/*` | 3D generation, rigging, animation, materials, scene pipelines | Reproducible asset-to-scene workflow, quality and runtime tests |
| NEX-04 | Agents & Orchestration | `research/agents/*` | Planning, routing, tools, memory, MCP, approvals, observability | Architecture research, compatibility map, isolated prototypes |
| NEX-05 | Creative Technology | `research/creative-tech/*` | Website/app creation, image/video/audio, motion graphics, animation | Workflow comparisons, export/editability tests |
| NEX-06 | Infrastructure & Models | `research/infrastructure/*` | Local-first serving, GPU/compute, storage, queues, deployment, cost | Resource profiles, architecture options, cost/risk report |
| NEX-07 | Product Investigations | `research/product-evaluations/*` | Playhouse, Unity Spark, Google Playground | Official-source reports and Adopt/Prototype/Monitor/Reject decisions |
| NEX-08 | Governance & Integration | `docs/governance/*` and `integration/*` | Research standards, decision records, safe transfer to products | Governance docs, decision records, integration proposals |
| NEX-09 | SINA Computer Use Lab | `research/computer-use/*` | Observe/plan/act/verify computer-use experiments | Reproducible task benchmarks, limitations, safety findings |
| NEX-10 | Autonomous Desktop Agent | `research/desktop-agent/*` | Desktop task execution across supported applications | Isolated prototype, task success and recovery report |
| NEX-11 | Vision & GUI Understanding | `research/vision-gui/*` | Screen perception, UI grounding, visual state understanding | Test protocol, grounding and state-recognition results |
| NEX-12 | Browser & App Automation | `research/browser-automation/*` | Browser and application workflows; API-first where appropriate | Workflow prototypes, API-vs-GUI comparison, security review |
| NEX-13 | Action & Execution Engine | `research/action-engine/*` | Action dispatch, verification, retries, and recovery | Execution contracts, state-machine design, reliability tests |
| NEX-14 | Agent Orchestration | `research/agent-orchestration/*` | Coordinate planners, executors, tools, and specialist agents | Orchestration design and compatibility map |
| NEX-15 | Human Approval & Security | `research/agent-security/*` | Permissions, approval gates, sandboxing, and auditability | Threat model, permission model, approval prototype |
| NEX-16 | Hybrid Cloud Infrastructure | `research/hybrid-cloud/*` | Local-first control plane with optional cloud execution | Hybrid architecture, failure-mode and cost report |
| NEX-17 | GPU Compute Network | `research/gpu-compute/*` | Evaluate GPU resources, drivers, serving, and placement | GPU compatibility matrix and workload benchmarks |
| NEX-18 | Cloud Worker System | `research/cloud-workers/*` | Queue-driven, scalable execution workers | Worker lifecycle prototype, concurrency and retry tests |
| NEX-19 | Local AI Runtime | `research/local-runtime/*` | Portable local model/tool runtime | Runtime comparison, provider adapters, resource profiles |
| NEX-20 | Compute Orchestrator | `research/compute-orchestration/*` | Resource-aware scheduling across local and remote compute | Scheduling policy, capability contracts, failover tests |
| NEX-21 | Auto Scaling & Load Management | `research/scaling-load/*` | Backpressure, concurrency, health checks, graceful degradation | Load tests, scaling policy, queue saturation report |
| NEX-22 | Infrastructure Cost Optimizer | `research/cost-optimization/*` | Budgets, quotas, metering, cost-aware routing | Cost model, usage proposal, guardrail tests |
| NEX-23 | Core Integration Gateway | `integration/core-gateway/*` | Controlled transfer of validated capabilities into SINA AI STUDIO | Versioned contracts, adapter proposal, integration checklist |
| NEX-24 | SINA AI POOL NETWORK Research | `research/pool-network/*` | Architecture research for a unified provider/requester resource pool | Architecture decision, threat model, API contracts, MVP plan |

## SINA AI POOL NETWORK boundary

The intended implementation is in the separate repository sina6565/sina-pool-network. NEXUS owns research and architecture only; it must not become a duplicate implementation repository.

The network connects:
- **Providers:** compute/GPU capacity, model endpoints, APIs, tools, or agents.
- **Requesters / Consumers:** users, organizations, developers, and authorized agents.
- **SINA Pool Engine:** resource registration and validation, matching, scheduling, quality/health monitoring, metering, and policy-governed settlement.

Initial capability pools: Image, Video, Audio, 3D/Game, Models, Agents/APIs, and Compute/GPU. Design for provider independence, explicit consent, secure isolation, auditability, and graceful provider failure. No blockchain/token dependency and no paid resource activation without owner approval.

## Branch creation policy

Create a branch when a concrete task is ready to begin—not simply because a workstream exists.

Examples:
- `research/ai-multimodal/model-candidate-matrix`
- `research/game-tech/engine-comparison`
- `research/3d-worlds/character-pipeline-review`
- `research/agents/orchestration-architecture-study`
- `research/creative-tech/export-workflow-review`
- `research/infrastructure/local-inference-benchmark`
- `research/product-evaluations/playhouse-review`
- `docs/governance/research-templates`

Each branch should address one focused deliverable. Merge completed documentation and approved reusable research artifacts into `main) by pull request. Keep large or unstable prototypes isolated; do not merge them merely to close a task.

## Task lifecycle

1. Create an issue with a clear research question and owner.
2. Define acceptance criteria, scope, constraints, and a free-first budget.
3. Create a focused branch from the current `main).
4. Record official sources, access conditions, license, privacy, and pricing.
5. Conduct the investigation or isolated prototype.
6. Attach evidence, measurements, limitations, and reproducible steps.
7. Request review and record the recommendation.
8. Merge the research record when approved; product integration requires a separate approval.

## Definition of done

A task is complete only when:
- Its research question is answered or explicitly marked unresolved.
- Claims are separated into verified, unverified, and unknown.
- Sources and check dates are recorded.
- Cost, licensing, privacy, and security have been reviewed.
- Test steps and results are reproducible where applicable.
- A next-step recommendation and decision owner are identified.

## First execution queue

1. NEX-09–NEX-15: define the Computer Use and autonomous execution architecture, then select one small safety-bounded prototype.
2. NEX-16–NEX-22: define hybrid cloud and private compute options; benchmark free/local-first paths before any paid resource.
3. NEX-23: define the integration gateway and compatibility requirements for validated transfers.
4. NEX-24: prepare the SINA AI POOL NETWORK architecture brief and MVP boundaries.
5. NEX-08: finish repository governance and add research/evaluation templates.
2. NEX-07: verify Playhouse, Unity Spark, and Google Playground from official sources.
3. NEX-02: compare engines against SINA's 3D game-builder requirements.
4. NEX-01: build a free/local-first multimodal model candidate matrix.
5. NEX-03: evaluate the 3D character and environment pipeline.
6. NEX-04: map agent research against the existing SINA AI STUDIO orchestrator.
7. NEX-06: benchmark feasible local inference and compute options.
8. NEX-05: evaluate creative workflows and editable/exportable outputs.

The project owner may change this order at any time.
