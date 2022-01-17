from renamer import Renamer
from database import EmployeeDatabase
import os

def main():
    payroll_date = input("Please enter payroll date exactly as you want to appear on the renamed files: ")
    db = EmployeeDatabase('../Employee-Tracking-Status-2022-Payroll.csv')
    target_dir = '/Users/brianpark/hr_stuff'
    renamer = Renamer(payroll_date, db, target_dir)
    for filename in os.listdir(target_dir):
        try:
            print("Working on filename: {}".format(filename))
            full_path = os.path.join(target_dir, filename)
            renamer.rename_file(full_path)
        except Exception:
            print("An error has occurred with a file. Skipping file: {}".format(filename))

if __name__ == '__main__':
    main()
