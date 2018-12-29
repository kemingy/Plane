import types
from inspect import signature

from plane.pattern import Token


class Pipeline:
    """
        Initialize pipeline with functions.
        For example:
        ::

            pl = Pipeline(
                lambda text: replace(text, EMAIL),
                segment,
            )
            pl("My email is abc@hello.com")

            >> ["My", "email", "is", "<Email>"]
    """
    def __init__(self, *functions):
        self.functions = []
        for func in functions:
            if not callable(func):
                raise ("Cann't call func: {}".format(func))
            self.functions.append(func)

    def __call__(self, text):
        for func in self.functions:
            if not text:
                return text
            if isinstance(text, types.GeneratorType):
                text = list(text)
            if isinstance(text, list):
                if isinstance(text[0], str):
                    text = " ".join(text)
                elif isinstance(text[0], Token):
                    text = " ".join([t.value for t in text])
                else:
                    raise TypeError(
                        "expected string or Token in list, but get {}"
                        .format(type(text[0])))

            text = func(text)
        return text

    def add(self, func, *args, **kwargs):
        """
        Add functions.
        ::

            pl = Pipeline()
            pl.add(replace, EMAIL)
            pl.add(segment)
            pl("My email is abc@hello.com")

            >> ["My", "email", "is", "<Email>"]
        """
        if 'text' in signature(func).parameters:
            def f(text): return func(text, *args, *kwargs)
        else:
            f = func(*args, **kwargs)
        self.functions.append(f)
