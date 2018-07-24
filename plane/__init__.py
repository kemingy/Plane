from plane.punctuation import remove_punctuation
from plane.main import replace, extract, segment, build_new_regex
from plane.plane import Plane
from plane.pipeline import Pipeline
from plane.pattern import (
    HTML,
    EMAIL,
    SPACE,
    TELEPHONE,
    URL,
    CHINESE,
    CJK,
)

__version__ = '0.1.1'