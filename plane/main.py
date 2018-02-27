"""
match, extract, remove parts of strings
"""

import re

from .pattern import (
    Regex,
    Token,
    DEFAULT_PATTERNS,
)

PATTERNS = dict([p.name, p] for p in DEFAULT_PATTERNS)

def add_new_pattern(name, regex, repl=''):
    PATTERNS[name] = Regex(name, regex, repl)

def build_regex(patterns):
    if not isinstance(patterns, list):
        patterns = [patterns]

    return '|'.join('(?P<%s>%s)' % (p.name, p.pattern) for p in patterns)

def extract(text, patterns):
    regex = build_regex(patterns)
    for mo in re.finditer(regex, text):
        name = mo.lastgroup
        value = mo.group(name)
        yield Token(name, value, mo.start(), mo.end())

def replace(text, patterns):
    tokens = extract(text, patterns)
    result = ''
    start = 0
    for t in tokens:
        result += text[start:t.start] + PATTERNS[t.name].repl
        start = t.end
    result += text[start:]

    return result