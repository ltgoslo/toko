# -*- coding: utf-8 -*-


import os
import sys
import subprocess
from subprocess import Popen, PIPE
from subtoken import Subtoken
import inspect


delimiter = '\n'

def classify_file(file_name):
    subtokenize_file(file_name)
    result = call_wapiti()
    write_output(file_name+"tokens", result)

def subtokenize_file(file_name):
    subtk_file = open("../tmp/tmp.subtks", "w")
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
    

def call_wapiti():
    wapiti_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '/../bin/wapiti-1.4.0/'
    input_path = "../../tmp/tmp.subtks"
    
    args = ['./wapiti', 'label', '-m', 'ptb.model', input_path]
    wapiti_proc = subprocess.Popen(args,cwd=wapiti_dir, stdout=PIPE)

    return wapiti_proc.stdout.readlines()



def write_output(out_file_name, wapiti_ouptut):
    out_file = open(out_file_name, "w")
    word = ""

    for l in wapiti_ouptut:
        columns = l.split("\t")
        word = ""
        
        if len(columns) < 2:
            out_file.write('\n')

        else:
            if columns[-1] == "SPLIT":
                word += columns[1]
                out_file.write(word)
                out_file.write(delimiter)
                word = ""
                
            else:
                word += columns[1]

    out_file.close()
        
    
    
    
