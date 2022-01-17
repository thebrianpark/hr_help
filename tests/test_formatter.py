from formatter import Formatter
import unittest

class FormatterTest(unittest.TestCase):

    def setUp(self):
        self.first_name = "Martha"
        self.last_name = "Tucker"
        self.company_name = "Trident Family"
        self.company_code = "L21"
        self.payroll_date = "1.25.22"
        self.formatted_filename = "L21 - Trident Family - Martha Tucker 1.25.22"
        self.formatter = Formatter(self.payroll_date)

    def test_format_name(self):
        actual = self.formatter.format_name(
                self.company_code,
                self.company_name,
                self.first_name,
                self.last_name,
        )
        self.assertEqual(self.formatted_filename, actual)

