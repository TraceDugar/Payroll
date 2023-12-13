class Employee:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        

class SalaryEmployee(Employee):
    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary

    def calculate_paycheck(self):
         return self.salary/52*2

class HourlyEmployee(Employee):
    def __init__(self, first_name, last_name, weekly_hours, hourly_rate):
        super().__init__(first_name, last_name)
        self.weekly_hours = weekly_hours
        self.hourly_rate = hourly_rate

    def calculate_paycheck(self):
        return self.weekly_hours * self.hourly_rate * 2
   
class CommissionEmployee(SalaryEmployee):
    def __init__(self, first_name, last_name, salary, sales_number, commission_rate):
        super().__init__(first_name, last_name, salary)
        self.sales_number = sales_number
        self.commission_rate = commission_rate

    def calculate_paycheck(self):
        regular_salary = super().calculate_paycheck()
        total_commission = self.sales_number * self.commission_rate
        return regular_salary + total_commission
    


