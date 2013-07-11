# -*- coding: utf-8 -*-

import os
import sys
from subtoken import Subtoken
import inspect


def prepare_file(file_name):
    wp_file = train_subtokenize_file(file_name)            

def train_subtokenize_file(file_name):
    '''
    This method produces subtokens for the 'train' mode; 
    it assumes an input file with one token per line, however it can
    handle sentence-ID \tab token per line.
    If there is no sentence-ID the function will assign one for
    each.
    Sentence are separated by newlines.
    '''

    wp_file_name = file_name + ".wptks"

    subtk_file = open(wp_file_name, "w")
    raw_lines = [line for line in open(file_name)]
    
    if len( raw_lines[0].split('\t') ) == 1:
        sentence_id = 0
        for line in raw_lines:
            if len(line) > 1:
                line_splits = line.split("\t") 
                t = Subtoken(line_splits[0][0:-1]) # [0:-1] to remove the `\n'
                subtokens, categories, spaces = t.subtokenize()
            
                # the gold standard files contain one token per line, 
                # each token is subtokenized, then between each pair
                # of subtokens (within one gold token) there must be
                # a NONSPLIT:
                for i in range(len(subtokens) - 1):
                    subtk_line = str(sentence_id) + '\t' + \
                        subtokens[i] + '\t' + str(spaces[i]) + \
                        '\t'+ categories[i] + '\t' + str(len(subtokens[i])) +\
                        '\t' + "NONSPLIT"
                    subtk_file.write(subtk_line)
                    subtk_file.write('\n')

                # and finally the last subtoken is a SPLIT:
                j = len(subtokens) - 1
                subtk_line = str(sentence_id) + '\t' + \
                    subtokens[j] + '\t' + str(spaces[j]) + \
                    '\t'+ categories[j] + '\t' + str(len(subtokens[j])) +\
                    '\t' + "SPLIT"
                subtk_file.write(subtk_line)
                subtk_file.write('\n')                
            else:
                sentence_id += 1
                subtk_file.write('\n')

    elif len( raw_lines[0].split('\t') ) == 2:
        for line in raw_lines:
            if len(line) > 1:
                line_splits = line.split("\t") 
                t = Subtoken(line_splits[1][0:-1]) # [0:-1] to remove the `\n'
                subtokens, categories, spaces = t.subtokenize()

                for i in range(len(subtokens) - 1):
                    subtk_line = line_splits[0] + '\t' + subtokens[i] +\
                        '\t' + str(spaces[i]) +\
                        '\t' + categories[i] + '\t' + str(len(subtokens[i])) +\
                        '\t' + "NONSPLIT"
                    subtk_file.write(subtk_line)
                    subtk_file.write('\n')
                    
                j = len(subtokens) - 1
                subtk_line = line_splits[0] + '\t' + subtokens[j] +\
                    '\t' + str(spaces[j]) +\
                    '\t' + categories[j] + '\t' + str(len(subtokens[j])) +\
                    '\t' + "SPLIT"
                subtk_file.write(subtk_line)
                subtk_file.write('\n')
            else:
                subtk_file.write('\n')


    else:
        print "toko is expecting one sentence per line or one sentence-ID and sentence per line (separated by a tab). Please double-check the input file."
        exit(1)

    subtk_file.close()
    return wp_file_name
