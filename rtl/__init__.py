# -*- coding: utf-8 -*-
from __future__ import print_function
from .reshaper import reshape, reshape_digits
import sys
from bidi.algorithm import get_display
__author__ = 'vahid'
__version__ = '0.3.0'


def rtl(exp, digits=False):
    exp = reshape(exp)
    exp = get_display(exp)
    if digits:
        return reshape_digits(exp)
    return exp


def write(s):
    print(s.encode('utf8'))


def main():
    for l in sys.stdin.readlines():
        l = l.strip().decode('utf8').strip()
        if not l:
            print('')
            continue
        write(rtl(l))
