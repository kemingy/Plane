import types
from collections import namedtuple

from plane.main import extract, replace, segment
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
            else:
                raise NameError('Unknown function name.')


    def __call__(self, text):
        for p in self.processors:
            if p.func == 'segment':
                text = segment(text)
            elif p.func == 'extract':
                text = extract(text, p.regex)
            else:
                text = replace(text, p.regex, p.repl)

        if isinstance(text, types.GeneratorType):
            return list(text)
        return text