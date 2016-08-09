# -*- coding: utf-8 -*-
import unittest
from rtl.pretty_printer import PrettyRtlPrinter
import io
import sys
import warnings
__author__ = 'vahid'


class TestPrettyPrint(unittest.TestCase):

    def test_pretty_printer(self):

        if sys.version_info < (3, 0):
            warnings.warn("pprint test is not supported on python<3.")
            return

        output_buffer = io.StringIO()
        printer = PrettyRtlPrinter(stream=output_buffer)
        printer.pprint({
            u'سلام': u'درود',
            u'خداحافظ': u'بدرود',
            u'صبح': u'سحر',
        })

        output_buffer.seek(0)
        e = u"{'ﺮﺤﺳ' :'ﺢﺒﺻ' ,'ﺩﻭﺭﺩ' :'ﻡﻼﺳ' ,'ﺩﻭﺭﺪﺑ' :'ﻆﻓﺎﺣاﺪﺧ'}\n"
        b = output_buffer.read()
        self.assertEqual(b, e)


if __name__ == '__main__':
    unittest.main()
