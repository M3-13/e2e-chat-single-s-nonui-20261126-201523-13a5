import time

import pytest

from textutils import is_palindrome


def test_sentence_palindrome() -> None:
    assert is_palindrome("A man, a plan, a canal: Panama") is True


def test_case_insensitive() -> None:
    assert is_palindrome("Racecar") is True


def test_not_palindrome() -> None:
    assert is_palindrome("hello") is False


def test_empty_and_symbols() -> None:
    assert is_palindrome("") is True
    assert is_palindrome("!?, ...") is True


@pytest.mark.parametrize("bad", [None, 5, b"abc", ["a"]])
def test_type_error(bad: object) -> None:
    with pytest.raises(TypeError):
        is_palindrome(bad)


def test_large_symbol_input_is_fast() -> None:
    start = time.perf_counter()
    assert is_palindrome("!" * 100_000) is True
    assert time.perf_counter() - start < 1
