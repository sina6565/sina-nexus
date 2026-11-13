# NEX-13 — Agentic Execution Engine: Research Intake & Technical Assessment

**Status:** Research intake recorded; source implementation not yet recovered or executed  
**Track:** NEX-13 — SINA Action & Execution Engine  
**Related tracks:** NEX-09 Computer Use, NEX-10 Desktop Agent, NEX-11 Vision & GUI, NEX-12 Browser/App Automation, NEX-14 Agent Orchestration, NEX-15 Human Approval & Security  
**Target product:** `sina6565/AI_Studio_AI` (integration only after review and explicit approval)  
**Research repository:** `sina6565/sina-nexus`

## 1. Executive summary

A user-supplied design describes a small Python-based mission execution environment. Its core pattern is:

1. Accept a mission and optional attachment.
2. Validate and normalize the request.
3. Produce a deterministic tool plan.
4. Execute registered tools in sequence.
5. persist job state, events, and outputs in SQLite.
6. Expose status and results through an HTTP API and a Persian RTL dashboard.

The proposed baseline includes text statistics, attachment metadata and SHA-256 calculation, and Markdown report composition. It explicitly does **not** call a language model, understand image/audio/video content, run MCP, provide agent memory, or execute autonomous computer actions.

This is a useful architectural seed for NEX-13 because it introduces a mission/job/event/result lifecycle and a tool registry. It is not yet a production-ready agent engine and must not be represented as one.

**Disposition:** Accept as an R&D input; prototype further after recovering the original source files and verifying the existing SINA architecture. Do not copy the supplied Python implementation into the production repository.

## 2. What was actually supplied

The conversation contained a text transcription of three named files:

- `server.py`
- `test_server.py`
- `.env.example`

The transcription describes:
- Python 3.11+ and standard-library-only implementation.
- `ThreadingHTTPServer` HTTP server.
- SQLite job and event persistence.
- `Engine`, deterministic planner, and `Registry`.
- A JSON-based tool context/output contract.
- Bearer-token authorization and basic Origin checking.
- A single-page Persian RTL dashboard.
- 16 test functions claimed in source: 9 core and 7 HTTP tests.
- A proposed ZIP creation command.

Important provenance limitation: this was copied from a rendered page, not recovered from an original downloadable archive. No ZIP, source attachment, repository URL for the source, or execution log was included in the supplied material. The displayed formatting appears to have collapsed some line breaks and transformed URLs into Markdown links. Therefore syntax defects in the transcription must not automatically be attributed to the original downloadable files.

## 3. Preliminary technical assessment

### Useful concepts worth carrying forward

- **Mission/job contract:** stable mission identity, request, plan, status, result, and error.
- **Event history:** explicit queued/running/step-started/step-completed/completed/failed/interrupted events.
- **Tool registry:** a narrow interface for adding approved capabilities.
- **Planner boundary:** planner output is validated against registered tools before execution.
- **Durable result record:** job state and structured output survive process restarts.
- **Human-inspectable workflow:** plan, execution trace, and artifacts are visible to the operator.
- **Provider independence:** the baseline can run without a model provider.
- **Honest capability reporting:** attachment metadata is not confused with semantic image/audio/video understanding.

These concepts should be mapped to existing SINA contracts rather than introduced as a parallel production architecture.

### Gaps and risks to investigate

| Area | Current supplied design | Research requirement |
|---|---|---|
| Planner | Fixed deterministic list | Typed planner interface; later model-assisted planning with schema validation |
| Orchestration | Single Engine | Reconcile with SINA Orchestrator; no competing orchestrator |
| Execution | Synchronous in HTTP request | Durable queue, worker lifecycle, cancellation, deadlines |
| Tools | In-process Python callables | Permission scopes, schemas, isolation, resource limits |
| Agents | No independent agents | Agent Registry, Base/Runner contracts, specialist coordination |
| Memory | No working or long-term memory | Explicit scoped working memory; later retrieval/RAG only if justified |
| Events | Basic SQLite event rows | Correlation IDs, structured event schema, traceability and retention |
| Retries | None | Idempotency, retry policy, backoff, deduplication and recovery |
| Attachments | Hash and metadata only | Safe content inspection, MIME/signature validation, quarantine and storage policy |
| Vision/audio/video | No semantic analysis | Separate capability adapters and measurable modality-specific tests |
| MCP | Not implemented | MCP client/server research, tool identity and permission mapping |
| Approval | No approval workflow | Human approval gates for sensitive, external, costly or irreversible actions |
| Security | Shared bearer token; basic checks | User identity, RBAC/capability grants, CSRF/origin model, rate limits, secret handling |
| Isolation | Trusted in-process code | Process/container sandbox, filesystem/network restrictions, CPU/memory/time quotas |
| Observability | Minimal event log | OpenTelemetry-compatible traces, metrics, logs and redaction |
| Storage | SQLite, no binary retention | SINA storage abstraction and retention/deletion controls |
| Deployment | Local development server | Production server, TLS, migrations, backup/restore, health/readiness checks |

### Specific observations from the copied transcription

1. Several Python statements appear concatenated (for example, multiple imports on one line). If the original files contain those exact bytes, they will fail to parse. The original files must be checked before treating this as a source defect.
2. The sample Origin values appear as Markdown links rather than literal origins. If present in the actual files, tests and browser requests will not agree with the configured origin.
3. The dashboard has no attachment picker, although the API schema supports an attachment. The UI also marks the text field required, while the API permits attachment-only submissions.
4. `POST /api/jobs` executes the complete workflow synchronously. Long-running jobs can tie up request threads and are not suitable for autonomous desktop or multimodal tasks.
5. The engine catches tool exceptions and returns a persisted failed job; the HTTP layer still returns 201. This is documented behavior in the sample, but clients must inspect job status and a future asynchronous API should separate acceptance from completion.
6. The attachment's decoded bytes are not retained or semantically inspected. Its declared MIME type is not verified against its actual content.
7. The Registry executes trusted host Python code. It is not a sandbox and must never be treated as safe execution for user-supplied code.
8. The tests are only written test cases. No test runner output, browser test, concurrency test, security test, or deployment verification was supplied.

## 4. Fit with the existing SINA architecture

The research must preserve the existing product architecture and the user's established boundaries:

- Main product: `sina6565/AI_Studio_AI`.
- R&D repository: `sina6565/sina-nexus`.
- Provider direction remains local-first: Ollama, ComfyUI, Whisper, Piper, and FFmpeg; cloud providers remain optional and must not become mandatory.
- SINA's own Orchestrator remains the control plane. External models may propose plans, but do not own SINA's governance or execution authority.
- Existing Provider Registry, Agent Registry, Tool Registry, approval/security, queue, and observability work must be reused or reconciled rather than duplicated.
- Keep the R&D implementation isolated. Transfer only validated, licensed, secure, tested capabilities through NEX-23 Core Integration Gateway and an approved pull request.
- Do not introduce paid services, subscriptions, cloud resources, or GPU usage without explicit owner approval.

### Proposed conceptual mapping

| Supplied concept | SINA target concept |
|---|---|
| `Engine` | Existing SINA Orchestrator + Execution Manager boundary |
| `default_plan` | Planner interface / validated execution plan |
| `Registry` | Existing Tool Registry and Agent Registry contracts |
| `Store` jobs/events | Existing job/event persistence and observability |
| Tool context | Versioned, typed execution context |
| Tool output dict | Structured, schema-validated result/artifact contract |
| Dashboard | Existing SINA mission/job UI; do not create a competing product UI |
| `inspect_attachment` | Modality-specific intake and processing adapters |
| Bearer token | Existing SINA authentication/authorization model |

This mapping is a research hypothesis, not a claim that every target component is currently implemented or verified. Confirm against the current main product repository before designing adapters.

## 5. Proposed research questions

1. What job, event, and execution contracts already exist in `AI_Studio_AI`, and what gaps remain?
2. Can the supplied job lifecycle be mapped to existing contracts without a second orchestrator or duplicate job system?
3. What is the smallest reliable worker model that supports durable jobs, cancellation, retries, and recovery?
4. How should Tool Registry entries declare JSON schemas, permissions, side effects, timeouts, and resource budgets?
5. How should the system distinguish read-only, reversible, externally visible, financial, destructive, and privileged actions?
6. Which actions require human approval, and how is approval bound to the exact plan and parameters?
7. How can SINA support observe → plan → act → verify → recover for browser/desktop tasks while preferring stable APIs when available?
8. What is the minimum useful working-memory design, and how does it avoid leaking data between users or missions?
9. Which local-first vision, speech, and multimodal adapters can be evaluated on available hardware without paid services?
10. Which execution traces and benchmarks will demonstrate reliability beyond a successful happy-path demo?

## 6. Staged research and prototype plan

### Stage A — Recover and verify source (first)

- Obtain the original `server.py`, `test_server.py`, `.env.example`, and any ZIP/download link.
- Compare original bytes with the copied transcription.
- Inspect archive contents, file paths, license, README, dependency manifests, sample configuration, and any omitted modules.
- Run syntax checks and the supplied tests in an isolated environment.
- Record actual test output and defects; do not claim tests passed before execution.

**Exit:** source provenance and complete file inventory are known; code parses; test results are recorded.

### Stage B — Architecture compatibility

- Inspect current `AI_Studio_AI` contracts for Orchestrator, jobs/queues, Agent/Tool/Provider registries, approval, auth, storage, and telemetry.
- Produce a mapping table: reuse / adapt / research only / reject.
- Identify duplicate responsibilities and integration risks.

**Exit:** owner-reviewed architecture decision record; no duplicate production core proposed.

### Stage C — Minimal isolated execution prototype

Build a small, local-first research prototype with:
- Mission intake and typed request schema.
- Deterministic planner first; model planner only behind a validated interface.
- Tool manifest with input/output schemas, permission scopes, timeout, side-effect class, and resource budget.
- Durable job state and event history.
- Worker-based execution, cancellation, idempotency, retry limits, and recovery.
- Artifact metadata and safe storage boundaries.
- Human approval gate for sensitive actions.
- Structured logs and reproducible tests.

Start with harmless tools (text analysis, file metadata, report generation) before any browser, shell, filesystem mutation, external network, or computer-use actions.

**Exit:** unit, integration, failure-recovery, permission, and concurrency tests pass in the isolated prototype; evidence is committed.

### Stage D — Computer-use and multimodal extensions

Only after the execution contract is reliable:
- Add screen capture and visual state understanding as a separate adapter.
- Add browser automation with API-first routing and explicit domain/session permissions.
- Add observe/plan/act/verify/recover loops.
- Add speech and image/video processors behind modality-specific provider contracts.
- Add MCP interoperability after tool identity, permissions, and audit behavior are defined.

**Exit:** task benchmarks include success, false action, recovery, latency, and safety metrics.

### Stage E — Controlled transfer

- Write an NEX-23 integration proposal.
- Identify the exact production interfaces and files affected.
- Include tests, migration/rollback, license, security, privacy, and operating-cost review.
- Obtain explicit project-owner approval before production changes.

## 7. Initial acceptance criteria

A prototype must not be called successful until it demonstrates:

- Mission requests are validated and assigned stable IDs.
- Every execution step is auditable and correlated to the mission.
- Invalid plans and unauthorized tools are rejected before execution.
- Tool input/output schemas are enforced.
- Tool timeouts and failures do not corrupt job state.
- Duplicate submissions can be detected or handled through idempotency keys.
- Jobs can be cancelled and interrupted jobs recover predictably.
- Sensitive actions require explicit, parameter-bound approval.
- Secrets and private payloads are redacted from logs and errors.
- Concurrency and queue saturation are tested.
- Artifacts have explicit retention and deletion behavior.
- The same tests can run without cloud credentials or paid services.

## 8. Missing material checklist

The user copied the visible page text and suspects the original page may have offered downloads that were not copied. The following remain unverified and should be requested/recovered:

- [ ] Original ZIP archive (if offered).
- [ ] Direct download links and file names.
- [ ] Original, unformatted `server.py`.
- [ ] Original, unformatted `test_server.py`.
- [ ] Original `.env.example`.
- [ ] Any `README.md`, setup guide, architecture diagrams, or API collection.
- [ ] Any requirements/lock files, Dockerfile, compose file, CI workflow, or deployment manifest.
- [ ] Any static assets, frontend files, screenshots, or browser preview.
- [ ] Any additional adapters, sample tools, migrations, or database files (database must be treated as potentially sensitive).
- [ ] License and attribution information.
- [ ] Test logs, screenshots, benchmark outputs, and known limitations from the original author.

Do not commit secrets, real tokens, personal data, production database files, or unreviewed binaries to this repository.

## 9. Time and effort estimate (planning estimate, not a delivery promise)

Assuming one engineer with repository access and the original source files:

| Scope | Indicative elapsed effort |
|---|---:|
| Recover files, inspect archive, repair transcription/source issues, run initial tests | 0.5–2 working days |
| Map against SINA architecture and write decision record | 1–3 working days |
| Build a safe local execution prototype with worker, typed tools, events, and approvals | 1–3 weeks |
| Add robust recovery, isolation, observability, and meaningful reliability/security tests | 2–4 additional weeks |
| Add browser/desktop Computer Use and multimodal adapters with benchmarks | 3–8+ additional weeks |
| Production integration, hardening, deployment and rollout | separate gated phase; estimate only after architecture and test evidence |

These ranges are not additive in every staffing scenario and depend on existing SINA components that can be reused. A small demonstration may be produced quickly; a reliable, secure autonomous execution system is a substantially larger engineering effort.

## 10. Current evidence status

| Item | Status |
|---|---|
| User-provided design text received | Confirmed in conversation |
| Three source filenames described | Confirmed in supplied text |
| Original downloadable ZIP recovered | Not yet |
| Source code copied into this repository | No |
| Source syntax verified | Not yet |
| Test suite executed | No |
| Browser UI rendered/tested | No |
| SINA production architecture compatibility verified | Not yet |
| Production integration approved | No |
| R&D intake documented | Yes, in this branch |

**Current recommendation:** Prototype Further. First recover the original files and inspect the canonical SINA architecture. The supplied design is a valuable execution-lifecycle reference, but the strategic opportunity is to evolve it into a safe, observable, permission-aware execution layer under SINA's own Orchestrator—not to adopt the small Python server as the product core.
