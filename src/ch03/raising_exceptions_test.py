"""Item 20.

Prefer Raising Exceptions to Returning `None`.
"""

import pytest


def test_raise_exception() -> None:
    """Raise exception instead of returning `None`."""

    def careful_divide(numerator: float, denominator: float) -> float:
        """Divide numerator by denominator.

        Raises ValueError when the inputs cannot be divided.
        """
        try:
            return numerator / denominator
        except ZeroDivisionError as zde:
            raise ValueError("Invalid inputs") from zde

    with pytest.raises(ValueError):
        careful_divide(3, 0)

    try:
        result = careful_divide(5, 2)
    except ValueError:
        pytest.fail("Should not raise an exception")
    else:
        assert result == 2.5
