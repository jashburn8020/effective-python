"""Item 16.

Prefer `get` Over `in` and `KeyError` to Handle Missing Dictionary Keys.
"""

from typing import Callable, Dict

import pytest


def increment_if_in(counter_mapping: Dict[str, int], key: str) -> None:
    """Use `if` and `in` to check for missing key."""
    if key in counter_mapping:
        count = counter_mapping[key]
    else:
        count = 0
    counter_mapping[key] = count + 1


def increment_keyerror(counter_mapping: Dict[str, int], key: str) -> None:
    """Rely on `KeyError` if a key is missing."""
    try:
        count = counter_mapping[key]
    except KeyError:
        count = 0
    counter_mapping[key] = count + 1


def increment_get_default(counter_mapping: Dict[str, int], key: str) -> None:
    """Use `get` method with default value."""
    count = counter_mapping.get(key, 0)
    counter_mapping[key] = count + 1


@pytest.mark.parametrize(
    "incrementor", [increment_if_in, increment_keyerror, increment_get_default]
)
def test_increment_counters(incrementor: Callable[[Dict[str, int], str], None]) -> None:
    """Increment counters in a `dict` using various `incrementor` strategies."""
    bread_votes = {"pumpernickel": 2, "sourdough": 1}
    # Key missing
    key = "wheat"
    incrementor(bread_votes, key)
    assert bread_votes[key] == 1

    # Key present
    key = "sourdough"
    incrementor(bread_votes, key)
    assert bread_votes[key] == 2


def test_get_complex_value() -> None:
    """Use `get` method and assignment expression for complex values."""
    bread_voters = {
        "baguette": ["Bob", "Alice"],
        "ciabatta": ["Coco", "Deb"],
    }

    key, voter = ("brioche", "Elmer")
    if (names := bread_voters.get(key)) is None:
        bread_voters[key] = names = []
    names.append(voter)

    assert bread_voters[key] == ["Elmer"]


def test_setdefault() -> None:
    """Use `setdefault`."""
    bread_voters = {
        "baguette": ["Bob", "Alice"],
        "ciabatta": ["Coco", "Deb"],
    }

    key, voter = ("brioche", "Elmer")
    names = bread_voters.setdefault(key, [])
    names.append(voter)

    assert bread_voters[key] == ["Elmer"]
