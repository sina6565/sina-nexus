# SINA NEXUS

**Technology Research & Innovation Division of SINA AI STUDIO**

> Research with evidence. Prototype with purpose. Integrate only what proves its value.

SINA NEXUS is the research, experimentation, and technology innovation division of SINA AI STUDIO. It explores emerging technologies, evaluates tools and models, builds prototypes, and turns validated findings into clear technical recommendations.

Its purpose is to help SINA move from ideas to reliable capabilities—without compromising product stability, ownership, security, or long-term independence.

---

## 1. Mission

SINA NEXUS exists to:

- Discover and evaluate promising AI, software, creative, and infrastructure technologies.
- Research models, APIs, open-source projects, developer platforms, and emerging products.
- Build small, reproducible prototypes to test real capabilities—not just demonstrations.
- Benchmark quality, speed, resource requirements, reliability, licensing, and total cost.
- Identify opportunities for original SINA technology, products, and intellectual property.
- Deliver evidence-based recommendations to the SINA AI STUDIO product and engineering teams.

**Core mission:** turn research into validated technology and validated technology into useful product capabilities.

## 2. Relationship to SINA AI STUDIO

SINA NEXUS is a dedicated R&D workspace. It is not a replacement for, fork of, or competing implementation of the main SINA AI STUDIO platform.

| Repository / initiative | Responsibility |
|---|---|
| `sina6565/AI_Studio_AI` | Main SINA AI STUDIO product and production platform |
| `sina6565/sina-nexus` | Research, experiments, benchmarks, prototypes, and technical decision records |
| `sina6565/sina-pool-network` | Independent shared network connecting capability/compute providers with requesters through a SINA coordination layer |
| `sina6565/sina-pool-network` | Separate network/marketplace initiative for connecting AI capability providers with users, subject to its own product and governance plan |

The main platform remains the canonical production codebase. NEXUS experiments must not silently replace production components or introduce unverified dependencies.

### Integration boundary

A NEXUS result may be proposed for the main platform only when it has:

1. A documented use case and measurable benefit.
2. Reproducible test results and known limitations.
3. A reviewed license and commercial-use position.
4. A security, privacy, and data-handling assessment.
5. A realistic operating-cost and infrastructure assessment.
6. A compatibility plan that preserves existing architecture and capabilities.
7. Explicit approval from the SINA project owner and relevant engineering maintainers.

Integration should happen through a documented proposal, API, adapter, or controlled pull request—not by copying experimental code directly into production.

## 3. Research Labs

### 3.1 AI & Multimodal Systems

Research text, image, video, audio, speech, multimodal, and small language models (SLMs) as well as large language models (LLMs).

Research topics include:
- Open-weight and open-source models.
- Text-to-image, image understanding, image editing, and visual composition.
- Text-to-video, video understanding, motion, and animation.
- Speech recognition, text-to-speech, voice, and audio generation.
- Character consistency and multimodal workflows.
- Model quantization, inference efficiency, and local deployment.

### 3.2 Game Technology & Interactive Worlds

Evaluate technologies for creating, running, and exporting interactive 2D and 3D experiences.

Research areas include:
- Unreal Engine 5.
- Unity.
- Godot 4.
- Three.js and React Three Fiber.
- Phaser and browser-based game technologies.
- Game agents, level generation, physics, camera systems, movement, interaction, and runtime performance.

Engine names identify research areas, not endorsements, exclusive dependencies, or confirmed integrations.

### 3.3 3D Worlds, Characters & Animation

Research:
- 3D asset and environment generation.
- Character creation, rigging, and animation.
- Materials, textures, lighting, and scene composition.
- Motion generation and retargeting.
- Scene understanding and procedural world building.
- Import/export formats, interoperability, and runtime optimization.

### 3.4 AI Agents & Orchestration

Explore reliable agent systems and tool-using workflows, including:
- Task planning and decomposition.
- Capability-based routing and provider selection.
- Execution management, retries, and reflection.
- Agent and tool registries.
- Working memory and context management.
- MCP and external tool interoperability.
- Human approval, permissions, audit trails, and observability.

Research must complement—not duplicate or bypass—the main platform's existing orchestration and provider architecture.

### 3.5 Creative Technology

Explore workflows that connect AI with:
- Website and application creation.
- Image, video, audio, and music production.
- Motion graphics and animation.
- Interactive storytelling and digital characters.
- Creative automation and reusable production pipelines.

### 3.6 Models, Infrastructure & Systems Engineering

Evaluate:
- Local-first inference and deployment.
- GPU and compute options.
- Model serving and API integration.
- Storage, queues, networking, and job execution.
- Performance, reliability, scaling, and cost controls.
- Portable architectures and vendor-independent designs.


### 3.7 Computer Use & Autonomous Execution

Research agents that can perceive and operate desktop and browser interfaces, in addition to using structured APIs and tools. This is an execution-capability research track, not a plan to train a foundation language model from scratch.

Research areas include:
- Visual desktop and browser understanding.
- Computer Use action loops: observe, plan, act, verify, and recover.
- Browser and application automation.
- Permission-scoped tool execution and sandboxing.
- Human approval for sensitive or irreversible actions.
- Audit logs, task replay, and failure recovery.
- API-first execution where a supported API is safer and more reliable than GUI automation.

### 3.8 SINA AI POOL NETWORK Research

Research the architecture of a unified resource and capability pool that connects independent providers with requesters. The network is a separate product/repository, while NEXUS owns research, evaluation, and architecture proposals.

Research areas include:
- Provider onboarding and capability/resource registration.
- Requester job submission and capability requirements.
- Capability pools for image, video, audio, 3D/game, AI models, agents, APIs, and compute/GPU.
- Matching, scheduling, routing, fallback, and workload placement.
- Provider validation, health, reputation, quality, and service-level evidence.
- Usage metering, transparent pricing/quotas, and settlement design.
- Identity, permissions, data isolation, security, and dispute handling.
- Open interfaces and adapters that avoid provider lock-in.

## 4. Initial Research Tracks

The first research tracks include the following products and technology areas:

- **Playhouse** — investigate its current capabilities, access requirements, 3D workflow, export options, terms, and possible relevance to SINA.
- **Unity Spark** — investigate its current availability, AI-assisted development workflow, technical requirements, licensing, and integration possibilities.
- **Google Playground** — verify the exact product, current availability, supported creation workflow, export options, geographic restrictions, and terms before evaluating it.

These are research subjects, not confirmed SINA integrations or production dependencies. Product names, features, availability, and access conditions must be verified against current official sources before conclusions are recorded.

Each research track must produce a written evaluation and a recommendation: **Adopt, Prototype Further, Monitor, or Reject**.

## 5. Research Principles

All NEXUS work follows these principles:

1. **Evidence before claims** — distinguish verified facts, measured results, assumptions, and open questions.
2. **Research before adoption** — do not adopt a technology because it is popular or visually impressive.
3. **Prototype before integration** — validate a real use case in an isolated environment.
4. **Free-first and cost-aware** — prioritize free, open-source, and locally runnable options. Do not create paid subscriptions, incur usage charges, or provision paid infrastructure without explicit approval.
5. **Open standards and portability** — avoid unnecessary vendor lock-in and preserve the ability to change providers.
6. **Ownership and licensing** — record code, model, dataset, asset, and output licenses; verify commercial-use rights before product use.
7. **Privacy and security by design** — never expose credentials, private user data, confidential project information, or production secrets in experiments.
8. **Reproducibility** — record versions, configurations, hardware, test data sources, and steps needed to reproduce results.
9. **Production stability** — experimental components stay isolated until they pass the integration requirements.
10. **Respect existing work** — preserve the main SINA platform's capabilities and architecture; no destructive changes or unapproved rewrites.

## 6. Standard Research Workflow

Every significant investigation should follow this lifecycle:

1. **Define** — state the question, use case, success criteria, and constraints.
2. **Discover** — find official documentation, repositories, papers, terms, and credible technical evidence.
3. **Verify** — check current availability, geographic access, account requirements, pricing, licensing, and commercial restrictions.
4. **Evaluate** — compare capability, quality, latency, reliability, resource use, privacy, and cost.
5. **Prototype** — build the smallest isolated experiment that can answer the research question.
6. **Benchmark** — test against documented criteria and retain reproducible evidence.
7. **Review** — identify risks, limitations, dependencies, and unresolved questions.
8. **Decide** — recommend Adopt, Prototype Further, Monitor, or Reject.
9. **Transfer** — if approved, prepare an integration proposal for the appropriate SINA product repository.

A failed experiment is useful when its hypothesis, evidence, and lessons are documented.

## 7. Evaluation Scorecard

Use a consistent scorecard when comparing technologies. Rate each criterion from 1 to 5, or mark it **Unknown** when evidence is insufficient.

| Criterion | What to assess |
|---|---|
| Capability | Does it solve the intended problem? |
| Output quality | Is the result good enough for the intended product use? |
| Reliability | Does it work consistently under repeatable tests? |
| Performance | Latency, throughput, and runtime behavior |
| Resource demand | GPU, CPU, memory, storage, and bandwidth |
| Cost | Free tier, usage charges, infrastructure, and operating cost |
| License & IP | Source, model, data, asset, and commercial-use rights |
| Privacy & security | Data retention, processing location, access controls, and risks |
| Portability | Export formats, APIs, standards, and vendor dependence |
| Integration effort | Compatibility, maintenance burden, and operational complexity |

Do not calculate a final score when critical criteria—especially licensing, privacy, or cost—are unknown. Record the uncertainty instead.

## 8. Repository Structure

The repository should grow in a documented, modular way:

```text
sina-nexus/
├── README.md
├── GOVERNANCE.md
├── ROADMAP.md
├── CONTRIBUTING.md
├── LICENSE-REVIEW.md
├── research/
│   ├── ai-multimodal/
│   ├── game-technology/
│   ├── 3d-worlds-characters/
│   ├── agents-orchestration/
│   ├── creative-technology/
│   └── infrastructure-models/
├── evaluations/
│   ├── templates/
│   └── completed/
├── prototypes/
│   ├── README.md
│   └── ...
├── benchmarks/
│   ├── methodology/
│   └── results/
├── decisions/
│   ├── accepted/
│   ├── rejected/
│   └── deferred/
├── integration-proposals/
└── docs/
    ├── architecture/
    ├── security/
    └── operations/
```

Create folders when there is actual work to put in them. Do not add empty frameworks or unnecessary dependencies just to make the repository look complete.

## 9. Research Record Template

Every substantial evaluation should document:

- Research title and date.
- Owner or contributor.
- Question and intended SINA use case.
- Official project and documentation links.
- Version, release, or model identifier.
- Access and geographic requirements.
- License and commercial-use findings.
- Pricing and resource requirements.
- Test environment and reproducible steps.
- Results, measurements, and evidence.
- Limitations, security/privacy risks, and unknowns.
- Recommendation: Adopt / Prototype Further / Monitor / Reject.
- Proposed next step and any approval required.

## 10. Governance & Decision Rights

- The SINA project owner retains final authority over product direction, priorities, public release, and integration into SINA AI STUDIO.
- Contributors may research and prototype within the approved scope.
- No contributor may publish confidential SINA information, credentials, private datasets, or unreleased product plans.
- No paid service, subscription, cloud resource, or external commitment may be activated without explicit authorization.
- No production repository, deployment, database, provider configuration, or user-facing capability may be changed solely on the basis of an experiment.
- Decisions and changes must be traceable through issues, pull requests, research records, and commits.

## 11. Intellectual Property & Responsible Use

Before using external code, models, datasets, 3D assets, plugins, or generated content in a SINA product:

- Identify the source and applicable license or terms.
- Check redistribution, modification, attribution, and commercial-use permissions.
- Record restrictions and required notices.
- Check whether outputs, training data, or uploaded content create additional obligations.
- Do not assume that public access, an open repository, a free tier, or a successful download grants commercial rights.

SINA-owned work should be clearly separated from third-party material. Do not commit secrets, private keys, access tokens, or personal data.

## 12. Initial Milestones

### Phase 1 — Establish the research foundation
- Maintain this charter and repository governance.
- Add research and evaluation templates.
- Select a small number of high-value research questions.
- Record official sources, constraints, and unknowns.

### Phase 2 — Run controlled evaluations
- Evaluate the initial Playhouse, Unity Spark, and Google Playground research tracks.
- Compare relevant open-source and local-first alternatives.
- Build isolated prototypes only where they answer a defined question.
- Publish benchmark results and decision records.

### Phase 3 — Validate original SINA capabilities
- Identify gaps that existing technologies do not adequately solve.
- Design original components and reusable technical assets.
- Assess whether prototypes can become maintainable SINA-owned capabilities.

### Phase 4 — Controlled product transfer
- Submit integration proposals to the appropriate product repository.
- Require owner approval, technical review, tests, and documented rollback plans.
- Keep rejected, deferred, and experimental work in NEXUS.

Milestones are research goals, not claims that these capabilities already exist.

## 13. Definition of Success

SINA NEXUS succeeds when it consistently produces:

- Reliable, evidence-backed technology evaluations.
- Reproducible prototypes and benchmarks.
- Clear decisions that reduce technical and commercial risk.
- Original SINA technology where it creates meaningful advantage.
- Safe, controlled integration proposals that strengthen SINA AI STUDIO without reducing existing capabilities.

---

**SINA NEXUS**  
*Technology Research & Innovation Division of SINA AI STUDIO*

**Research boldly. Verify rigorously. Build responsibly.**


## 14. Project Execution Documents

Use these documents as the operational source of truth for planning and governance:

- [Roadmap](ROADMAP.md) — phases, research priorities, and exit criteria.
- [Governance](GOVERNANCE.md) — authority, approvals, security, IP, and contribution rules.
- [Workstreams & Branch Plan](WORKSTREAMS.md) — research tracks, branch naming, task lifecycle, and first execution queue.
- [Research record template](evaluations/templates/RESEARCH_TEMPLATE.md) — standard evidence record.
- [Product evaluation template](evaluations/templates/PRODUCT_REVIEW_TEMPLATE.md) — official product and eligibility review.
- [Benchmark template](benchmarks/templates/BENCHMARK_TEMPLATE.md) — reproducible technical measurements.
- [Integration proposal template](integration-proposals/TEMPLATE.md) — controlled transfer into a SINA product.

## 15. Newly Added Execution Tracks

The following workstreams extend the research charter. They are planned work, not claims of implementation:

- NEX-09–NEX-15: Computer Use, autonomous desktop agents, vision/GUI understanding, browser/app automation, action execution, agent orchestration, and human approval/security.
- NEX-16–NEX-22: hybrid cloud infrastructure, GPU compute network, cloud workers, local AI runtime, compute orchestration, autoscaling/load management, and infrastructure cost optimization.
- NEX-23: Core Integration Gateway for controlled transfer of validated research into the main SINA product.
- NEX-24: SINA AI POOL NETWORK research and architecture, kept distinct from the implementation repository sina6565/sina-pool-network.

