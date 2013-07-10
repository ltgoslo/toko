toko
========

toko is a machine learning based tokenization tool (based on [Fares et al. 2013](http://link.springer.com/chapter/10.1007%2F978-3-642-37247-6_19)).
In brief, toko introduces potential token boundaries, 
then it uses a pre-trained CRF model to classify the potential token boundaries.

Prerequisites
--------------

* Python (versions 2.6 and 2.7 recommended)
* Wapiti (http://wapiti.limsi.fr/)


Installation
--------------
toko can be installed as a python package (site-package) using the egg file: *toko-0.1.0-py2.7.egg*.
One can also build the egg file first and then install it.

To build toko as an egg file, do (in the toko dir):
```sh
    python setup.py bdist_egg
```

Then you can install the egg file using [easy_install](http://peak.telecommunity.com/DevCenter/EasyInstall) (for example). 
Assuming that you have already set PYTHONPATH (in your .bashrc) to /home/user/mypythonpackages/, do:

```sh
    easy_install --install-dir /home/user/mypythonpackages/ toko-0.1.0-py2.7.egg
```
To install the egg file provided with toko, you only need to run the last command above.


Usage
------------
The toko package can be used in two ways:
1. The *toko* script
2. from toko import wpclassify


A Python script named *toko* will be installed together with the toko package (in your Python site-packages directory).
You can either use the *toko* script or import toko to your Python project or script.

To use the *toko* script, simply do:
```sh
    python toko tokenize file-name --wapiti /home/user/wapiti/
```

To call toko from another Python script:
```python
    >>> from toko import wpclassify
    >>> wpclassify.toko_file(file_to_be_tokenized, full_wapiti_path, wapiti_model, delimiter)
    >>> wpclassify.toko_sentence("sentence", "/full/path/to/wapiti/", "/full/path/to/wapiti/model/ptb.model")
```
toko provides two functions for tokenization:
*   __toko_file__:  takes a file as an input and writes the output into another file
*   __toko_sentence__: takes a sentence (string) and returns a list of tokens (strings) 

For more details see toko/wpclassify.py.



### Input
The input files can be formatted in two ways:

1. Sentence-ID \tab sentence per line:
```
    22200014        The complicated language in the huge new law has muddied the fight.
```

2. One sentence per line:
```
    The complicated language in the huge new law has muddied the fight.
```

### Output
The default output of toko is a file containing one token per line and sentences are separated by newlines.

```
The
complicated
language
in
the
huge
new
law
has
muddied
the
fight
.

```

If the input file name was input.txt, then the output file would be input.txt.tks


### Running modes

toko runs in three modes:

*  config 
*  tokenize 
*  train

#### config
You can use the config mode to permanently set the path to Wapiti, as follows:
```sh
    python toko config --wapiti /full/path/to/wapiti/
```


After doing this there will be no need to pass the wapiti path in
the 'tokenize' mode, however if you haven't permanently set the path
to wapiti you must pass the argument --wapiti.


#### tokenize

In this mode toko expects a file to tokenize with several optional
arguments.
```sh
    python toko tokenize file
```

#### train
The train mode only prepares training data but the actual training needs to be done using Wapiti.

Files
------------
```
+---models
|       - ptb.model
+---data
|       - test.raw.tokens
|       - test.raw
+---toko
|       - wpclassify.py
|       - toko.py
|       - subtoken.py
|       - __init__.py
```

Tasks
----------

- [x] toko_sentence
- [ ] train mode
- [x] egg file

Notes
----------
Please use absolute paths, especially for Wapiti
models because the Wapiti path might be different from that of toko.


References
----------

```LaTeX
    @inproceedings{Far:Oep:Zha:13,
        author = {Fares, Murhaf and Oepen, Stephan and Zhang, Yi},
        title = {Machine learning for high-quality tokenization replicating variable tokenization schemes},
        booktitle = {Proceedings of the 14th international conference on Computational Linguistics and Intelligent Text Processing - Volume Part I},
        year = {2013},
        isbn = {978-3-642-37246-9},
        location = {Samos, Greece},
        pages = {231--244}, 
        publisher = {Springer-Verlag},
        address = {Berlin, Heidelberg},
    }
```


License (MIT)
--------------

Copyright (c) 2013 Murhaf Fares

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
