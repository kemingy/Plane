.. plane documentation master file, created by
   sphinx-quickstart on Tue Jul 17 17:45:43 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Plane's documentation!
=================================

`Plane` is a tool to remove the useless part of the sentence, just like the carpenter shapes the wood.

.. figure:: https://upload.wikimedia.org/wikipedia/commons/e/e3/Kanna2.gif


This package already offers some useful regex patterns, such as HTML tags, URL, Email. You can also write your own regex pattern and concatenate with existing patterns.


Features
---------

* build-in regex patterns: :class:`plane.pattern.Regex`
* custom regex patterns
* extract, replace patterns
* segment sentence
* chain function calls: :class:`plane.plane.Plane`
* pipeline: :class:`plane.pipeline.Pipeline`


Why we need this?
------------------------

In NLP(Natural language processing) task, cleaning text data may be one of the most boring things. `Plane` is built for this.

* extract content from web page source
* detect urls, emails, telephone numbers
* split sentence composed of Chinese and English
* remove all punctuations to get pure text


Usage
---------

Only support Python3.

`extract` and `replace`
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

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


`segment`
~~~~~~~~~~~~~~~~

`segment` can be used to segment sentence, English and Numbers like 'PS4' will be keeped and others like Chinese '中文' will be split to single word format `['中', '文']`.

::

    from plane import segment
    segment('你看起来guaiguai的。<EOS>')
    >>> ['你', '看', '起', '来', 'guaiguai', '的', '。', '<EOS>']


replace all punctuations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`remove_punctuation` will replace all unicode punctuations to `' '` or something you send to this function as paramter `repl`.

**Attention**: '+', '^', '$', '~' and some chars are not punctuation.

::

    from plane import remove_punctuation

    text = 'Hello world!'
    remove_punctuation(text)

    >>> 'Hello world '

    # replace punctuation with special string
    remove_punctuation(text, '<P>')

    >>> 'Hello world<P>'


chain function calls
~~~~~~~~~~~~~~~~~~~~~~~~

`Plane` contains `extract`, `replace`, `segment` and `remove_punctuation`, and these methods can be called in chain. Since `segment` returns list, it can only be called in the end of the chain.

`Plane.text` saves the result of processed text and `Plane.values` saves the result of extracted strings.

::

    from plane import Plane
    from plane.pattern import EMAIL

    p = Plane()
    p.update('My email is my@email.com.').replace(EMAIL, '').text # update() will init Plane.text and Plane.values

    >>> 'My email is .'

    p.update('My email is my@email.com.').replace(EMAIL).segment()

    >>> ['My', 'email', 'is', '<Email>', '.']

    p.update('My email is my@email.com.').extract(EMAIL).values

    >>> [Token(name='Email', value='my@email.com', start=12, end=24)]


pipeline
~~~~~~~~~~~~~~~~

You can use `Pipeline` if you like.

::

    from plane import Pipeline, replace, segment
    from plane.pattern import URL

    pipe = Pipeline()
    pipe.add(replace, URL, '')
    pipe.add(segment)
    pipe('http://www.guokr.com is online.')

    >>> ['is', 'online', '.']


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   patterns
   details


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
