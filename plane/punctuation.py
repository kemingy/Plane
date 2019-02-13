import sys
import unicodedata


class Punctuation:
    """All the punctuations in Unicode.

    Abbr. Description
    ::

        Pc	Punctuation, Connector
        Pd	Punctuation, Dash
        Ps	Punctuation, Open
        Pe	Punctuation, Close
        Pi	Punctuation, Initial quote (may behave like Ps or Pe depending on usage)
        Pf	Punctuation, Final quote (may behave like Ps or Pe depending on usage)
        Po	Punctuation, Other

    Some chars are not included in punctuations. Such as: `+`, `^`, `$`, `~`.

    You can use :class:`Plane.pattern` to process these chars.
    """
    def __init__(self):
        self.repl = ' '
        self.punc = None
        self.punc_map = {}

    def get_punc_map(self, repl=' '):
        if not self.punc:
            self.punc = [
                c for c in range(sys.maxunicode)
                if unicodedata.category(chr(c)).startswith('P')
            ]
        if repl not in self.punc_map:
            self.punc_map[repl] = dict(zip(self.punc, repl * len(self.punc)))

        return self.punc_map[repl]


punc = Punctuation()


def remove_punctuation(text, repl=' '):
    """
    :param str text: input text

    Remove all punctuations.

    This methods use :class:`unicodedata`
    (https://docs.python.org/3.6/library/unicodedata.html) to get all
    the punctuations.
    """
    return text.translate(punc.get_punc_map(repl))
