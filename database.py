from employee import Employee
import csv

class EmployeeDatabase:
    def __init__(self, filename):
        self.employees = []
        with open(filename) as csvfile:
            employee_reader = csv.DictReader(csvfile)
            for row in employee_reader:
                first_name = row['First'].strip()
                last_name = row['Last'].strip()
                company_code = row['ADP'].strip()
                company_name = row['FGM'].strip()
                name = first_name + " " + last_name
                emp = Employee(first_name, last_name,
                                company_name, company_code)
                self.employees.append(emp)

    def get_employer(self, first_name, last_name, company_code=None):
        for employer in self.employees:
            if employer.first_name == first_name and employer.last_name == last_name:
                if company_code == None:
                    return employer
                elif employer.company_code == company_code:
                    return employer
        return None

if __name__ == '__main__':
    db = EmployeeDatabase('Employee-Tracking-Status-2022-Payroll.csv')
    print(db.employees)
    print(db.employees[0].first_name)
    print(db.employees[0].last_name)
    print(db.employees[0].company_name)
    print(db.employees[0].company_code)
