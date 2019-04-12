"""
Plane class, support chain function calls.
"""

from plane.pattern import Token, ASCII_WORD
from plane.punctuation import punc
from plane.func import compile_regex


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
        regex = compile_regex(regex)
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
        regex = compile_regex(regex)
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
        self._text = punc.remove(self._text, repl)
        return self

    def normalize_punctuation(self):
        """
        normalize punctuations to English punctuations
        """
        self._text = punc.normalize(self.text)
        return self
