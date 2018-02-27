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

def remove_punctuation(text, replacer=DEFAULT_REPLACER):
    if replacer != DEFAULT_REPLACER:
        return text.translate(dict(zip(PUNCTUATION, replacer * len(PUNCTUATION))))
    return text.translate(UNICODE_PUNCTUATION)
