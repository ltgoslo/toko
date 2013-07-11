toko
========

toko is a machine learning based tokenization tool (based on [Fares et
al. 2013](http://link.springer.com/chapter/10.1007%2F978-3-642-37247-6_19)).
In brief, toko introduces potential token boundaries (so-called
subtokens), then it uses a pre-trained CRF model to classify the
potential token boundaries.

Prerequisites
--------------

* Python (versions 2.6 and 2.7 recommended)
* Wapiti (http://wapiti.limsi.fr/)


Installation
--------------
toko can be installed as a python package (site-package) using the egg
file: *toko-0.1.0-py2.7.egg*.
One can also build the egg file first and then install it.

To build toko as an egg file, do (in the toko dir):
```sh
    python setup.py bdist_egg
```

Then you can install the egg file using [easy_install](http://peak.telecommunity.com/DevCenter/EasyInstall). 
Assuming that you have already set PYTHONPATH (in your .bashrc, for
example) to /home/user/mypythonpackages/, do:

```sh
    easy_install --install-dir /home/user/mypythonpackages/ toko-0.1.0-py2.7.egg
```
To install the egg file provided with toko, you only need to run the last command above.

*Note*: Of course one can use toko without installing it by running the script [toko.py](toko/toko.py).


Usage
------------
The toko package can be used in two ways:

1. The *toko* script
2. from toko import wpclassify


A Python script named *toko* will be installed together with the toko
package (in your Python site-packages directory).
You can either use the *toko* script or import toko to your Python
project or script.

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

For more details see [wpclassify.py](toko/wpclassify.py).



### Input & Output
The input files can be formatted in two ways:

1. Sentence-ID \tab sentence per line:
```
    22200014        The complicated language in the huge new law has muddied the fight.
```

2. One sentence per line:
```
    The complicated language in the huge new law has muddied the fight.
```

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

If the input file name was input.txt, then the output file would be
named input.txt.tks


### Running modes

toko runs in three modes:

*  config 
*  tokenize 
*  train

#### config
The only use of the *config* mode is to permanently set the path to
Wapiti.
In order to avoid passing the argument --wapiti every time you want to
tokenize a file (or sentence), you can permanently set the Wapiti path
as follows:
```sh
    python toko config --wapiti /full/path/to/wapiti/
```



#### tokenize

The *tokenize* mode toko expects a file to tokenize with several optional
arguments.
```sh
    python toko tokenize file --delimiter " | " --model /home/user/toko/models/ptb.model
```

--delimiter and --model are optional arguments.

#### train
The train mode only prepares training data but the actual training
needs to be done using Wapiti (we provide the feature template used to
train our PTB model). In other words, the 'train' mode provides the
subtokens of the 'gold' tokens.

toko, in the train mode, expects a file with one 'gold' token per line
and sentence are separated with newlines. However, Sentence-ID \tab
token is also allowed, as described [above](#input--output]).

To prepare the training data:
```sh
	python toko train myfilename
```

The output is saved in a file named myfilename.wptks

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
|       - wptrain.py
|       - toko.py
|       - subtoken.py
|       - __init__.py
```



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
