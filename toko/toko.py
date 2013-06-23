#!/usr/bin/env python
# -*- coding: utf-8 -*-

#from argparse import ArgumentParser
from token import Token

def main():
    t = Token("But Congress didn't anticipate or intend more public debt, say opponents of the RTC's working-capital plan, and Rep. Charles Schumer (D., N.Y.) said the RTC Oversight Board has been remiss in not keeping Congress informed.")
    a, b = t.subtokenize()

    for i in range(len(a)):
        print a[i], '\t', b[i]

if __name__ == '__main__':
    main()
