# -*- coding: utf-8 -*-


import os
import sys
import subprocess
from subprocess import call, Popen
import inspect

def classify_file(file_name):
    subtokenize_file(file_name)
    call_wapiti(file_name + ".subtks")


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
    

def call_wapiti(file_name):
    wapiti_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '/../bin/wapiti-1.4.0/'
    #print wapiti_dir
    
    #subprocess.check_output(["./wapiti"])
    #subprocess.call(["./wapiti-1.4.0/wapiti"])
    #print(a)
    
    #wapiti_dir = os.getcwd() + '/wapiti-1.4.0/'
    args = ['./wapiti', 'label', '-m', 'ptb.model']
    subprocess.Popen(args,cwd=wapiti_dir)
    
