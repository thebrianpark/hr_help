from renamer import Renamer
import os

def main():
    db = EmployeeDatabase('Employee-Tracking-Status-2022-Payroll.csv')
    target_dir = '~/hr_stuff'
    renamer = Renamer("1.25.22", db, target_dir)
    for file_name in os.listdir(target_dir):
        renamer.rename_file(filename)
