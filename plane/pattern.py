from collections import namedtuple
import re


class Regex(namedtuple(
    'Regex',
    [
        'name',
        'pattern',
        'flag',
        'repl',
    ]
)):
    """
    :param str name: regex name
    :param str pattern: Python regex
    :param str repl: replaement

    regex pattern
    """
    __slots__ = ()

    def __new__(cls, name, pattern, flag=0, repl=' '):
        return super(Regex, cls).__new__(cls, name, pattern, flag, repl)

    def __add__(self, other):
        """This method should only be used for language range.

        :param :class:`.Regex` other: another Regex instance
        """
        if isinstance(other, Regex):
            return Regex(
                '{}_{}'.format(self.name, other.name),
                '{}|{}'.format(self.pattern, other.pattern),
                self.flag | other.flag,
                self.repl if self.repl == other.repl else '{}_{}'
                    .format(self.repl, other.repl)
            )
        return self

    def __radd__(self, other):
        """Trait `sum`
        """
        return self.__add__(other)


class Token(namedtuple(
    'Token',
    [
        'name',
        'value',
        'start',
        'end',
    ]
)):
    """
    :param str name: token name
    :param str value: matched text
    :param int start: matched text started index
    :param int end: matched text ended index

    matched token
    """


#: URLs should begin with :code:`http` or :code:`https`.
#:
#: Only support ASCII chars.
URL = Regex(
    'URL',
    r'https?:\/\/[!-~]+',
    re.I,
    '<URL>',
)

#: [local-part]@[domain].[top-level-domain]
EMAIL = Regex(
    'Email',
    r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-]+',
    0,
    '<Email>',
)

#: Chinese telephone number format of 11 numbers. ( `[xxx][xxxx][xxxx]` )
#:
#: There can be space, `+`, `.`, `-` as delimiters. Such as
#: `155-5555-5555`
TELEPHONE = Regex(
    'Telephone',
    r'\d{3}[ +.-]?\d{4}[ +.-]?\d{4}',
    0,
    '<Telephone>',
)

#: :code:`r(\s+)`
#:
#: This can remove all extra spaces.
SPACE = Regex(
    'Space',
    r'\s+',
)

#: HTML tags includes 'script', 'style' and others.
HTML = Regex(
    'HTML',
    r'<script.*?>.*?</script>|<style.*?>.*?</style>|<.*?>',
    re.S,
)

#: English words, numbers, like 'hash', '3.14', '$100', '<EOS>'
#: , '99.9%'
ASCII_WORD = Regex(
    'ASCII_word',
    r'[<$#&]?[a-zA-Z0-9_.-]*\'?[a-zA-Z0-9]+[%>]?',
)

#: English words, punctuations, numbers are not included
ENGLISH = Regex(
    'English',
    r'[!-/:-~]+',
)

#: Numbers
NUMBER = Regex(
    'Numbers',
    r'[0-9]+',
)

#: Vietnamese with punctuations
#:
#: - https://stackoverflow.com/questions/37579692/unicode-range-for-vietnamese
#: - http://vietunicode.sourceforge.net/charset/
VIETNAMESE = Regex(
    'Vietnamese',
    r'[' +
    ''.join([r'\U{:0>8X}-\U{:0>8X}'.format(begin, end) for begin, end in [
        (0x0021, 0x0080),  # a-zA-Z0-9 and some punctuations
        (0x00C0, 0x00C3),
        (0x00C8, 0x00CA),
        (0x00CC, 0x00CD),
        (0x00D2, 0x00D5),
        (0x00D9, 0x00DA),
        (0x00E0, 0x00E3),
        (0x00E8, 0x00EA),
        (0x00EC, 0x00ED),
        (0x00F2, 0x00F5),
        (0x00F9, 0x00FA),
        (0x0102, 0x0103),
        (0x0110, 0x0111),
        (0x0128, 0x0129),
        (0x0168, 0x0169),
        (0x01A0, 0x01B0),
        (0x1EA0, 0x1EF9),
        (0x02C6, 0x0323),
    ]]) + ''.join([r'\U{:0>8X}'.format(x) for x in (0x00D0, 0x00DD, 0x00FD)])
        + r']+',
)

#: Thai: https://en.wikipedia.org/wiki/Thai_(Unicode_block) with punctuations
THAI = Regex(
    'Thai',
    r'[' +
    ''.join([r'\U{:0>8X}-\U{:0>8X}'.format(begin, end) for begin, end in [
        (0x0E01, 0x0E3A),
        (0x0E3F, 0x0E5B),
    ]]) + r']+',
)

#: All Chinese words without punctuations.
CHINESE_WORDS = Regex(
    'Chinese_words',
    r'[' +
    ''.join([r'\U{:0>8X}-\U{:0>8X}'.format(begin, end) for begin, end in [
        (0x4E00, 0x9FFF),       # CJK Unified Ideographs
        (0x3400, 0x4DBF),       # CJK Unified Ideographs Extension A
        (0x20000, 0x2A6DF),     # CJK Unified Ideographs Extension B
        (0x2A700, 0x2B73F),     # CJK Unified Ideographs Extension C
        (0x2B740, 0x2B81F),     # CJK Unified Ideographs Extension D
        (0x2B820, 0x2CEAF),     # CJK Unified Ideographs Extension E
        (0x2CEB0, 0x2EBEF),     # CJK Unified Ideographs Extension F
    ]]) + r']+',
)

#: All Chinese words includes most punctuations.
CHINESE = Regex(
    'Chinese',
    r'[' +
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
)

#: All CJK chars.
CJK = Regex(
    'CJK',
    r'[' +
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
)

DEFAULT_PATTERNS = [
    HTML,
    EMAIL,
    SPACE,
    TELEPHONE,
    URL,
    ASCII_WORD,
    CHINESE,
    CJK,
    ENGLISH,
    NUMBER,
    THAI,
    VIETNAMESE,
    CHINESE_WORDS,
]
