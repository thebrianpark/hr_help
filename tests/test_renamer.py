from renamer import Renamer
from database import EmployeeDatabase
import unittest

class RenamerTest(unittest.TestCase):

    def setUp(self):
        self.first_name = "Martha"
        self.last_name = "Tucker"
        self.company_name = "Trident Family"
        self.company_code = "L21"
        self.payroll_date = "1.25.22"
        self.formatted_filename = "L21 - Trident Family - Martha Tucker 1.25.22"
        self.db = EmployeeDatabase('../Employee-Tracking-Status-2022-Payroll.csv')
        self.target_dir = '/User/brianpark/hr_stuff/'
        self.renamer = Renamer(self.payroll_date, self.db, self.target_dir)

    def test_get_new_filename(self):
        filename = self.target_dir + "Martha Tucker.jpg"
        expected = "/User/brianpark/hr_stuff/L21 - Trident Family - Martha Tucker 1.25.22.jpg"
        actual = self.renamer.get_new_filename(filename)
        self.assertEqual(expected, actual)

