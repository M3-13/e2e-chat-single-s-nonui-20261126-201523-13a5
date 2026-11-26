import pytest

from textutils import truncate


def test_short_text_unchanged():
    assert truncate("Hello World", 20) == "Hello World"
    assert truncate("Hello", 5) == "Hello"


def test_truncates_with_suffix():
    result = truncate("Hello World", 8)
    assert result == "Hello..."
    assert len(result) == 8


def test_max_len_smaller_than_suffix():
    assert truncate("Hello", 2) == ".."
    assert truncate("Hello", 0) == ""


def test_custom_suffix():
    assert truncate("Hello World", 7, suffix="~") == "Hello ~"


def test_negative_max_len_raises():
    with pytest.raises(ValueError):
        truncate("x", -1)


@pytest.mark.parametrize("bad", [None, 5, b"x", ["a"]])
def test_non_str_text_raises(bad):
    with pytest.raises(TypeError):
        truncate(bad, 5)


@pytest.mark.parametrize("bad", [True, False, 1.5, "3", None])
def test_bad_max_len_type_raises(bad):
    with pytest.raises(TypeError):
        truncate("Hello", bad)


def test_length_bound():
    text = "abcdefghij"
    for n in range(0, 15):
        for suffix in ("", ".", "...", "-----------"):
            out = truncate(text, n, suffix)
            assert len(out) <= n
            assert len(out) <= max(len(text), len(suffix))
