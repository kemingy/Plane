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

DEFAULT_PATTERNS = [
    HTML,
    EMAIL,
    SPACE,
    TELEPHONE,
    RESTRICT_URL,
]
