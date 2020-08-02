"""Item 5.

Write Helper Functions Instead of Complex Expressions.
"""

from urllib.parse import parse_qs
from typing import Dict, List


def test_parse_query_string_complex() -> None:
    """Parse query string to obtain `int`s - complex expressions."""
    my_values = parse_qs("red=5&blue=0&green=", keep_blank_values=True)

    # We want all parameter values to be converted to integers
    assert my_values.get("red") == ["5"]
    assert my_values.get("green") == [""]
    assert my_values.get("opacity") is None

    # Complex
    assert int(my_values.get("red", [""])[0] or 0) == 5
    assert int(my_values.get("green", [""])[0] or 0) == 0
    assert int(my_values.get("opacity", [""])[0] or 0) == 0

    # Clearer, but can be better
    red_str = my_values.get("red", [""])
    assert int(red_str[0]) if red_str[0] else 0 == 5

    green_str = my_values.get("green", [""])
    assert int(green_str[0]) if green_str[0] else 0 == 0

    opacity_str = my_values.get("opacity", [""])
    assert int(opacity_str[0]) if opacity_str[0] else 0 == 0


def test_parse_query_string_helper() -> None:
    """Parse query string to obtain `int`s - helper function."""

    def get_first_int(values: Dict[str, List[str]], key: str, default: int = 0) -> int:
        found = values.get(key, [""])
        if found[0]:
            return int(found[0])

        return default

    my_values = parse_qs("red=5&blue=0&green=", keep_blank_values=True)

    assert get_first_int(my_values, "red") == 5
    assert get_first_int(my_values, "green") == 0
    assert get_first_int(my_values, "opacity") == 0
