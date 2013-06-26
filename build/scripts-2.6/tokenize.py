#!/usr/bin/python
# -*- coding: utf-8 -*-

older_version = False
try:
    from argparse import ArgumentParser
except ImportError:
    print "argpase is not available, please ..."
    older_version = True


from toko.classify import classify_file
import sys


def main():
    if older_version:
        print "old"
        toko.classify_file(sys.argv[1])
    else:
        classify_file(sys.argv[1])
        argparser = ArgumentParser(description=__doc__)
        argparser.add_argument('files', nargs='*',
                               help='a (list of) file(s) to tokenize')
        argparser.add_argument('--delimiter', default='\n',
                               help='specify a delimiter for token boundaries')
        argparser.add_argument('--model', 
                               help='path to *Wapiti* model')

        args = argparser.parse_args()
        
        pattern = None
        
        #for path in args.files:
        #    process(path, pattern, config)
        #print args.delimiter
    
if __name__ == '__main__':
    main()
