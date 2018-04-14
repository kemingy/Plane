"""
match, extract, remove parts of strings
"""

import re

from .pattern import (
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

def segment(text, patterns=ASCII_WORD):
    regex = build_regex(patterns)
    print(regex)
    result = []
    start = 0
    for t in re.finditer(regex, text):
        result.extend(
            [char for char in list(text[start:t.start()])
                if char != ' '])
        result.append(text[t.start():t.end()])
        start = t.end()
    result.extend([char for char in list(text[start:]) if char != ' '])
    return result
