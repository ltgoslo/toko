#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os import getcwd
import sys
import subprocess
from subprocess import call


def test(arg1):
    print "Hi, this is me trying!"
    





def main():
    
    test(sys.argv[1])
    #subprocess.check_output(["./wapiti"])
    #subprocess.call(["./wapiti-1.4.0/wapiti"])
    #print(a)
    
    wapiti_dir = os.getcwd() + '/wapiti-1.4.0/'
    args = ['./wapiti']
    subprocess.Popen(args,cwd=wapiti_dir)
    



if __name__ == "__main__":
    main()
