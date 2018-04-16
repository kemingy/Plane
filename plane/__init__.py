from .punctuation import remove_punctuation
from .main import replace, extract, segment, build_new_regex
from .pattern import (
    HTML,
    EMAIL,
    SPACE,
    TELEPHONE,
    RESTRICT_URL,
    CHINESE,
    CJK,
)

__version__ = '0.0.7'