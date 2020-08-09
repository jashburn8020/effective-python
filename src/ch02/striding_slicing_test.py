"""Item 12.

Avoid Striding and Slicing in a Single Expression.
"""

import pytest


def test_reverse_stride_unicode() -> None:
    """Reverse Unicode strings by negative striding."""
    unicode = "你好"
    assert unicode[::-1] == "好你"

    utf8 = unicode.encode("utf-8")
    with pytest.raises(UnicodeDecodeError):
        utf8[::-1].decode("utf-8")
