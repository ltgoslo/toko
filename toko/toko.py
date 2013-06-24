#!/usr/bin/env python
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
from subtoken import Subtoken
import classify
from classify import call_wapiti
import sys

def subtokenize_file(file_name):
    subtk_file = open(file_name + ".subtks", "w")
    raw_lines = [line for line in open(file_name)]
    
    for line in raw_lines:
        line_splits = line.split("\t") #0: ID, 1: sentence
        t = Subtoken(line_splits[1][0:-1]) # [0:-1] to remove the `\n'
        subtokens, categories, spaces = t.subtokenize()

        for i in range(len(subtokens)):
            subtk_line = line_splits[0] + '\t' + subtokens[i] + '\t' + str(spaces[i]) + '\t'+ categories[i] + '\t'
            subtk_file.write(subtk_line)
            subtk_file.write('\n')
        subtk_file.write('\n')

    subtk_file.close()
        

def main():
    #t = Token("He Cannot go to school, today! Wow, why he wouldn't?")
    #subtokens, categories, spaces = t.subtokenize()

    #for i in range(len(subtokens)):
    #    print subtokens[i], '\t', categories[i], '\t', spaces[i], '\t'
    call_wapiti()

    #subtokenize_file(sys.argv[1])

    argparser = ArgumentParser(description=__doc__)
    argparser.add_argument('files', nargs='*',
                           help='a (list of) file(s) to tokenize')
    #argparser.add_argument('--accounting', action='store_true',
    #                       help='output an account of modifications made to the original segment')
    argparser.add_argument('--delimiter', default='\n',
                           help='specify a delimiter for token boundaries')
    argparser.add_argument('--paragraph-mode', action='store_true',
                           help='force segmentation at double newlines')
    argparser.add_argument('--model',
                           help='path to *Wapiti* model')

    args = argparser.parse_args()
    
    pattern = None

    #for path in args.files:
    #    process(path, pattern, config)
    print args.delimiter
    print args
    
if __name__ == '__main__':
    main()
