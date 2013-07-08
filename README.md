toko
========

toko is a machine learning based tokenization tool described in [Fares et al. 2013](http://link.springer.com/chapter/10.1007%2F978-3-642-37247-6_19).


Prerequisites:
--------------

* Python (versions 2.6 and 2.7 recommended)
* Wapiti (http://wapiti.limsi.fr/)


Installation
--------------
You can install toko as a python package (site-package) using the egg file already built or build toko yourself.
To build toko as an egg file, do (in the toko dir):
```sh
    python setup.py bdist_egg
```

Then you can install the egg file using easy_install (for example). Assuming that you have already set PYTHONPATH (in your .bashrc) to /home/user/mypythonpackages/, do:

```sh
    easy_install --install-dir /home/user/mypythonpackages/ the-toko-egg-file.egg
```
If you cannot build the egg file, you can install the egg file provided with toko (you only need to run the previous command).


To use (with caution), simply do::

    >>> import toko
    >>> toko.wpclassify.wp_classify_file()
    >>> toko.tokenize_sentence()

Running modes
--------------

toko runs in three modes: 
    *  config 
    *  tokenize 
    *  train

### config
You can use the config mode to permanently set the path to Wapiti, as follows:
```sh
    python toko config --wapiti /full/path/to/wapiti/
```


After doing this there will be no need to pass the wapiti path in
the 'tokenize' mode, however if you haven't permanently set the path
to wapiti you must pass the argument --wapiti.


### tokenize

In this mode toko expects a file to tokenize with several optional
arguments.
```sh
    python toko tokenize file
```


TODO
----------

- [ ] toko_sentence
- [ ] train mode
- [X] egg file

Notes
----------
1) Please use absolute paths all the time, especially for Wapiti
models because the Wapiti path might be different from that of the
tokenizer.


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
