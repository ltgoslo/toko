# -*- coding: utf-8 -*-


import os
from os import remove
import sys
import subprocess
from subprocess import Popen, PIPE
from subtoken import Subtoken
import inspect

sys.path.insert(0, '../config/')
import tokosettings


delimiter = '\n'
wapiti_dir = tokosettings.config['wapiti']

def wp_classify_file(file_name):
    '''
    takes a `raw' file as an input (one sentence per line) and outputs
    a file (.tokens) with one token per line and empty lines between
    sentences
    '''
    wp_file = subtokenize_file(file_name)
    result = call_wapiti(wp_file)
    write_output(file_name+".tokens", result)
    os.remove(wp_file)

def subtokenize_file(file_name):
    wp_file_name = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))+"tmp.subtks"
    subtk_file = open(wp_file_name, "w")
    raw_lines = [line for line in open(file_name)]
    
    for line in raw_lines:
        line_splits = line.split("\t") #0: ID, 1: sentence
        t = Subtoken(line_splits[1][0:-1]) # [0:-1] to remove the `\n'
        subtokens, categories, spaces = t.subtokenize()

        for i in range(len(subtokens)):
            subtk_line = line_splits[0] + '\t' + subtokens[i] + '\t' + str(spaces[i]) \
            + '\t'+ categories[i] + '\t' + str(len(subtokens[i])) + '\t'
            subtk_file.write(subtk_line)
            subtk_file.write('\n')
        subtk_file.write('\n')

    subtk_file.close()
    return wp_file_name

def call_wapiti(wp_file_name):    
    input_path = wp_file_name
    wp_model = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '/../models/ptb.model'
    
    args = ['./wapiti', 'label', '-m', wp_model, input_path]
    wapiti_proc = subprocess.Popen(args,cwd=wapiti_dir, stdout=PIPE)#, stderr=PIPE)
    
    return wapiti_proc.stdout.readlines()



def write_output(out_file_name, wapiti_output):
    '''
    reads the output of wapiti and writes a new file with each token
    on one line
    
    '''
    out_file = open(out_file_name, "w")
    word = ""

    for l in wapiti_output:
        columns = l.split("\t")        
        
        if len(columns) < 2:
            out_file.write('\n')

        else:
            word += columns[1]
            if columns[2] == "1": #if the word is followed by a whitespace
                word += " "
            
            if columns[-1][0:-1] == "SPLIT":                
                out_file.write(word)
                out_file.write(delimiter)
                word = ""
                

    out_file.close()
        
    
    
    
def wp_classify():
    wp_classify_file(sys.argv[1])


    
if __name__ == '__main__':
    wp_classify()
