from formatter import Formatter
from database import EmployeeDatabase
import os

class Renamer:
    def __init__(self, payroll_date, emp_database, target_dir):
        self.payroll_date = payroll_date
        self.emp_database = emp_database
        self.formatter = Formatter(payroll_date)
        self.target_dir = target_dir

    def rename_file(self, base_filename):
        emp_info = os.path.basename(base_filename)
        elements = emp_info.split()
        num_elements = len(elements)
        if num_elements > 3:
            print("file name has {} elements, which is too many.".format(num_elements))
            raise ValueError
        first_name = elements[0]
        last_name = elements[1]
        company_code = elements[2] if num_elements == 3 else None
        emp = self.emp_database.get_employer(first_name, last_name, company_code)
        if emp is None:
            print("Employee not found: {} {} - company code: {}".format(first_name, last_name, company_code))
            raise ValueError
        new_filename = self.formatter.format_name(
                emp.company_code,
                emp.company_name,
                emp.first_name,
                emp.last_name,)
        filename = self.target_dir + "/" + base_filename
        new_filename = self.target_dir + "/" + new_filename
        os.rename(filename, new_filename)
        print("Renamed '{}' to '{}'".format(filename, new_filename))

if __name__ == '__main__':
    db = EmployeeDatabase('Employee-Tracking-Status-2022-Payroll.csv')
    target_dir = 'tests'
    renamer = Renamer("1.25.22", db, target_dir)
    renamer.rename_file("Zachary Lovett")

