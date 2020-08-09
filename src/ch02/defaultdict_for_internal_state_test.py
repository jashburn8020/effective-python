"""Item 17.

Prefer `defaultdict` Over `setdefault` to Handle Missing Items in Internal State.
"""

from collections import defaultdict
from typing import Callable, Dict, Set

import pytest


def access_get(visits: Dict[str, Set[str]], country: str, city: str) -> None:
    """Use `get` to access items when you don't control the `dict` creation."""
    if (cities := visits.get(country)) is None:
        visits[country] = cities = set()
    cities.add(city)


def access_setdefault(visits: Dict[str, Set[str]], country: str, city: str) -> None:
    """Use `setdefault` to access items when you don't control the `dict` creation."""
    visits.setdefault(country, set()).add(city)


@pytest.mark.parametrize("city_adder", [access_get, access_setdefault])
def test_no_control_dict_creation(
    city_adder: Callable[[Dict[str, Set[str]], str, str], None]
) -> None:
    """Use `get` and `setdefault` to access items."""
    visits = {
        "Mexico": {"Tulum", "Puerto Vallarta"},
        "Japan": {"Hakone"},
    }

    city_adder(visits, "Japan", "Kyoto")
    assert visits["Japan"] == {"Hakone", "Kyoto"}

    city_adder(visits, "France", "Paris")
    assert visits["France"] == {"Paris"}


def test_default_dict() -> None:
    """Use `defaultdict` when you do control the dictionary creation."""

    class Visits:
        """Track visits to cities in each country."""

        def __init__(self) -> None:
            self.data: Dict[str, Set[str]] = defaultdict(set)

        def add(self, country: str, city: str) -> None:
            """Add a `city` to the `country`."""
            self.data[country].add(city)

    visits = Visits()
    visits.add("Ethiopia", "Addis Ababa")
    visits.add("Ethiopia", "Dire Dawa")

    assert visits.data["Ethiopia"] == {"Addis Ababa", "Dire Dawa"}
