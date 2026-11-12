import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from sina_mini_core import (  # noqa: E402
    AgentContext,
    AgentRegistry,
    AgentRequest,
    InMemoryMemoryStore,
    InMemoryToolRegistry,
    Orchestrator,
    RunStatus,
    SkillRegistry,
)


class EchoAgent:
    agent_id = "echo"

    async def execute(self, request, context):
        await context.memory.put("tests", request.request_id, request.task)
        return {"echo": request.task}


class BrokenAgent:
    agent_id = "broken"

    async def execute(self, request, context):
        raise RuntimeError("sensitive internal detail")


class FoundationTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.memory = InMemoryMemoryStore()
        self.context = AgentContext(
            memory=self.memory,
            tools=InMemoryToolRegistry(),
            skills=SkillRegistry(),
        )
        self.agents = AgentRegistry()

    async def test_dispatches_to_registered_agent(self):
        self.agents.register(EchoAgent())
        result = await Orchestrator(self.agents).dispatch(
            AgentRequest(task="hello", agent_id="echo"), self.context
        )
        self.assertEqual(result.status, RunStatus.SUCCEEDED)
        self.assertEqual(result.output, {"echo": "hello"})
        self.assertEqual(await self.memory.get("tests", result.request_id), "hello")

    async def test_failure_is_normalized_without_leaking_exception(self):
        self.agents.register(BrokenAgent())
        result = await Orchestrator(self.agents).dispatch(
            AgentRequest(task="run", agent_id="broken"), self.context
        )
        self.assertEqual(result.status, RunStatus.FAILED)
        self.assertNotIn("sensitive internal detail", result.error_message)

    async def test_unknown_agent_is_rejected(self):
        with self.assertRaises(LookupError):
            await Orchestrator(self.agents).dispatch(
                AgentRequest(task="run", agent_id="missing"), self.context
            )

    async def test_memory_is_namespaced(self):
        await self.memory.put("user-a", "preference", "x")
        await self.memory.put("user-b", "preference", "y")
        self.assertEqual(await self.memory.get("user-a", "preference"), "x")
        self.assertEqual(await self.memory.get("user-b", "preference"), "y")


if __name__ == "__main__":
    unittest.main()
