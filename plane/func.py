"""
Basic :meth:`match`, :meth:`extract`, :meth:`segment` function.
"""

import re

from plane.pattern import (
    Regex,
    Token,
    DEFAULT_PATTERNS,
    ASCII_WORD,
)

PATTERNS = dict([p.name, p] for p in DEFAULT_PATTERNS)


def build_new_regex(name, regex, flag=0, repl=' '):
    """
    :param str name: regex pattern name
    :param str regex: regex
    :param str repl: replacement

    build regex pattern, space :code:`' '` in name will be replaced by
    :code:`'_'`
    """
    name = name.replace(' ', '_')
    regex = Regex(name, regex, flag, repl)
    PATTERNS[name] = regex
    return regex


def compile_regex(regex):
    assert isinstance(regex, Regex)
    expression = re.compile('(?P<%s>%s)' % (regex.name, regex.pattern),
                            regex.flag)
    return expression


def extract(text, pattern):
    """
    :param str text: text
    :param Regex pattern: :class:`plane.pattern.Regex`

    Extract tokens with regex pattern.
    """
    regex = compile_regex(pattern)
    for mo in regex.finditer(text):
        name = mo.lastgroup
        value = mo.group(name)
        yield Token(name, value, mo.start(), mo.end())


def replace(text, pattern, repl=None):
    """
    :param str text: text
    :param Regex pattern: :class:`plane.pattern.Regex`
    :param str repl: replacement for pattern, if setted, default `repl` \
    will be overwritten

    Replace matched tokens with `repl`.
    """
    tokens = extract(text, pattern)
    result = ''
    start = 0
    repl = repl if repl is not None else pattern.repl
    for t in tokens:
        result += text[start:t.start] + repl
        start = t.end
    result += text[start:]

    return result


def segment(text, pattern=ASCII_WORD):
    """
    :param str text: text
    :param Regex pattern: :class:`plane.pattern.Regex`

    Segment sentence.
    Chinese words will be split into char and English words will be keeped.
    """
    regex = compile_regex(pattern)
    result = []
    start = 0
    for t in regex.finditer(text):
        result.extend(
            [char for char in list(text[start:t.start()])
                if char != ' '])
        result.append(text[t.start():t.end()])
        start = t.end()
    result.extend([char for char in list(text[start:]) if char != ' '])
    return result
