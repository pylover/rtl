# -*- coding: utf-8 -*-

from pprint import PrettyPrinter

from rtl.reshaper import reshape
from bidi.algorithm import get_display


class PrettyRtlPrinter(PrettyPrinter):

    def format(self, obj, context, maxlevels, level):
        repr_string, isreadable, isrecursive = PrettyPrinter.format(self, obj, context, maxlevels, level)

        if isreadable:
            repr_string = reshape(repr_string, digits=False)
            repr_string = get_display(repr_string)

        return repr_string, isreadable, isrecursive
