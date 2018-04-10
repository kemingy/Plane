"""
All regex patterns.

"""

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
    r'([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+)',
    '<Email>',
)

TELEPHONE = Regex(
    'Telephone',
    r'(\d{3})[ +.-]?(\d{4})[ +.-]?(\d{4})',
    '<Telephone>',
)

SPACE = Regex(
    'Space',
    r'(\s+)',
    ' ',
)

HTML= Regex(
    'HTML',
    r'(?s)<script.*?>.*?</script>|<style.*?>.*?</style>|<.*?>',
    ' ',
)

CHINESE = Regex(
    'Chinese',
    r'[' + \
    ''.join([r'\U{:0>8X}-\U{:0>8X}'.format(begin, end) for begin, end in [
        (0x4E00, 0x9FFF),
        (0x3400, 0x4DBF),
        (0x20000, 0x2A6DF),
        (0x2A700, 0x2B73F),
        (0x2B740, 0x2B81F),
        (0x2B820, 0x2CEAF),
        (0x2CEB0, 0x2EBEF),
    ]]) + r']',
    ' ',
)

CJK = Regex(
    'CJK',
    r'[' + \
    ''.join([r'\U{:0>8X}-\U{:0>8X}'.format(begin, end) for begin, end in [
        (0x4E00, 0x9FFF),
        (0x3400, 0x4DBF),
        (0x20000, 0x2A6DF),
        (0x2A700, 0x2B73F),
        (0x2B740, 0x2B81F),
        (0x2B820, 0x2CEAF),
        (0x2CEB0, 0x2EBEF),
        (0x2E80, 0x2EFF),
        (0x2F00, 0x2FDF),
        (0x2FF0, 0x2FFF),
        (0x3000, 0x303F),
        (0x31C0, 0x31EF),
        (0x3200, 0x32FF),
        (0x3300, 0x33FF),
        (0xF900, 0xFAFF),
        (0xFE30, 0xFE4F),
        (0xFF00, 0xFFEF),
        (0x1F200, 0x1F2FF),
        (0x2F800, 0x2FA1F),
    ]]) + r']',
    ' ',
)

DEFAULT_PATTERNS = [
    HTML,
    EMAIL,
    SPACE,
    TELEPHONE,
    RESTRICT_URL,
    CHINESE,
    CJK,
]
