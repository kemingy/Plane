"""
match, extract, remove parts of strings
"""

import re

from plane.pattern import (
    Regex,
    Token,
    DEFAULT_PATTERNS,
    ASCII_WORD,
)

PATTERNS = dict([p.name, p] for p in DEFAULT_PATTERNS)

def build_new_regex(name, regex, repl=''):
    name = name.replace(' ', '_')
    regex = Regex(name, regex, repl)
    PATTERNS[name] = regex
    return regex

def build_regex(regex):
    assert isinstance(regex, Regex)

    value = re.compile('(?P<%s>%s)' % (regex.name, regex.pattern))
    return value

def extract(text, pattern):
    regex = build_regex(pattern)
    for mo in regex.finditer(text):
        name = mo.lastgroup
        value = mo.group(name)
        yield Token(name, value, mo.start(), mo.end())

def replace(text, pattern, repl=None):
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
    regex = build_regex(pattern)
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
