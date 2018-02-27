"""
Some chars are not include.
Such as:
    +
    ^
    $
    ~

You can use **pattern** to process these chars.
"""

import sys
import unicodedata

PUNCTUATION = [c for c in range(sys.maxunicode) if unicodedata.category(chr(c)).startswith('P')]

DEFAULT_REPLACER = ' '

UNICODE_PUNCTUATION = dict(zip(PUNCTUATION, DEFAULT_REPLACER * len(PUNCTUATION)))

def remove_punctuation(text, repl=DEFAULT_REPLACER):
    if repl != DEFAULT_REPLACER:
        return text.translate(dict(zip(PUNCTUATION, repl * len(PUNCTUATION))))
    return text.translate(UNICODE_PUNCTUATION)
