"""slugify: turn arbitrary text into a URL-friendly slug."""

import unicodedata


def slugify(text: str) -> str:
    """Return a lowercase, ASCII, hyphen-separated slug of ``text``.

    Accents are removed (NFKD), 'ß' becomes 'ss', and every run of characters
    that are not ASCII letters or digits collapses into a single hyphen.
    Leading and trailing hyphens are stripped. Runs in linear time.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    normalized = unicodedata.normalize("NFKD", text.lower().replace("ß", "ss"))
    parts: list[str] = []
    pending_sep = False
    for ch in normalized:
        if ch.isascii() and ch.isalnum():
            if pending_sep and parts:
                parts.append("-")
            pending_sep = False
            parts.append(ch)
        else:
            # Combining marks left over from NFKD are dropped silently.
            if not unicodedata.combining(ch):
                pending_sep = True
    return "".join(parts)
