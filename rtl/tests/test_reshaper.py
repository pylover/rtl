# -*- coding: utf-8 -*-
import unittest
from rtl import rtl
__author__ = 'vahid'


class TestReshaper(unittest.TestCase):

    def setUp(self):
        self.expression_persian = u'گگگ گ پپپ پ ژ پژ چچچ چ'
        self.expression_english = u'abcdefghi'

    def test_reshaper(self):
        exp = rtl(self.expression_persian)
        expected_exp = u"ﭺ ﭻﭽﭼ ﮋﭘ ﮊ ﭖ ﭗﭙﭘ ﮒ ﮓﮕﮔ"
        self.assertEqual(exp, expected_exp)
        self.assertNotEqual(exp, self.expression_persian)

        exp = rtl(self.expression_english)
        self.assertEqual(exp, self.expression_english)

    def test_digits(self):
        result = rtl('1234567890', digits=True)
        expected = u'١٢٣٤٥٦٧٨٩٠'
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
