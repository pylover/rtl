# -*- coding: utf-8 -*-
from .pretty_printer import PrettyRtlPrinter
__author__ = 'vahid'


def pprint(obj, stream=None, indent=1, width=80, depth=None, compact=False):
    """Pretty-print a Python object to a stream [default is sys.stdout]."""
    printer = PrettyRtlPrinter(
        stream=stream, indent=indent, width=width, depth=depth,
        compact=compact)
    printer.pprint(obj)