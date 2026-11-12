# SINA MINI — Foundation Prototype

This directory contains the first isolated, dependency-light foundation for SINA MINI.

## Scope of this first slice

- A small asynchronous Agent execution contract.
- An Agent registry and a single-agent Orchestrator.
- A runtime boundary that normalizes success and failure.
- Pluggable interfaces for tools, memory, and skills.
- An in-memory memory adapter for tests and local experiments.
- A dependency-free test suite.

## Explicitly out of scope

No model/provider integration, mobile UI, cloud sync, collective learning, user-data sharing, authentication, or production deployment is implemented here. These are later layers and must not be inferred from the interfaces.

## Runtime

- Python 3.11+
- Standard library only
- No API key or paid service required

Run tests from this directory:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

## Design constraints

1. Keep the core independent of any LLM vendor.
2. Keep adapters replaceable through protocols.
3. Do not store secrets or real personal data in this prototype.
4. Keep experimental code isolated from the production repository.
5. Add capabilities only behind explicit interfaces and tests.

This is a foundation prototype, not a production-ready personal agent.