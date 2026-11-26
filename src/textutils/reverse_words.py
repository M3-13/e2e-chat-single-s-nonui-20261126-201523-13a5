"""reverse_words: reverse the order of the words in a text."""


def reverse_words(text: str) -> str:
    """Return the words of ``text`` in reverse order, separated by single spaces.

    Words are separated by any run of whitespace; leading and trailing
    whitespace is dropped. Runs in linear time.

    Raises:
        TypeError: if ``text`` is not a ``str``.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    return " ".join(reversed(text.split()))
