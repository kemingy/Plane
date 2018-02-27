from plane import remove_punctuation

def test_punctuation():
    # ASCII
    text = 'Hello World!'
    assert remove_punctuation(text) == 'Hello World '

    # Chinese
    text = '你瞅啥？瞅你咋地！'
    assert remove_punctuation(text) == '你瞅啥 瞅你咋地 '

def test_punctuation_with_repl():
    text = 'Hello, you are so c!@#%&*()_-l!'
    repl = 'o'
    assert remove_punctuation(text, repl) == 'Helloo you are so coooooooooolo'