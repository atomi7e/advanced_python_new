class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def get_salary(self):
        return self._salary

    def get_role(self):
        return "Employee"

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def get_role(self):
        return "Manager"

    def get_bonus(self):
        return self.bonus

def print_employee_info(employees):
    for emp in employees:
        role = emp.get_role()
        salary = emp.get_salary()
        print(f"Role: {role}, Name: {emp.name}, Salary: {salary}")
        
        if isinstance(emp, Manager):
            print(f"  -> Bonus: {emp.get_bonus()}")

emp1 = Employee("Ivan", 50000)
mgr1 = Manager("Petr", 80000, 15000)

staff = [emp1, mgr1]
print_employee_info(staff)