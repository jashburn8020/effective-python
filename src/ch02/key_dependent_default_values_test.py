"""Item 18.

Know How to Construct Key-Dependent Default Values with `__missing__`.
"""

from typing import Dict


def test_missing() -> None:
    """Use `__missing__` method to create default values."""

    class Keys(Dict[str, str]):
        """Map string keys to arbitrary strings.

        Return the key in uppercase as the value by default.
        """

        # Note: It appears that pylint returns false positive unsubscriptable-object
        # when subclassing Dict.
        # https://github.com/PyCQA/pylint/issues/3129

        def __missing__(self, key: str) -> str:
            value = key.upper()
            self[key] = value
            return value

    keys = Keys()
    assert keys["a"] == "A"
    assert keys["CTRL-a"] == "CTRL-A"

    keys["b"] = "CTRL-b"
    assert keys["b"] == "CTRL-b"
