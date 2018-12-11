# Plane

[![Build Status](https://travis-ci.org/kemingy/Plane.svg?branch=master)](https://travis-ci.org/kemingy/Plane)

> **Plane** is a tool for shaping wood using muscle power to force the cutting blade over the wood surface.  
> *from [Wikipedia](https://en.wikipedia.org/wiki/Plane_(tool))*

![plane(tool) from wikipedia](https://upload.wikimedia.org/wikipedia/commons/e/e3/Kanna2.gif)

This package is used for extracting or replacing specific parts from text, like URL, Email, HTML tags, telephone numbers and so on. Or just remove all unicode punctuations.

See the full [Documents](https://kemingy.github.io/Plane/).

## Install

Python **3.x** only.

### pip

```python
pip install plane
```

### Install from source

```sh
python setup.py install
```

## Features

* build-in regex patterns: `plane.pattern.Regex`
* custom regex patterns
* extract, replace patterns
* segment sentence
* chain function calls: `plane.plane.Plane`

## Usage

### pattern

`Regex` is a namedtuple with 3 items:

* `name`
* `pattern`: Regular Expression
* `repl`: replacement tag, this will replace matched regex when using `replace` function

```python
# create new pattern
from plane import build_new_regex
custom_regex = build_new_regex('my_regex', r'(\d{4})', '<my-replacement-tag>')
```

Default Regex: [Details](https://github.com/Momingcoder/Plane/blob/master/plane/pattern.py)

* `URL`: only ASCII
* `EMAIL`: local-part@domain
* `TELEPHONE`: like xxx-xxxx-xxxx
* `SPACE`: ` `, `\t`, `\n`, `\r`, `\f`, `\v`
* `HTML`: HTML tags, Script part and CSS part
* `ASCII_WORD`: English word, numbers, `<tag>` and so on.
* `CHINESE`: all Chinese characters (only Han and punctuations)
* `CJK`: all Chinese, Japanese, Korean(CJK) characters and punctuations

Regex name | replace
-----------|---------
URL        | `'<URL>'`
EMAIL      | `'<Email>'`
TELEPHONE  | `'<Telephone>'`
SPACE      | `' '`
HTML       | `' '`
ASCII_WORD | `' '`
CHINESE    | `' '`
CJK        | `' '`

Use regex to `extract` or `replace`:

```python
from plane import EMAIL, extract, replace
text = 'fake@no.com & fakefake@nothing.com'

emails = extract(text, EMAIL) # this return a generator object
for e in emails:
    print(e)

>>> Token(name='Email', value='fake@no.com', start=0, end=11)
>>> Token(name='Email', value='fakefake@nothing.com', start=14, end=34)

print(EMAIL)

>>> Regex(name='Email', pattern='([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-]+)', repl='<Email>')

replace(text, EMAIL) # replace(text, Regex, repl), if repl is not provided, Regex.repl will be used

>>> '<Email> & <Email>'

replace(text, EMAIL, '')

>>> ' & '
```

### segment

`segment` can be used to segment sentence, English and Numbers like 'PS4' will be keeped and others like Chinese '中文' will be split to single word format `['中', '文']`.

```python
from plane import segment
segment('你看起来guaiguai的。<EOS>')
>>> ['你', '看', '起', '来', 'guaiguai', '的', '。', '<EOS>']
```

### punctuation

`remove_punctuation` will replace all unicode punctuations to `' '` or something you send to this function as paramter `repl`.

**Attention**: '+', '^', '$', '~' and some chars are not punctuation.

```python
from plane import remove_punctuation

text = 'Hello world!'
remove_punctuation(text)

>>> 'Hello world '

# replace punctuation with special string
remove_punctuation(text, '<P>')

>>> 'Hello world<P>'
```

### Chain function

`Plane` contains `extract`, `replace`, `segment` and `remove_punctuation`, and these methods can be called in chain. Since `segment` returns list, it can only be called in the end of the chain.

`Plane.text` saves the result of processed text and `Plane.values` saves the result of extracted strings.

```python
from plane import Plane
from plane.pattern import EMAIL

p = Plane()
p.update('My email is my@email.com.').replace(EMAIL, '').text # update() will init Plane.text and Plane.values

>>> 'My email is .'

p.update('My email is my@email.com.').replace(EMAIL).segment()

>>> ['My', 'email', 'is', '<Email>', '.']

p.update('My email is my@email.com.').extract(EMAIL).values

>>> [Token(name='Email', value='my@email.com', start=12, end=24)]
```

### Pipeline

You can use `Pipeline` if you like. 

`segment` and `extract` can only present in the end.

```python
from plane import Pipeline
from plane.pattern import URL

pipe = Pipeline([
    ('replace', URL, ''),
    ('segment', ),
])
pipe('http://www.guokr.com is online.')

>>> ['is', 'online', '.']
