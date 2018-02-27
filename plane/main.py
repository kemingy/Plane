"""
match, extract, remove parts of strings
"""

import re

from .pattern import (
    Regex,
    Token,
    EMAIL,
    SPACE,
    TELEPHONE,
    RESTRICT_URL,
)

DEFAULT_PATTERN = [
    EMAIL,
    SPACE,
    TELEPHONE,
    RESTRICT_URL,
]

def add_new_pattern(name, regex, repl=''):
    DEFAULT_PATTERN.append(
        Regex(name, regex, repl)
    )

def build_regex(patterns):
    return '|'.join('(?P<%s>%s)' % (p.name, p.pattern) for p in patterns)

def match(text, patterns):
    pass

def extract(text, patterns):
    regex = build_regex(patterns)
    for mo in re.finditer(regex, text):
        name = mo.lastgroup
        value = mo.group(name)
        yield Token(name, value, mo.start(), mo.end())

def replace(text, patterns):
    tokens = list(extract(text, patterns))
    for t in tokens[::-1]:
        text[t.start : t.end] = '<%s>' % t.name

    return text