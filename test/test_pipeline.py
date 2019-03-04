from plane import Pipeline, replace, extract, segment, punc
from plane.pattern import EMAIL, TELEPHONE


def test_pipeline():
    text = 'You can send me an email at send@email.com ' \
        'or call me at 123-4567-8910.'
    pipeline = Pipeline()
    pipeline.add(replace, EMAIL)
    pipeline.add(replace, TELEPHONE, '')
    assert pipeline(text) == 'You can send me an email ' \
        'at <Email> or call me at .'

    pipeline = Pipeline()
    pipeline.add(replace, EMAIL, '')
    pipeline.add(replace, TELEPHONE, '')
    pipeline.add(segment)
    assert pipeline(text) == [
        'You', 'can', 'send', 'me', 'an', 'email',
        'at', 'or', 'call', 'me', 'at', '.'
    ]

    pipeline = Pipeline()
    pipeline.add(extract, EMAIL)
    assert list(pipeline(text))[0].value == 'send@email.com'

    pipeline = Pipeline()
    pipeline.add(replace, EMAIL, 'email')
    pipeline.add(extract, EMAIL)
    assert list(pipeline(text)) == []

    pipeline = Pipeline(
        punc.remove,
        segment
    )
    assert pipeline('hello, world!') == ['hello', 'world']
