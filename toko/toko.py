#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from argparse import ArgumentParser
except ImportError:
    print "argparse is required to run this program"
    exit(1)
from wpclassify import toko_file
from wptrain import prepare_file
import sys
import inspect
import os

toko_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + "/"

def wpconfig(wapiti_path):
    config_file = open(toko_path + "tokoconfig", "w")
    config_file.write(wapiti_path)
    config_file.close()
    print "Wapiti path is permanently set to " + wapiti_path

def tokofile(file_path, Wapiti_path, Wapiti_model, delimiter):
    toko_file(file_path, Wapiti_path, Wapiti_model, delimiter)

def check_args(args):
    '''
    making sure that what's required is provided.
    '''
    if args.mode.lower() == "tokenize" and len(args.file) == 0:
        raise ValueError("You didn't specify any file to tokenize.")
        exit(1)
    else:
        for f in args.file:
            if not os.path.isfile(f):
                raise IOError("The following file doesn't exist:\n" + f)
                exit(1)
    
    if args.mode.lower() == "config" and args.wapiti is None:
        raise ValueError("You didn't provide the full path to Wapiti, please use the option --wapiti")        
    elif args.wapiti is not None and not os.path.exists(args.wapiti):
        raise IOError("The Wapiti path you provided doesn't exist.")
        exit(1)
    
    if args.model is not None and not os.path.isfile(args.model):
        raise IOError("The model (path) doesn't exist.")
        exit(1)

def main():

    argparser = ArgumentParser(description=__doc__)

    argparser.add_argument('mode', default='tokenize',
                           help='config, train or tokenize')

    argparser.add_argument('file', nargs='*',
                           help='file(s) to tokenize')

    argparser.add_argument('--delimiter', default='\n',
                           help='specify a delimiter for token boundaries (default: newline)')

    argparser.add_argument('--model', 
                           help='tokenization model (Wapiti model)')

    argparser.add_argument('--wapiti',
                           help='full path to Wapiti')


    args = argparser.parse_args()

    check_args(args)

    if args.mode.lower() == "config":
        wpconfig(args.wapiti)

    elif args.mode.lower() == "train":
        for input_file in args.file:
            prepare_file(input_file)

    elif args.mode.lower() == "tokenize":
        for input_file in args.file:
            tokofile(input_file, args.wapiti, args.model, args.delimiter)

    else:
        raise ValueError("Unknown mode. Please use: tokenize, train or config")


if __name__ == '__main__':
    main()
