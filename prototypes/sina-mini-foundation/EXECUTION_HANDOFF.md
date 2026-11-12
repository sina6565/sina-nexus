# SINA MINI — Execution Agent Handoff

## Objective

Continue the isolated foundation prototype in this directory. Do not redesign the product or expand into future network features.

## Read first

1. `README.md`
2. `src/sina_mini_core/contracts.py`
3. `src/sina_mini_core/runtime.py`
4. `src/sina_mini_core/orchestrator.py`
5. `tests/test_core.py`

## Current module boundaries

- `contracts.py`: typed contracts and protocols.
- `registry.py`: in-process Agent and Tool registries.
- `runtime.py`: guarded asynchronous execution and normalized result.
- `orchestrator.py`: explicit dispatch to one registered Agent.
- `memory.py`: volatile namespaced adapter; not durable storage.
- `skills.py`: minimal skill metadata registry.

## First assignment for the execution agent

1. Run the existing tests with Python 3.11+.
2. Report exact command, environment, pass/fail count, and any traceback.
3. Review typing, async behavior, error boundaries, and package layout.
4. Add tests before changing behavior.
5. Propose the smallest necessary corrections as a focused commit on this branch.

## Guardrails

- Do not modify `main`.
- Do not add paid services, API keys, external network calls, or non-standard runtime dependencies.
- Do not implement collective learning, cloud synchronization, authentication, UI, or provider-specific LLM integrations in this phase.
- Do not store real user data or secrets.
- Do not replace the current architecture wholesale.
- Mark anything not actually executed as **not tested**.
