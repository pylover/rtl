# -*- coding: utf-8 -*-
from pprint import PrettyPrinter
from rtl import rtl
__author__ = 'vahid'


class PrettyRtlPrinter(PrettyPrinter):

    def format(self, obj, context, maxlevels, level):
        repr_string, isreadable, isrecursive = PrettyPrinter.format(self, obj, context, maxlevels, level)
        return \
            rtl(repr_string) if isreadable else repr_string, \
            isreadable, \
            isrecursive
