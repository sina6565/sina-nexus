"""First orchestration slice: explicit agent selection, no model routing yet."""
from __future__ import annotations

from .contracts import AgentContext, AgentRequest, AgentResult
from .registry import AgentRegistry
from .runtime import AgentRuntime


class Orchestrator:
    def __init__(self, agents: AgentRegistry, runtime: AgentRuntime | None = None) -> None:
        self._agents = agents
        self._runtime = runtime or AgentRuntime()

    async def dispatch(self, request: AgentRequest, context: AgentContext) -> AgentResult:
        agent = self._agents.get(request.agent_id)
        return await self._runtime.run(agent, request, context)
