#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from argparse import ArgumentParser
from token import Token
import sys

def subtokenize_file(file_name):
    subtk_file = open(file_name + ".subtks", "w")
    raw_lines = [line for line in open(file_name)]
    
    for line in raw_lines:
        line_splits = line.split("\t") #0: ID, 1: sentence
        t = Token(line_splits[1][0:-1]) # [0:-1] to remove the `\n'
        subtokens, categories, spaces = t.subtokenize()

        for i in range(len(subtokens)):
            subtk_line = line_splits[0] + '\t' + subtokens[i] + '\t' + str(spaces[i]) + '\t'+ categories[i] + '\t'
            subtk_file.write(subtk_line)
            subtk_file.write('\n')
        subtk_file.write('\n')

    subtk_file.close()
        

def main():
    t = Token("But Congress didn't anticipate or intend more public debt, say opponents of the RTC's working-capital plan, and Rep. Charles Schumer (D., N.Y.) said the RTC Oversight Board has been remiss in not keeping Congress informed.")
    t = Token("He Cannot go to school, today! Wow, why he wouldn't?")
    subtokens, categories, spaces = t.subtokenize()

    for i in range(len(subtokens)):
        print subtokens[i], '\t', categories[i], '\t', spaces[i], '\t'


    subtokenize_file(sys.argv[1])
    
if __name__ == '__main__':
    main()
