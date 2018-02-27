"""
All regex patterns.

"""
import sys
import unicodedata
from collections import namedtuple

Regex = namedtuple(
    'Regex',
    [
        'name',
        'pattern',
        'repl',
    ]
)

Token = namedtuple(
    'Token',
    [
        'name',
        'value',
        'start',
        'end',
    ]
)

# regex expression

RESTRICT_URL = Regex(
    'URL',
    r'(?i)https?:\/\/[!-~]+',
    '<URL>',
)

EMAIL = Regex(
    'Email',
    r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)',
    '<Email>',
)

TELEPHONE = Regex(
    'Phone',
    r'(\d{3})[ +.-]?(\d{4})[ +.-]?(\d{4})',
    '<Phone>',
)

SPACE = Regex(
    'Space',
    r'(\s+)',
    '<Space>',
)

# function

PUNCTUATION = [c for c in range(sys.maxunicode) if unicodedata.category(chr(c)).startswith('P')]

DEFAULT_REPLACER = ' '

UNICODE_PUNCTUATION = dict(zip(PUNCTUATION, DEFAULT_REPLACER * len(PUNCTUATION)))

def remove_punctuation(text, replacer=DEFAULT_REPLACER):
    if replacer != DEFAULT_REPLACER:
        return text.translate(dict(zip(PUNCTUATION, replacer * len(PUNCTUATION))))
    return text.translate(UNICODE_PUNCTUATION)
