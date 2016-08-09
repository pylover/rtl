
import sys
from rtl import helpers


if sys.version_info >= (3, 0):
    # Python 3

    from rtl._pprint_py3 import pprint

    def process_streams(input_file, output_file, reshape=True, bidi=True, digits=False):
        for l in input_file.readlines():
            if not l.strip():
                output_file.write('\n')
                continue

            if isinstance(l, bytes):
                l = l.decode()

            output_file.write(helpers.rtl(l, reshape=reshape, bidi=bidi, digits=digits))

else:
    # Python 2

    from rtl._pprint_py2 import pprint

    def process_streams(input_file, output_file, reshape=True, bidi=True, digits=False):
        for l in input_file.readlines():
            l = l.decode('utf8')

            if not l.strip():
                output_file.write('\n')
                continue

            output_file.write(helpers.rtl(l, reshape=reshape, bidi=bidi, digits=digits))
