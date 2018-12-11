import types
from collections import namedtuple

from plane.main import extract, replace, segment
from plane.punctuation import remove_punctuation
from plane.pattern import Regex
from plane.pattern import ASCII_WORD

Processor = namedtuple(
    'Processor',
    [
        'func',
        'regex',
        'repl',
    ]
)


def build_procssor(func, regex=None, repl=None):
    if func == 'segment':
        regex = regex or ASCII_WORD
    elif func == 'remove_punctuation':
        repl = repl if repl is not None else ' '
    return Processor(func, regex, repl)


class Pipeline:
    def __init__(self, processors):
        self._check(processors)
        self.processors = [build_procssor(*p) for p in processors]

    def _check(self, processors):
        for i, p in enumerate(processors):
            assert isinstance(p[0], str)
            if p[0] == 'replace':
                assert len(p) > 1
                assert isinstance(p[1], Regex)
            elif p[0] == 'extract':
                assert i == len(processors) - 1
                assert len(p) > 1
                assert isinstance(p[1], Regex)
            elif p[0] == 'segment':
                assert i == len(processors) - 1
            elif p[0] == 'remove_punctuation':
                continue
            else:
                raise NameError('Unknown function name.')

    def __call__(self, text):
        for p in self.processors:
            if p.func == 'segment':
                text = segment(text, p.regex)
            elif p.func == 'extract':
                text = extract(text, p.regex)
            elif p.func == 'replace':
                text = replace(text, p.regex, p.repl)
            else:
                text = remove_punctuation(text, p.repl)
                print(text)

        if isinstance(text, types.GeneratorType):
            return list(text)
        return text
