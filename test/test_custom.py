from plane import extract, replace, build_new_regex
import re


def test_custom_regex():
    custom_regex = build_new_regex('custom', r'(one|two|three)', re.I, '<NUM>')
    text = 'One of the two will be used. Which one is undefined.'
    num = ['One', 'two', 'one']
    expect = '<NUM> of the <NUM> will be used. Which <NUM> is undefined.'

    result = list(extract(text, custom_regex))
    assert len(result) == len(num)
    for i in range(len(num)):
        assert num[i] == result[i].value

    assert replace(text, custom_regex) == expect
