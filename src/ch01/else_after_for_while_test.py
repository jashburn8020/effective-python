"""Item 9.

Avoid `else` Blocks After `for` and `while` Loops.
"""


def test_coprime_else() -> None:
    """Test if 2 numbers are coprime, using `else`."""
    a = 4
    b = 9
    coprime = False

    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            break
    else:
        coprime = True

    assert coprime


def test_coprime_helper() -> None:
    """Test if 2 numbers are coprime, using a helper function."""

    def is_coprime(a: int, b: int) -> bool:
        """Return `True` if `a` and `b` are coprime."""
        for i in range(2, min(a, b) + 1):
            if a % i == 0 and b % i == 0:
                return False
        return True

    assert is_coprime(4, 9)
    assert not is_coprime(3, 9)
