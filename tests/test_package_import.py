"""The package is installed and exposes its public interface (AC-01)."""

import importlib
import importlib.metadata

import pytest

NAMES = ["slugify", "truncate", "word_count", "is_palindrome", "reverse_words"]


def test_all_five_names_import_from_textutils() -> None:
    from textutils import is_palindrome, reverse_words, slugify, truncate, word_count

    for func in (slugify, truncate, word_count, is_palindrome, reverse_words):
        assert callable(func)


@pytest.mark.parametrize("name", NAMES)
def test_name_is_exported_and_callable(name: str) -> None:
    module = importlib.import_module("textutils")
    assert name in module.__all__
    assert callable(getattr(module, name))


def test_all_lists_exactly_the_public_interface() -> None:
    module = importlib.import_module("textutils")
    assert sorted(module.__all__) == sorted(NAMES)


def test_package_is_installed() -> None:
    assert importlib.metadata.version("textutils")
