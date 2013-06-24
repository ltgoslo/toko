#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
#from os import getcwd
import sys
import subprocess
from subprocess import call
import inspect

def test(arg1):
    print "Hi, this is me trying!"
    





def main():
    #subprocess.check_output(["./wapiti"])
    #subprocess.call(["./wapiti-1.4.0/wapiti"])
    #print(a)
    
    wapiti_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '/../bin/wapiti-1.4.0/'
    
    args = ['ls']
    #subprocess.Popen(args,cwd='../../')
    print os.path.abspath( __file__ )
    print wapiti_dir


if __name__ == "__main__":
    main()
