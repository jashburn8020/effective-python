"""Item 8.

Use `zip` to Process Iterators in Parallel.
"""
from typing import List, Optional, Tuple

import pytest


@pytest.fixture(name="names_counts")
def fixture_names_counts() -> Tuple[List[str], List[int]]:
    """Return a list of names."""
    names = ["Ekon", "Kwame", "Feechi"]
    return (names, [len(name) for name in names])


def test_longest_name(names_counts: Tuple[List[str], List[int]]) -> None:
    """Get the longest name."""
    names, counts = names_counts

    longest_name: Optional[str] = None
    max_count = 0

    for i in range(len(names)):
        count = counts[i]
        if count > max_count:
            longest_name = names[i]
            max_count = count

    assert longest_name == "Feechi"


def test_longest_name_zip(names_counts: Tuple[List[str], List[int]]) -> None:
    """Get the longest name using `zip`."""
    names, counts = names_counts

    longest_name: Optional[str] = None
    max_count = 0

    for name, count in zip(names, counts):
        if count > max_count:
            longest_name = name
            max_count = count

    assert longest_name == "Feechi"
