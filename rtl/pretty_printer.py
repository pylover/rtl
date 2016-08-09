# -*- coding: utf-8 -*-

from pprint import PrettyPrinter

from rtl import helpers


class PrettyRtlPrinter(PrettyPrinter):

    def format(self, obj, context, maxlevels, level):
        repr_string, isreadable, isrecursive = PrettyPrinter.format(self, obj, context, maxlevels, level)

        if isreadable:
            repr_string = helpers.rtl(repr_string)

        return repr_string, isreadable, isrecursive
