"""Item 6 and item 7.

Prefer Multiple Assignment Unpacking Over Indexing.
Prefer enumerate Over range.
"""

from typing import List


def test_unpack_for_loop() -> None:
    """Unpack `for` loops and similar constructs."""
    snacks = [("bacon", 350), ("donut", 240)]
    exp_calorie_stmts = ["#1: bacon has 350 calories", "#2: donut has 240 calories"]

    calorie_stmts: List[str] = []
    for i in range(len(snacks)):
        item = snacks[i]
        name = item[0]
        calories = item[1]
        calorie_stmts.append(f"#{i+1}: {name} has {calories} calories")

    assert calorie_stmts == exp_calorie_stmts

    calorie_stmts_unpack: List[str] = []
    for rank, (name, calories) in enumerate(snacks, 1):
        calorie_stmts_unpack.append(f"#{rank}: {name} has {calories} calories")

    assert calorie_stmts_unpack == exp_calorie_stmts

    assert [
        f"#{rank}: {name} has {calories} calories"
        for rank, (name, calories) in enumerate(snacks, 1)
    ] == exp_calorie_stmts
