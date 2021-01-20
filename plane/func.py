"""
Basic :meth:`match`, :meth:`extract`, :meth:`segment` function.
"""

import re

from plane.pattern import ASCII_WORD, DEFAULT_PATTERNS, Regex, Token


def build_new_regex(name, regex, flag=0, repl=" "):
    """
    :param str name: regex pattern name
    :param str regex: regex
    :param str repl: replacement

    build regex pattern, space :code:`' '` in name will be replaced by
    :code:`'_'`
    """
    name = name.replace(" ", "_")
    regex = Regex(name, regex, flag, repl)
    PATTERNS[name] = compile_regex(regex)
    return regex


def compile_regex(regex):
    assert isinstance(regex, Regex)
    expression = re.compile("(?P<%s>%s)" % (regex.name, regex.pattern), regex.flag)
    return expression


PATTERNS = dict([p.name, compile_regex(p)] for p in DEFAULT_PATTERNS)


def extract(text, regex):
    """
    :param str text: text
    :param Regex pattern: :class:`plane.pattern.Regex`

    Extract tokens with regex pattern.
    """
    regex = PATTERNS.get(regex.name, compile_regex(regex))
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
    result = ""
    start = 0
    repl = repl if repl is not None else pattern.repl
    for t in tokens:
        result += text[start : t.start] + repl
        start = t.end
    result += text[start:]

    return result


def segment(text, regex=ASCII_WORD):
    """
    :param str text: text
    :param Regex pattern: :class:`plane.pattern.Regex`

    Segment sentence.
    Chinese words will be split into char and English words will be keeped.
    """
    regex = PATTERNS.get(regex.name, compile_regex(regex))
    result = []
    start = 0
    for t in regex.finditer(text):
        result.extend([char for char in list(text[start : t.start()]) if char != " "])
        result.append(text[t.start() : t.end()])
        start = t.end()
    result.extend([char for char in list(text[start:]) if char != " "])
    return result
