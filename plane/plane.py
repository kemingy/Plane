"""
Plane class
"""

import re
import sys
import unicodedata

from plane.pattern import (
    Regex,
    Token,
    DEFAULT_PATTERNS,
    ASCII_WORD,
)

PUNCTUATION = [c for c in range(sys.maxunicode) 
               if unicodedata.category(chr(c)).startswith('P')]
UNICODE_PUNCTUATION = dict(zip(PUNCTUATION, ' ' * len(PUNCTUATION)))

def build_regex(regex):
    if not isinstance(regex, list):
        regex = [regex]

    value = re.compile('|'.join('(?P<%s>%s)' % (p.name, p.pattern) 
                       for p in regex))

    return value


class Plane:
    def __init__(self):
        self._text = ''
        self._values = []

    @property
    def text(self):
        return self._text

    @property
    def values(self):
        return self._values

    def extract(self, regex, result=False):
        regex = build_regex(regex)
        values = []
        for mo in regex.finditer(self._text):
            name = mo.lastgroup
            value = mo.group(name)
            values.append(Token(name, value, mo.start(), mo.end()))

        if result:
            return values
        self._values.extend(values)
        return self

    def replace(self, regex, repl=None, result=False):
        repl = repl if repl is not None else regex.repl
        text, start = '', 0

        for t in self.extract(regex, result=True):
            text += self._text[start:t.start] + repl
            start = t.end
        text += self._text[start:]

        if result:
            return text
        self._text = text
        return self

    def update(self, text):
        if not isinstance(text, str):
            raise TypeError('Only support string.')

        self._text = text
        self._values = []
        return self

    def segment(self, regex=ASCII_WORD):
        regex = build_regex(regex)
        result, start = [], 0
        for t in regex.finditer(self._text):
            result.extend(
                [char for char in list(self._text[start:t.start()])
                      if char != ' '])
            result.append(self._text[t.start():t.end()])
            start = t.end()
        result.extend([char for char in list(self._text[start:]) if char != ' '])
        return result

    def remove_punctuation(self, repl=' '):
        if repl != ' ':
            return self._text.translate(dict(zip(PUNCTUATION, repl * len(PUNCTUATION))))
        return self._text.translate(UNICODE_PUNCTUATION)