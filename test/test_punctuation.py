from plane import punc


def test_punctuation():
    # ASCII
    text = 'Hello World!'
    assert punc.remove(text) == 'Hello World '

    # Chinese
    text = '你瞅啥？瞅你咋地！'
    assert punc.remove(text) == '你瞅啥 瞅你咋地 '


def test_punctuation_with_repl():
    text = 'Hello, you are so c!@#%&*()_-l!'
    repl = 'o'
    assert punc.remove(text, repl) == 'Helloo you are so coooooooooolo'


def test_punctuation_normalization():
    text = '你读过那本《边城》吗？什么编程？！人生苦短，我用 Python。'
    assert punc.normalize(text) == '你读过那本(边城)吗?什么编程?!人生苦短,我用 Python.'
