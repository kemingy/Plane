import sys
import unicodedata
import re


class Punctuation:
    """All the punctuations in Unicode.

    Abbr. Description
    ::

        Pc	Punctuation, Connector
        Pd	Punctuation, Dash
        Ps	Punctuation, Open
        Pe	Punctuation, Close
        Pi	Punctuation, Initial quote (may behave like Ps or Pe)
        Pf	Punctuation, Final quote (may behave like Ps or Pe)
        Po	Punctuation, Other

    Some chars are not included in punctuations. Such as: `+`, `^`, `$`, `~`.

    You can use :class:`Plane.pattern` to process these chars.
    """
    def __init__(self, normalization=None):
        self.repl = ' '
        self.punc = None
        self.punc_map = {}
        self.normalizer = None
        self.normelization = normalization or {
            '`': '\'',
            '\'\'': '"',
            '„': '"',
            '–': '-',
            '—': ' - ',
            '´': '\'',
            '‚': '"',
            '´´': '"',
            '…': '...',
            # French quotes
            '«': '"',
            '»': '"',
            # Chinese
            '，': ',',
            '。': '.',
            '？': '?',
            '！': '!',
            '：': ':',
            '（': '(',
            '）': ')',
            '【': '(',
            '】': ')',
            '《': '(',
            '》': ')',
            '「': '(',
            '」': ')',
            '『': '(',
            '』': ')',
            '’': '\'',
            '‘': '\'',
            '“': '"',
            '”': '"',
            '；': ';',
            '〜': '~',
        }

    def get_punc_map(self, repl=' '):
        if not self.punc:
            self.punc = [
                c for c in range(sys.maxunicode)
                if unicodedata.category(chr(c)).startswith('P')
            ]
        if repl not in self.punc_map:
            self.punc_map[repl] = dict(zip(self.punc, repl * len(self.punc)))

        return self.punc_map[repl]

    def remove(self, text, repl=' '):
        """
        :param str text: input text

        Remove all punctuations.

        This methods use :class:`unicodedata`
        (https://docs.python.org/3.6/library/unicodedata.html) to get all
        the punctuations.
        """
        return text.translate(self.get_punc_map(repl))

    def normalize(self, text):
        """
        :param str text: input text

        Convert punctuations from other languages to English punctuations.
        Not every punctuation is included.

        - https://github.com/moses-smt/mosesdecoder/blob/master/scripts
        - http://xahlee.info/comp/unicode_punctuation_symbols.html
        - https://www.compart.com/en/unicode/category/Po
        """
        if not self.normalizer:
            self.init_normalization()
        return self.normalizer.sub(
            lambda m: self.normelization[m.string[m.start():m.end()]], text)

    def init_normalization(self):
        if not self.normalizer:
            self.normalizer = re.compile('({})'.format(
                '|'.join(map(re.escape, self.normelization.keys()))))


punc = Punctuation()
