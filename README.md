# textutils

`textutils` ist eine kleine Python-Bibliothek mit fünf unabhängigen String-Hilfsfunktionen: `slugify`, `truncate`, `word_count`, `is_palindrome` und `reverse_words`. Die Bibliothek hat keine Laufzeit-Abhängigkeiten und nutzt ausschließlich die Standardbibliothek.

## Technik

- Python 3.10 oder neuer
- Paketierung mit `pyproject.toml` (src-Layout)
- Tests mit `pytest`, Lint mit `ruff`
- Keine Laufzeit-Abhängigkeiten

## Installation

```bash
pip install -e .
```

Mit den Entwicklungswerkzeugen (pytest und ruff):

```bash
pip install -e .[dev]
```

## Verwendung

Alle Funktionen werden direkt aus dem Paket importiert:

```python
from textutils import slugify, truncate, word_count, is_palindrome, reverse_words
```

Jede Funktion löst einen `TypeError` aus, wenn `text` kein `str` ist.

### `slugify(text: str) -> str`

Wandelt Text in einen URL-freundlichen Slug um (Kleinbuchstaben, ASCII, Bindestriche).

```python
slugify("Hello, World!")  # 'hello-world'
slugify("  Crème Brûlée  ")  # 'creme-brulee'
slugify("---")  # ''
```

### `truncate(text: str, max_len: int, suffix: str = "...") -> str`

Kürzt Text auf höchstens `max_len` Zeichen und hängt dabei `suffix` an. Ein negatives `max_len` löst einen `ValueError` aus, ein Wert, der kein `int` ist (auch `bool`), einen `TypeError`.

```python
truncate("Hello World", 20)  # 'Hello World'
truncate("Hello World", 8)  # 'Hello...'
truncate("Hello", 2)  # '..'
```

### `word_count(text: str) -> int`

Zählt die durch Leerraum getrennten Wörter.

```python
word_count("one two  three\nfour")  # 4
word_count("   ")  # 0
```

### `is_palindrome(text: str) -> bool`

Prüft, ob der Text vorwärts und rückwärts gleich gelesen wird. Groß-/Kleinschreibung und Zeichen, die keine Buchstaben oder Ziffern sind, werden ignoriert.

```python
is_palindrome("A man, a plan, a canal: Panama")  # True
is_palindrome("hello")  # False
```

### `reverse_words(text: str) -> str`

Kehrt die Reihenfolge der Wörter um; die Wörter werden durch je ein Leerzeichen getrennt.

```python
reverse_words("one two  three")  # 'three two one'
reverse_words("  hi  ")  # 'hi'
```

## Tests und Lint

```bash
pytest
ruff check
```

## Funktionen

- `slugify` – URL-freundliche Slugs
- `truncate` – Text auf eine maximale Länge kürzen
- `word_count` – Wörter zählen
- `is_palindrome` – Palindrom-Prüfung
- `reverse_words` – Wortreihenfolge umkehren
