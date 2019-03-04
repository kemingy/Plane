from plane import Plane
from plane.pattern import EMAIL

p = Plane()
text = 'You can send me an email at send@email.com.'


def test_extract():
    v = list(p.update(text).extract(EMAIL, True))
    values = p.update(text).extract(EMAIL).values

    assert v == values
    assert values[0].value == 'send@email.com'


def test_replace():
    p.update(text)
    assert p.replace(EMAIL).text == 'You can send me an email at <Email>.'
    p.update(text)
    assert p.replace(EMAIL, '').text == 'You can send me an email at .'


def test_segment():
    assert p.update(text).replace(EMAIL, '').segment() == \
        ['You', 'can', 'send', 'me', 'an', 'email', 'at', '.']


def test_remove_punctuation():
    assert p.update(text).remove_punctuation().text == \
        'You can send me an email at send email com '

    assert p.update(text).replace(EMAIL, '').remove_punctuation().text == \
        'You can send me an email at  '


def test_normalize_punctuation():
    t = '你读过那本《边城》吗？什么编程？！人生苦短，我用 Python。'
    assert p.update(t).normalize_punctuation().text == \
        '你读过那本(边城)吗?什么编程?!人生苦短,我用 Python.'
