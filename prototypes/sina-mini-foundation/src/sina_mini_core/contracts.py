"""Stable contracts shared by the first SINA MINI foundation modules."""
from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Mapping, Protocol, Sequence
from uuid import uuid4


class RunStatus(str, Enum):
    SUCCEEDED = "succeeded"
    FAILED = "failed"


@dataclass(frozen=True, slots=True)
class AgentRequest:
    task: str
    agent_id: str = "default"
    request_id: str = field(default_factory=lambda: str(uuid4()))
    user_id: str | None = None
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True, slots=True)
class AgentResult:
    request_id: str
    status: RunStatus
    output: Any = None
    error_code: str | None = None
    error_message: str | None = None
    duration_ms: int = 0


@dataclass(frozen=True, slots=True)
class Skill:
    skill_id: str
    description: str
    instructions: str = ""


class Tool(Protocol):
    name: str

    async def invoke(self, arguments: Mapping[str, Any]) -> Any:
        """Execute a tool using validated arguments."""


class MemoryStore(Protocol):
    async def get(self, namespace: str, key: str) -> Any | None: ...
    async def put(self, namespace: str, key: str, value: Any) -> None: ...


class ToolRegistry(Protocol):
    def get(self, name: str) -> Tool: ...
    def names(self) -> Sequence[str]: ...


class SkillRegistry(Protocol):
    def get(self, skill_id: str) -> Skill: ...
    def list(self) -> Sequence[Skill]: ...


@dataclass(slots=True)
class AgentContext:
    memory: MemoryStore
    tools: ToolRegistry
    skills: SkillRegistry
    settings: Mapping[str, Any] = field(default_factory=dict)


class Agent(Protocol):
    agent_id: str

    async def execute(self, request: AgentRequest, context: AgentContext) -> Any:
        """Run one task and return a serializable result."""
