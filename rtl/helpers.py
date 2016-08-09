
from bidi.algorithm import get_display

from rtl import reshaper


def rtl(exp, reshape=True, bidi=True, digits=False):

    if reshape:
        exp = reshaper.reshape(exp, digits=digits)

    if bidi:
        exp = get_display(exp)

    return exp
