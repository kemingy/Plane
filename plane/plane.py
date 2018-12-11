"""
Plane class, support chain function calls.
"""

import re
import sys
import unicodedata

from plane.pattern import Token, ASCII_WORD


PUNCTUATION = [c for c in range(sys.maxunicode)
               if unicodedata.category(chr(c)).startswith('P')]
UNICODE_PUNCTUATION = dict(zip(PUNCTUATION, ' ' * len(PUNCTUATION)))


class Plane:
    """
    Init :class:`Plane.text` and :class:`Plane.values` when the instance is
    created.
    """
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
        """
        :param Regex regex: :class:`Regex`
        :param bool result: if `True`, return result directly

        Extract tokens, results is saved in :class:`Plane.values`
        """
        regex = re.compile('(?P<%s>%s)' % (regex.name, regex.pattern))
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
        """
        :param Regex regex: :class:`Regex`
        :param str repl: replacement for regex, if setted, default value will \
        be overwritten
        :param bool result: if `True`, return result directly

        Replace matched :class:`regex` patterns with :class:`repl`.
        """
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
        """
        :param str text: text string.

        Init `Plane.text` and `Plane.values`.
        """
        if not isinstance(text, str):
            raise TypeError('Only support string.')

        self._text = text
        self._values = []
        return self

    def segment(self, regex=ASCII_WORD):
        """
        :param Regex regex: default regex is `ASCII_WORD`, this will keep all \
        english words complete

        Segment sentence.
        Chinese words will be split into char and English words will be keeped.
        """
        regex = re.compile('(?P<%s>%s)' % (regex.name, regex.pattern))
        result, start = [], 0
        for t in regex.finditer(self._text):
            result.extend(
                [char for char in list(self._text[start:t.start()])
                 if char != ' '])
            result.append(self._text[t.start():t.end()])
            start = t.end()
        result.extend([char for char in list(self._text[start:])
                       if char != ' '])
        return result

    def remove_punctuation(self, repl=' '):
        """
        :param str repl: replacement for regex, if setted, default value will \
        be overwritten

        remove all punctuations
        """
        if repl != ' ':
            self._text = self._text.translate(
                dict(zip(PUNCTUATION, repl * len(PUNCTUATION))))
        self._text = self._text.translate(UNICODE_PUNCTUATION)
        return self
