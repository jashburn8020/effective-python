"""Item 4.

Prefer Interpolated F-Strings Over C-style Format Strings and str.format.
"""

import pytest


def test_c_printf_style_change_order() -> None:
    """C printf-style string formatting.

    Change order of data values.
    """
    key = "my_var"
    value = 1.234
    formatted = "%-10s = %.2f" % (key, value)
    assert formatted == "my_var     = 1.23"

    with pytest.raises(TypeError):
        formatted = "%-10s = %.2f" % (value, key)


def test_c_printf_style_small_modifications() -> None:
    """C printf-style string formatting.

    Make small modifications to values before formatting them.
    """
    item_number = 0
    fruit = "avocados"
    count = 1.25
    price = 1.05

    formatted = "#%d: %s (£%.2f): %.2f" % (item_number, fruit, price, count)
    assert formatted == "#0: avocados (£1.05): 1.25"

    formatted = "#%d: %s (£%.2f): %d" % (
        item_number + 1,
        fruit.title(),
        price,
        round(count),
    )
    assert formatted == "#1: Avocados (£1.05): 1"


def test_c_printf_style_dictionary() -> None:
    """C printf-style string formatting.

    Use a dictionary instead of a tuple.
    """
    item = {
        "item_number": 0,
        "fruit": "avocados",
        "count": 1.25,
        "price": 1.05,
    }

    formatted = "#%(item_number)d: %(fruit)s (£%(price).2f): %(count).2f" % item
    assert formatted == "#0: avocados (£1.05): 1.25"


def test_format_small_modifications() -> None:
    """`format` method string formatting.

    Make small modifications to values before formatting them.
    """
    item_number = 0
    fruit = "avocados"
    count = 1.25
    price = 1.05

    formatted = "#{}: {} (£{:.2f}): {}".format(
        item_number + 1, fruit.title(), price, round(count),
    )
    assert formatted == "#1: Avocados (£1.05): 1"


def test_f_string_small_modifications() -> None:
    """F-string interpolation."""
    item_number = 0
    fruit = "avocados"
    count = 1.25
    price = 1.05

    formatted = f"#{item_number + 1}: {fruit.title()} (£{price:.2f}): {round(count)}"
    assert formatted == "#1: Avocados (£1.05): 1"
