import time

import pytest

from textutils import word_count


def test_counts_words_across_whitespace():
    assert word_count("one two  three\nfour") == 4


def test_tabs_and_newlines():
    assert word_count("a\tb\nc") == 3


def test_empty_and_whitespace_only():
    assert word_count("") == 0
    assert word_count("   ") == 0


@pytest.mark.parametrize("bad", [None, 5, b"a b", ["a"]])
def test_non_str_raises_type_error(bad):
    with pytest.raises(TypeError):
        word_count(bad)


def test_large_whitespace_input_is_fast():
    text = " " * 100_000
    start = time.perf_counter()
    assert word_count(text) == 0
    assert time.perf_counter() - start < 1
