import time

import pytest

from textutils import reverse_words


def test_reverses_and_collapses_whitespace() -> None:
    assert reverse_words("one two  three") == "three two one"


def test_strips_outer_whitespace() -> None:
    assert reverse_words("  hi  ") == "hi"


def test_empty_string() -> None:
    assert reverse_words("") == ""


def test_any_whitespace_separates() -> None:
    assert reverse_words("a\tb\nc") == "c b a"


@pytest.mark.parametrize("bad", [None, 5, b"x", ["a"]])
def test_non_str_raises_type_error(bad: object) -> None:
    with pytest.raises(TypeError):
        reverse_words(bad)


def test_large_whitespace_input_is_fast() -> None:
    start = time.perf_counter()
    assert reverse_words(" " * 100_000) == ""
    assert time.perf_counter() - start < 1
