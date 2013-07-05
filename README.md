toko
--------

To use (with caution), simply do::

    >>> import toko
    >>> toko.wpclassify.wp_classify_file()
    >>> toko.tokenize_sentence()


Notes:
1) Please use absolute paths all the time, especially for Wapiti
models because the Wapiti path might be different from that of the
tokenizer.


The package runs in three modes: 
    1.  config 
    2.  tokenize 
    3.  train

### config
To permanently set the path of Wapiti, you can use::

    python toko config --wapiti /full/path/to/wapiti


After doing this there will be no need to pass the wapiti path with
the 'tokenize' mode, however if you haven't permanently set the path
to wapiti you must pass the argument --wapiti.


### tokenize

In this mode toko expects a file to tokenize with several optional
arguments


http://dl.acm.org/citation.cfm?id=2468243

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

