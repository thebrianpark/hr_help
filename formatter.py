class Formatter:

    def __init__(self, payroll_date):
        self.payroll_date = payroll_date

    def format_name(self, company_code, company_name,
                    first_name, last_name):
        return "{0} - {1} - {2} {3} {4}".format(
                company_code, company_name,
                first_name, last_name, self.payroll_date)

if __name__ == '__main__':
    formatter = Formatter("1.25.22")
    print(formatter.format_name("L21", "Trident Family",
                                "Martha", "Tucker"))
