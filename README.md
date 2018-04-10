# Plane

[![Build Status](https://travis-ci.org/Momingcoder/Plane.svg?branch=master)](https://travis-ci.org/Momingcoder/Plane)

> **Plane** is a tool for shaping wood using muscle power to force the cutting blade over the wood surface.  
> *from [Wikipedia](https://en.wikipedia.org/wiki/Plane_(tool))*

![plane(tool) from wikipedia](https://upload.wikimedia.org/wikipedia/commons/e/e3/Kanna2.gif)

This package is used for extracting or replacing specific parts from text, like URL, Email, HTML tags, telephone numbers and so on. Or just remove all unicode punctuations.

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

Default Regex:

* `RESTRICT_URL`: only ASCII
* `EMAIL`: local-part@domain
* `TELEPHONE`: like xxx-xxxx-xxxx
* `SPACE`: ` `, `\t`, `\n`, `\r`, `\f`, `\v`
* `HTML`: HTML tags, Script part and CSS part
* `CHINESE`: all Chinese characters (only Han, without punctuations)
* `CJK`: all Chinese, Japanese, Korean(CJK) characters (with punctuations)

Use regex to `extract` or `replace`:

```python
from plane import EMAIL, extract, replace
text = 'fake@no.com & fakefake@nothing.com'

emails = extract(text, [EMAIL]) # this return a generator object
for e in emails:
    print(e)

>>> Token(name='Email', value='fake@no.com', start=0, end=11)
>>> Token(name='Email', value='fakefake@nothing.com', start=14, end=34)

replace(text, [EMAIL])

>>> '<Email> & <Email>'
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