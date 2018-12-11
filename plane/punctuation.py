"""
Some chars are not included in punctuations.
Such as: `+`, `^`, `$`, `~`.
You can use :class:`Plane.pattern` to process these chars.
"""

import sys
import unicodedata

PUNCTUATION = [c for c in range(sys.maxunicode)
               if unicodedata.category(chr(c)).startswith('P')]

DEFAULT_REPLACER = ' '

UNICODE_PUNCTUATION = dict(zip(PUNCTUATION,
                               DEFAULT_REPLACER * len(PUNCTUATION)))


def remove_punctuation(text, repl=DEFAULT_REPLACER):
    """
    :param str text: input text

    Remove all punctuations.

    This methods use :class:`unicodedata`
    (https://docs.python.org/3.6/library/unicodedata.html) to get all
    the punctuations.
    """
    if repl != DEFAULT_REPLACER:
        return text.translate(dict(zip(PUNCTUATION, repl * len(PUNCTUATION))))
    return text.translate(UNICODE_PUNCTUATION)
