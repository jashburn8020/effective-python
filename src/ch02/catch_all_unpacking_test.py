"""Item 13.

Prefer Catch-All Unpacking Over Slicing.
"""


def test_catch_all_slicing() -> None:
    """Catch-all by slicing."""
    ages_desc = [20, 19, 15, 9, 8]
    oldest = ages_desc[0]
    older = ages_desc[1]
    others = ages_desc[2:]
    assert (oldest, older, others) == (20, 19, [15, 9, 8])


def test_catch_all_starred_expression() -> None:
    """Catch-all using starred expression."""
    ages_desc = [20, 19, 15, 9, 8]
    oldest, older, *others = ages_desc
    assert (oldest, older, others) == (20, 19, [15, 9, 8])

    oldest, *others, youngest = ages_desc
    assert (oldest, others, youngest) == (20, [19, 15, 9], 8)

    *others, younger, youngest = ages_desc
    assert (others, younger, youngest) == ([20, 19, 15], 9, 8)
