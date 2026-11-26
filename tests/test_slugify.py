import time

import pytest

from textutils import slugify


def test_basic() -> None:
    assert slugify("Hello, World!") == "hello-world"


def test_accents() -> None:
    assert slugify("  Crème Brûlée  ") == "creme-brulee"


def test_sharp_s() -> None:
    assert slugify("Straße") == "strasse"


def test_empty_and_symbols_only() -> None:
    assert slugify("") == ""
    assert slugify("---") == ""


def test_collapses_runs() -> None:
    assert slugify("a  --  b___c") == "a-b-c"


@pytest.mark.parametrize("bad", [None, 5, b"x", ["a"]])
def test_type_error(bad: object) -> None:
    with pytest.raises(TypeError):
        slugify(bad)


@pytest.mark.parametrize("ch", [" ", "!", "-"])
def test_large_input_is_fast(ch: str) -> None:
    start = time.perf_counter()
    assert slugify(ch * 100_000) == ""
    assert time.perf_counter() - start < 1
