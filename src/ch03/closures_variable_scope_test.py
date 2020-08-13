"""Item 21.

Know How Closures Interact with Variable Scope.
"""

from typing import Set, Tuple


def test_sort_not_found() -> None:
    """Variable does not exist in the current scope."""
    numbers = [8, 3, 1, 2, 4]
    group = {2, 3, 5, 7}

    found = False

    def sort_key(elem: int) -> Tuple[int, int]:
        if elem in group:
            # `found` does not exist in the current scope; the assignment is treated as
            # a variable definition, scoped within this function.
            found = True
            return (0, elem)
        return (1, elem)

    numbers.sort(key=sort_key)

    assert numbers == [2, 3, 1, 4, 8]
    assert not found


def test_sort_found() -> None:
    """Use `nonlocal` to traverse scope upon assignment for a variable."""
    numbers = [8, 3, 1, 2, 4]
    group = {2, 3, 5, 7}

    found = False

    def sort_key(elem: int) -> Tuple[int, int]:
        nonlocal found
        if elem in group:
            found = True
            return (0, elem)
        return (1, elem)

    numbers.sort(key=sort_key)

    assert numbers == [2, 3, 1, 4, 8]
    assert found


def test_sort_class() -> None:
    """Wrap state in a helper class."""

    class Sorter:
        def __init__(self, group: Set[int]) -> None:
            self.group = group
            self.found = False

        def __call__(self, elem: int) -> Tuple[int, int]:
            if elem in group:
                self.found = True
                return (0, elem)
            return (1, elem)

    numbers = [8, 3, 1, 2, 4]
    group = {2, 3, 5, 7}
    sorter = Sorter(group)
    numbers.sort(key=sorter)

    assert numbers == [2, 3, 1, 4, 8]
    assert sorter.found
