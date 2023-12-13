from employee import Employee, SalaryEmployee, HourlyEmployee, CommissionEmployee

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        print('Current Employees:')
        for i in self.employees:
            print(i.first_name, i.last_name)
        print('---------------------')

    def pay_employees(self):
        print('Paying Employees:')
        for i in self.employees:
            print('Paycheck for:', i.first_name, i.last_name)
            print(f'Amount: ${i.calculate_paycheck():,.2f}')
            print('----------------------------')
            

def main():
    my_company = Company()

    employee1 = SalaryEmployee('Trace', 'Dugar', 38000)
    my_company.add_employee(employee1)
    employee2 = SalaryEmployee('Tommy', 'Boudreaux', 39000)
    my_company.add_employee(employee2)
    employee3 = SalaryEmployee('John', 'Smith', 58000)
    my_company.add_employee(employee3)
    employee4 = HourlyEmployee('Samantha', 'Landry', 40, 30)
    my_company.add_employee(employee4)
    employee5 = HourlyEmployee('Trent', 'Romero', 40, 55)
    my_company.add_employee(employee5)
    employee6 = CommissionEmployee('Sarah', 'Batiste', 30000, 5, 1000)
    my_company.add_employee(employee6)

    my_company.display_employees()
    my_company.pay_employees()


main()
