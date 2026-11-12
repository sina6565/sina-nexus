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

1. NEX-08: finish repository governance and add research/evaluation templates.
2. NEX-07: verify Playhouse, Unity Spark, and Google Playground from official sources.
3. NEX-02: compare engines against SINA's 3D game-builder requirements.
4. NEX-01: build a free/local-first multimodal model candidate matrix.
5. NEX-03: evaluate the 3D character and environment pipeline.
6. NEX-04: map agent research against the existing SINA AI STUDIO orchestrator.
7. NEX-06: benchmark feasible local inference and compute options.
8. NEX-05: evaluate creative workflows and editable/exportable outputs.

The project owner may change this order at any time.
