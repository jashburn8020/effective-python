"""Item 10.

Prevent Repetition with Assignment Expressions.
"""

from enum import Enum
from typing import Dict


def test_walrus() -> None:
    """Use the walrus operator to approximate switch-case."""
    Fruit = Enum("Fruit", "APPLE, BANANA, LEMON")

    def make_smoothie(num: int) -> int:
        return num // 2

    def make_cider(num: int) -> int:
        return num // 4

    def make_lemonade(num: int) -> int:
        return num

    def to_enjoy_if_else(basket: Dict[Fruit, int]) -> int:
        count = basket.get(Fruit.BANANA, 0)
        if count >= 2:
            to_enjoy = make_smoothie(count)
        else:
            count = basket.get(Fruit.APPLE, 0)
            if count >= 4:
                to_enjoy = make_cider(count)
            else:
                count = basket.get(Fruit.LEMON, 0)
                if count:
                    to_enjoy = make_lemonade(count)
                else:
                    to_enjoy = 0

        return to_enjoy

    def to_enjoy_walrus(basket: Dict[Fruit, int]) -> int:
        if (count := basket.get(Fruit.BANANA, 0)) >= 2:
            return make_smoothie(count)
        if (count := basket.get(Fruit.APPLE, 0)) >= 4:
            return make_cider(count)
        if count := basket.get(Fruit.LEMON, 0):
            return make_lemonade(count)
        return 0

    fruits = {Fruit.APPLE: 10, Fruit.BANANA: 8, Fruit.LEMON: 5}
    assert to_enjoy_if_else(fruits) == to_enjoy_walrus(fruits) == 4

    fruits = {Fruit.APPLE: 10, Fruit.BANANA: 0, Fruit.LEMON: 5}
    assert to_enjoy_if_else(fruits) == to_enjoy_walrus(fruits) == 2

    fruits = {Fruit.APPLE: 3, Fruit.LEMON: 5}
    assert to_enjoy_if_else(fruits) == to_enjoy_walrus(fruits) == 5
