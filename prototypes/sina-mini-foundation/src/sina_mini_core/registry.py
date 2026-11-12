"""Small in-process registries; persistent/distributed registries are later adapters."""
from __future__ import annotations

from typing import Iterable

from .contracts import Agent, Tool


class RegistryError(LookupError):
    pass


class AgentRegistry:
    def __init__(self) -> None:
        self._agents: dict[str, Agent] = {}

    def register(self, agent: Agent) -> None:
        agent_id = getattr(agent, "agent_id", "").strip()
        if not agent_id:
            raise ValueError("agent.agent_id must be a non-empty string")
        if agent_id in self._agents:
            raise ValueError(f"agent already registered: {agent_id}")
        self._agents[agent_id] = agent

    def get(self, agent_id: str) -> Agent:
        try:
            return self._agents[agent_id]
        except KeyError as exc:
            raise RegistryError(f"unknown agent: {agent_id}") from exc

    def names(self) -> tuple[str, ...]:
        return tuple(sorted(self._agents))


class InMemoryToolRegistry:
    def __init__(self, tools: Iterable[Tool] = ()) -> None:
        self._tools: dict[str, Tool] = {}
        for tool in tools:
            self.register(tool)

    def register(self, tool: Tool) -> None:
        name = getattr(tool, "name", "").strip()
        if not name:
            raise ValueError("tool.name must be a non-empty string")
        if name in self._tools:
            raise ValueError(f"tool already registered: {name}")
        self._tools[name] = tool

    def get(self, name: str) -> Tool:
        try:
            return self._tools[name]
        except KeyError as exc:
            raise RegistryError(f"unknown tool: {name}") from exc

    def names(self) -> tuple[str, ...]:
        return tuple(sorted(self._tools))
