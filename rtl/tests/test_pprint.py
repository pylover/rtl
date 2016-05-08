# -*- coding: utf-8 -*-
import unittest
from rtl.pretty_printer import PrettyRtlPrinter
import io
import sys
__author__ = 'vahid'


class TestPrettyPrint(unittest.TestCase):

    def test_pretty_printer(self):

        if sys.version_info < (3, 0):
            raise Exception("This test is not supported on python<3.")

        buffer = io.StringIO()
        printer = PrettyRtlPrinter(stream=buffer)
        printer.pprint({
            u'سلام': u'درود',
            u'خداحافظ': u'بدرود',
            u'صبح': u'سحر',
        })

        buffer.seek(0)
        e = u"{'ﺮﺤﺳ' :'ﺢﺒﺻ' ,'ﺩﻭﺭﺩ' :'ﻡﻼﺳ' ,'ﺩﻭﺭﺪﺑ' :'ﻆﻓﺎﺣاﺪﺧ'}\n"
        b = buffer.read()
        self.assertEqual(b, e)


if __name__ == '__main__':
    unittest.main()
