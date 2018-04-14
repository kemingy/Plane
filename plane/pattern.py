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

ASCII_WORD = Regex(
    'ASCII_word',
    r'[<$#&]?[a-zA-Z0-9_.-]*\'?[a-zA-Z0-9]+[%>]?',
    ' ',
)

CHINESE = Regex(
    'Chinese',
    r'[' + \
    ''.join([r'\U{:0>8X}-\U{:0>8X}'.format(begin, end) for begin, end in [
        (0x4E00, 0x9FFF),       # CJK Unified Ideographs
        (0x3400, 0x4DBF),       # CJK Unified Ideographs Extension A
        (0x20000, 0x2A6DF),     # CJK Unified Ideographs Extension B
        (0x2A700, 0x2B73F),     # CJK Unified Ideographs Extension C
        (0x2B740, 0x2B81F),     # CJK Unified Ideographs Extension D
        (0x2B820, 0x2CEAF),     # CJK Unified Ideographs Extension E
        (0x2CEB0, 0x2EBEF),     # CJK Unified Ideographs Extension F
        (0x3000, 0x303F),       # CJK Symbols and Punctuation
        (0xFE30, 0xFE4F),       # CJK Compatibility Forms
        (0xFF00, 0xFFEF),       # Halfwidth and Fullwidth Forms
    ]]) + r']+',
    ' ',
)

CJK = Regex(
    'CJK',
    r'[' + \
    ''.join([r'\U{:0>8X}-\U{:0>8X}'.format(begin, end) for begin, end in [
        (0x4E00, 0x9FFF),       # CJK Unified Ideographs
        (0x3400, 0x4DBF),       # CJK Unified Ideographs Extension A
        (0x20000, 0x2A6DF),     # CJK Unified Ideographs Extension B
        (0x2A700, 0x2B73F),     # CJK Unified Ideographs Extension C
        (0x2B740, 0x2B81F),     # CJK Unified Ideographs Extension D
        (0x2B820, 0x2CEAF),     # CJK Unified Ideographs Extension E
        (0x2CEB0, 0x2EBEF),     # CJK Unified Ideographs Extension F
        (0x2E80, 0x2EFF),       # CJK Radicals Supplement
        (0x2F00, 0x2FDF),       # Kangxi Radicals
        (0x2FF0, 0x2FFF),       # Ideographic Description Characters
        (0x3000, 0x303F),       # CJK Symbols and Punctuation
        (0x31C0, 0x31EF),       # CJK Strokes
        (0x3200, 0x32FF),       # Enclosed CJK Letters and Months
        (0x3300, 0x33FF),       # CJK Compatibility
        (0xF900, 0xFAFF),       # CJK Compatibility Ideographs
        (0xFE30, 0xFE4F),       # CJK Compatibility Forms
        (0xFF00, 0xFFEF),       # Halfwidth and Fullwidth Forms
        (0x1F200, 0x1F2FF),     # Enclosed Ideographic Supplement
        (0x2F800, 0x2FA1F),     # CJK Compatibility Ideographs Supplement
    ]]) + r']+',
    ' ',
)

DEFAULT_PATTERNS = [
    HTML,
    EMAIL,
    SPACE,
    TELEPHONE,
    RESTRICT_URL,
    ASCII_WORD,
    CHINESE,
    CJK,
]
