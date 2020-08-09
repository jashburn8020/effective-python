"""Item 14.

Sort by Complex Criteria Using the `key` Parameter.
"""

from typing import List
import pytest


class Tool:
    """Object does not support sorting by natural order."""

    def __init__(self, name: str, weight: float) -> None:
        self.name = name
        self.weight = weight


def test_sort_attribute() -> None:
    """Sort objects by their attribute."""
    tools = [
        Tool("level", 3.5),
        Tool("hammer", 1.25),
        Tool("screwdriver", 0.5),
        Tool("chisel", 0.25),
    ]

    tools.sort(key=lambda tool: tool.name)
    assert [tool.name for tool in tools] == ["chisel", "hammer", "level", "screwdriver"]

    tools.sort(key=lambda tool: tool.weight)
    assert [tool.name for tool in tools] == ["chisel", "screwdriver", "hammer", "level"]


@pytest.fixture(name="power_tools")
def fixture_power_tools() -> List[Tool]:
    """Return a list of power tools."""
    return [
        Tool("drill", 4),
        Tool("circular saw", 4),
        Tool("jackhammer", 40),
        Tool("sander", 4),
    ]


def test_sort_multiple_criteria(power_tools: List[Tool]) -> None:
    """Sort objects by multiple criteria.

    Ascending weight, then ascending name.
    """
    power_tools.sort(key=lambda tool: (tool.weight, tool.name))
    assert [(tool.name, tool.weight) for tool in power_tools] == [
        ("circular saw", 4),
        ("drill", 4),
        ("sander", 4),
        ("jackhammer", 40),
    ]


def test_sort_multiple_criteria_rev_numerical(power_tools: List[Tool]) -> None:
    """Sort objects by multiple criteria, reverse order for numerical values.

    Descending weight, then ascending name.
    """
    power_tools.sort(key=lambda tool: (-tool.weight, tool.name))
    assert [(tool.name, tool.weight) for tool in power_tools] == [
        ("jackhammer", 40),
        ("circular saw", 4),
        ("drill", 4),
        ("sander", 4),
    ]


def test_sort_multiple_criteria_rev_non_numerical(power_tools: List[Tool]) -> None:
    """Sort objects by multiple criteria, reverse order for non-numerical values.

    Ascending weight, then descending name. Sort by name, followed by weight.
    """
    power_tools.sort(key=lambda tool: tool.name, reverse=True)
    power_tools.sort(key=lambda tool: tool.weight)
    assert [(tool.name, tool.weight) for tool in power_tools] == [
        ("sander", 4),
        ("drill", 4),
        ("circular saw", 4),
        ("jackhammer", 40),
    ]
