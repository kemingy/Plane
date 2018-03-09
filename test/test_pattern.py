from plane import extract, replace, RESTRICT_URL, EMAIL, TELEPHONE, SPACE, HTML

def assert_list(x, y):
    assert len(x) == len(y)
    for i in range(len(x)):
        assert x[i] == y[i]

def test_url():
    text = [
        'http://www.guokr.com/如何',
        'For more information about Python Re, check https://docs.python.org/3/library/re.html',
    ]
    urls = [
        ['http://www.guokr.com/'],
        ['https://docs.python.org/3/library/re.html'],
    ]
    expect = [
        '<URL>如何',
        'For more information about Python Re, check <URL>',
    ]
    assert_list(
        urls,
        [[x.value for x in list(extract(t, RESTRICT_URL))] for t in text]
    )
    assert_list(
        expect,
        [replace(t, RESTRICT_URL) for t in text]
    )

def test_email():
    text = [
        'Email Address: hello@kitty.com.',
        '电子邮件地址中通常会忽略一部分 full stops，比如 yes.sir@guokr.com 相当于 yessir@guokr.com',
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
