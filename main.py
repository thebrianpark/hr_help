from renamer import Renamer
from database import EmployeeDatabase
import os

def main():
    db = EmployeeDatabase('../Employee-Tracking-Status-2022-Payroll.csv')
    target_dir = '/Users/brianpark/hr_stuff'
    renamer = Renamer("1.25.22", db, target_dir)
    for filename in os.listdir(target_dir):
        try:
            print("Working on filename: {}".format(filename))
            full_path = os.path.join(target_dir, filename)
            renamer.rename_file(full_path)
        except Exception:
            print("An error has occurred with a file. Skipping file: {}".format(filename))

if __name__ == '__main__':
    main()
