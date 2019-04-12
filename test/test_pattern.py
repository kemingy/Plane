from plane import extract, replace, build_new_regex
from plane.pattern import (
    HTML,
    EMAIL,
    SPACE,
    TELEPHONE,
    URL,
    ASCII_WORD,
    CHINESE,
    CJK,
    CHINESE_WORDS,
    ENGLISH,
    THAI,
    VIETNAMESE,
    NUMBER,
)


def assert_list(x, y):
    assert len(x) == len(y)
    for i in range(len(x)):
        assert x[i] == y[i]


def test_url():
    text = [
        'http://www.guokr.com/如何',
        'For more information about Python Re, check'
        ' https://docs.python.org/3/library/re.html',
        'HTTPS://github.com/ try the upper case http://u.me.',
    ]
    urls = [
        ['http://www.guokr.com/'],
        ['https://docs.python.org/3/library/re.html'],
        ['HTTPS://github.com/', 'http://u.me.'],
    ]
    expect = [
        '<URL>如何',
        'For more information about Python Re, check <URL>',
        '<URL> try the upper case <URL>',
    ]
    assert_list(
        urls,
        [[x.value for x in list(extract(t, URL))] for t in text]
    )
    assert_list(
        expect,
        [replace(t, URL) for t in text]
    )


def test_email():
    text = [
        'Email Address: hello@kitty.com.',
        '电子邮件地址中通常会忽略一部分 full stops，比如 yes.sir@guokr.com '
        '相当于 yessir@guokr.com',
    ]
    emails = [
        ['hello@kitty.com'],
        ['yes.sir@guokr.com', 'yessir@guokr.com'],
    ]
    expect = [
        'Email Address: <Email>.',
        '电子邮件地址中通常会忽略一部分 full stops，比如 <Email> 相当于 <Email>',
    ]
    assert_list(
        emails,
        [[x.value for x in list(extract(t, EMAIL))] for t in text]
    )
    assert_list(
        expect,
        [replace(t, EMAIL) for t in text]
    )


def test_phone():
    text = [
        'Call me at 400-2333-6666',
        '这个13323336666的号码是谁的？',
        '188 0000 9999 是以前的，现在结尾是 2333',
    ]
    phones = [
        ['400-2333-6666'],
        ['13323336666'],
        ['188 0000 9999'],
    ]
    expect = [
        'Call me at <Telephone>',
        '这个<Telephone>的号码是谁的？',
        '<Telephone> 是以前的，现在结尾是 2333',
    ]
    assert_list(
        phones,
        [[x.value for x in list(extract(t, TELEPHONE))] for t in text]
    )
    assert_list(
        expect,
        [replace(t, TELEPHONE) for t in text]
    )


def test_space():
    text = [
        'hello world!\texciting!',
        """
        One more time.
        """,
    ]
    no_space = [
        [' ', '\t'],
        ['\n        ', ' ', ' ', '\n        '],
    ]
    expect = [
        'hello world! exciting!',
        ' One more time. '
    ]
    assert_list(
        no_space,
        [[x.value for x in list(extract(t, SPACE))] for t in text]
    )
    assert_list(
        expect,
        [replace(t, SPACE) for t in text]
    )


def test_html_and_space():
    text = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>
    <div class="center">
        <p id="danger">Don't do it!</p>
    </div>
</body>
<style>
    body {
        margin: 0;
        color: brown;
    }
</style>
<script>
    let m = Array();
    consolo.log(m);
</script>
</html>
        """
    expect = """ Document Don't do it! """
    assert replace(replace(text, HTML), SPACE) == expect


def test_ascii_word():
    text = "( ⊙ o ⊙ )What's that? It cost me $1000 to buy 0.1 bitcoin."
    expect = ['o', "What's", 'that', 'It', 'cost',
              'me', '$1000', 'to', 'buy', '0.1', 'bitcoin']
    assert [t.value for t in extract(text, ASCII_WORD)] == expect


def test_Chinese_and_cjk():
    text = """
Hello World!世界和平？
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Speed = 3×10^8 ㎞/s.
"""
    expect_chinese = '世界和平？'
    expect_cjk = '世界和平？㎞'
    assert ''.join([m.value for m in extract(text, CHINESE)]) == expect_chinese
    assert ''.join([m.value for m in extract(text, CJK)]) == expect_cjk


def test_pattern_add():
    ASCII = build_new_regex('ascii', r'[a-zA-Z0-9]+')
    WORDS = ASCII + CHINESE_WORDS
    text = "自然语言处理太难了！who can help me? (╯▔🔺▔)╯"
    expect = "自然语言处理太难了 who can help me"
    assert ' '.join([t.value for t in extract(text, WORDS)]) == expect


def test_pattern_radd():
    CN_EN_NUM = sum([CHINESE, ENGLISH, NUMBER])
    text = "佛是虚名，道亦妄立。एवं मया श्रुतम्। 1999 is not the end of the world. "
    expect = "佛是虚名，道亦妄立。 1999 is not the end of the world."
    assert ' '.join([t.value for t in extract(text, CN_EN_NUM)]) == expect


def test_thai():
    text = 'กากา cat หมา'
    expect = 'กากา หมา'
    assert ' '.join([t.value for t in extract(text, THAI)]) == expect


def test_viet():
    text = '越南语Vietnamese: Trường đại học bách khoa hà nội'
    expect = 'Vietnamese: Trường đại học bách khoa hà nội'
    assert ' '.join([t.value for t in extract(text, VIETNAMESE)]) == expect


def test_english():
    text = '全世界都在说 hello world!'
    expect = 'hello world!'
    assert ' '.join([t.value for t in extract(text, ENGLISH)]) == expect


def test_number():
    text = '2012 is not the end of world. So does 1999.'
    expect = '2012 1999'
    assert ' '.join([t.value for t in extract(text, NUMBER)]) == expect
