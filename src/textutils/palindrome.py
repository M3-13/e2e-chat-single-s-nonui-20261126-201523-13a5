"""is_palindrome: check whether text reads the same in both directions."""


def is_palindrome(text: str) -> bool:
    """Return True if ``text`` is a palindrome, ignoring case and non-alphanumerics.

    Empty or symbol-only text is a palindrome. Runs in linear time.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    chars = [c.casefold() for c in text if c.isalnum()]
    return chars == chars[::-1]
