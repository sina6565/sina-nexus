"""Run the dependency-free SINA MINI foundation demo.

From this directory:
    PYTHONPATH=src python examples/run_demo.py
"""
import asyncio

from sina_mini_core import (
    AgentContext,
    AgentRegistry,
    AgentRequest,
    InMemoryMemoryStore,
    InMemoryToolRegistry,
    Orchestrator,
    SkillRegistry,
)


class WelcomeAgent:
    agent_id = "welcome"

    async def execute(self, request, context):
        count = await context.memory.get("demo", "runs") or 0
        await context.memory.put("demo", "runs", count + 1)
        return {
            "message": f"Agent received: {request.task}",
            "run_number": count + 1,
        }


async def main() -> None:
    context = AgentContext(
        memory=InMemoryMemoryStore(),
        tools=InMemoryToolRegistry(),
        skills=SkillRegistry(),
    )
    registry = AgentRegistry()
    registry.register(WelcomeAgent())

    result = await Orchestrator(registry).dispatch(
        AgentRequest(task="Start SINA MINI", agent_id="welcome"),
        context,
    )
    print({
        "status": result.status.value,
        "output": result.output,
        "duration_ms": result.duration_ms,
    })


if __name__ == "__main__":
    asyncio.run(main())
