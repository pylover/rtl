# -*- coding: utf-8 -*-

from __future__ import print_function
import sys

from rtl.compat import pprint, process_streams
from rtl.helpers import rtl
from rtl.pretty_printer import PrettyRtlPrinter

__version__ = '0.4.3'


def write(s):
    print(s.encode('utf8'))


def main():
    process_streams(sys.stdin, sys.stdout)
    # for l in sys.stdin.readlines():
    #     l = l.strip().decode('utf8').strip()
    #     if not l:
    #         print('')
    #         continue
    #     write(rtl(l))
