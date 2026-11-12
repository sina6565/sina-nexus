# SINA MINI — Foundation Architecture

## Current execution path

`AgentRequest -> Orchestrator -> AgentRegistry -> AgentRuntime -> Agent -> AgentResult`

The runtime receives an `AgentContext` containing replaceable interfaces for memory, tools, and skills. The initial adapters are in-process only.

## Boundaries

- **Core contracts:** request, result, status, Agent, Tool, MemoryStore, and Skill interfaces.
- **Orchestration:** selects an explicitly named registered Agent. Automatic planning/routing is not implemented.
- **Runtime:** awaits one Agent execution and normalizes ordinary execution exceptions. Cancellation is not swallowed.
- **Memory:** namespace/key API with a volatile in-memory adapter. No disk or cloud persistence exists yet.
- **Tools:** registry contract only. No tool execution policy or external tool is enabled yet.
- **Skills:** metadata registry only. Skills are not dynamically executed as code.

## Design decisions

1. Provider-neutral: no model SDK is imported by the core.
2. Adapter-first: storage and tools are defined by protocols.
3. Explicit dispatch: no hidden model selection or autonomous tool use in this first slice.
4. Minimal dependencies: runtime code uses the Python standard library.
5. Fail closed: execution errors returned to callers do not expose raw exception details.

## Not implemented

Authentication, authorization, durable memory, encryption at rest, multi-agent collaboration, collective learning, cloud sync, mobile UI, model inference, tool permissions, retries, and production observability.

## Next engineering gate

Run the tests and demo on Python 3.11+, then add durable storage only after its data ownership, namespace isolation, deletion, and migration behavior are specified.
