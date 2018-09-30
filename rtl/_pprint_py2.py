from .pretty_printer import PrettyRtlPrinter


def pprint(obj, stream=None, indent=1, width=80, depth=None, compact=False):
    """Pretty-print a Python object to a stream [default is sys.stdout]."""
    printer = PrettyRtlPrinter(
        stream=stream, indent=indent, width=width, depth=depth
    )
    printer.pprint(obj)

