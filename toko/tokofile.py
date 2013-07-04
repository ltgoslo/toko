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

def tokofile(file_path, Wapiti_path, Wapiti_model, delimiter):
    wp_classify_file(file_path, Wapiti_path, Wapiti_model, delimiter)

def check_args(args):
    for f in args.file:
        if not os.path.isfile(f):
            print f + " doesn't exist."
            exit(1)
    
    if args.wapiti is not None and not os.path.exists(args.wapiti):
        print "The Wapiti path you provided doesn't exist."
        exit(1)
    
    if args.model is not None and not os.path.isfile(args.model):
        print "The model (path) doesn't exist."
        exit(1)

def main():

    argparser = ArgumentParser(description=__doc__)

    argparser.add_argument('mode', default='tokenize',
                           help='config, train or tokenize')

    argparser.add_argument('file', nargs='*',
                           help='a file to tokenize')

    argparser.add_argument('--delimiter', default='\n',
                           help='specify a delimiter for token boundaries')

    argparser.add_argument('--model', 
                           help='path to Wapiti model')

    argparser.add_argument('--wapiti',
                           help='Wapiti full path')


    args = argparser.parse_args()

    check_args(args)

    if args.mode.lower() == "config":
        wpconfig(args.wapiti)

    elif args.mode.lower() == "train":
        print "produce training files"

    elif args.mode.lower() == "tokenize":
        for input_file in args.file:
            tokofile(input_file, args.wapiti, args.model, args.delimiter)

    else:
        print "Unknown mode. Please use: tokenize, train or config"


if __name__ == '__main__':
    main()
