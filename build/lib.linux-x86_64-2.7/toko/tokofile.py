#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from argparse import ArgumentParser
except ImportError:
    print "argparse is required to run this program"
    #exit(1)
from wpclassify import wp_classify_file
import sys
import inspect
import os

toko_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "/"

def wpconfig(wapiti_path):    
    print toko_path
    config_file = open(toko_path + "tokoconfig", "w")
    config_file.write(wapiti_path)
    config_file.close()

def tokofile(file_path):
    wp_classify_file(file_path)

def main():

    argparser = ArgumentParser(description=__doc__)

    argparser.add_argument('mode', default='tokenize',
                           help='config, train or tokenize')

    argparser.add_argument('file', nargs='*',
                           help='a file to tokenize')

    argparser.add_argument('--delimiter', default='\n',
                           help='specify a delimiter for token boundaries')

    argparser.add_argument('--model', 
                           help='path to *Wapiti* model')

    argparser.add_argument('--wapiti',
                           help='Wapiti full path')


    args = argparser.parse_args()

    if args.mode == "config":
        print "configuration"
        wpconfig(args.wapiti)

    elif args.mode == "train":
        print "produce training files"

    elif args.mode == "tokenize":
        for input_file in args.file:
            tokofile(input_file)
        print "tokenizing"

    else:
        print "Unknown mode. Please use: tokenize, train or config"


if __name__ == '__main__':
    main()
