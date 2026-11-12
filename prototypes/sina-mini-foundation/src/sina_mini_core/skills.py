"""Skill definitions are data; execution policy belongs to the Agent/runtime."""
from __future__ import annotations

from .contracts import Skill


class SkillRegistry:
    def __init__(self) -> None:
        self._skills: dict[str, Skill] = {}

    def register(self, skill: Skill) -> None:
        if not skill.skill_id.strip():
            raise ValueError("skill_id must be non-empty")
        if skill.skill_id in self._skills:
            raise ValueError(f"skill already registered: {skill.skill_id}")
        self._skills[skill.skill_id] = skill

    def get(self, skill_id: str) -> Skill:
        try:
            return self._skills[skill_id]
        except KeyError as exc:
            raise LookupError(f"unknown skill: {skill_id}") from exc

    def list(self) -> tuple[Skill, ...]:
        return tuple(self._skills[key] for key in sorted(self._skills))
