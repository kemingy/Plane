from plane import Pipeline
from plane.pattern import EMAIL, TELEPHONE


def test_pipeline():
    text = 'You can send me an email at send@email.com ' \
        'or call me at 123-4567-8910.'
    pipeline = Pipeline([
        ('replace', EMAIL),
        ('replace', TELEPHONE, ''),
    ])
    assert pipeline(text) == 'You can send me an email ' \
        'at <Email> or call me at .'

    pipeline = Pipeline([
        ('replace', EMAIL, ''),
        ('replace', TELEPHONE, ''),
        ('segment',),
    ])
    assert pipeline(text) == ['You', 'can', 'send', 'me', 'an', 'email',
                              'at', 'or', 'call', 'me', 'at', '.']

    pipeline = Pipeline([
        ('extract', EMAIL)
    ])
    assert pipeline(text)[0].value == 'send@email.com'

    pipeline = Pipeline([
        ('replace', EMAIL, 'email'),
        ('extract', EMAIL),
    ])
    assert pipeline(text) == []

    pipeline = Pipeline([
        ('remove_punctuation',),
        ('segment', ),
    ])
    assert pipeline('hello, world!') == ['hello', 'world']
