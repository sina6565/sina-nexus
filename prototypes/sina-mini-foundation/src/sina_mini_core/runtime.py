"""Execution boundary for agents."""
from __future__ import annotations

from time import perf_counter

from .contracts import Agent, AgentContext, AgentRequest, AgentResult, RunStatus


class AgentRuntime:
    async def run(self, agent: Agent, request: AgentRequest, context: AgentContext) -> AgentResult:
        started = perf_counter()
        try:
            output = await agent.execute(request, context)
            return AgentResult(
                request_id=request.request_id,
                status=RunStatus.SUCCEEDED,
                output=output,
                duration_ms=max(0, round((perf_counter() - started) * 1000)),
            )
        except Exception:
            # Do not leak stack traces, secrets, or raw exception details to callers.
            return AgentResult(
                request_id=request.request_id,
                status=RunStatus.FAILED,
                error_code="AGENT_EXECUTION_FAILED",
                error_message="The agent could not complete the request.",
                duration_ms=max(0, round((perf_counter() - started) * 1000)),
            )
