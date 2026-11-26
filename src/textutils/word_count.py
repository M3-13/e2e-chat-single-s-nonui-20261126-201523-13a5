"""word_count: count whitespace-separated words."""


def word_count(text: str) -> int:
    """Return the number of whitespace-separated words in ``text``.

    Raises TypeError if ``text`` is not a str. Runs in linear time.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    return len(text.split())
