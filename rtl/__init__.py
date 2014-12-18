# -*- coding: utf-8 -*-
from .reshaper import reshape
import sys
from bidi.algorithm import get_display
__author__ = 'vahid'
__version__ = '0.1.3'


def rtl(exp):
    exp = reshape(exp)
    exp = get_display(exp)
    return exp


def write(s):
    print s.encode('utf8')


def main():
    for l in sys.stdin.readlines():
        l = l.strip().decode('utf8').strip()
        if not l:
            print ''
            continue
        write(rtl(l))
