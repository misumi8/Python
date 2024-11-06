# 4 ------------------------------------------------
# Build an employee hierarchy with a base class Employee.
# Create subclasses for different types of employees like Manager, Engineer, and Salesperson.
# Each subclass should have attributes like salary and methods related to their roles

class Employee:
    def __init__(self, name, salary):
        self.salary = salary
        self.name = name
    def __lt__(self, other):
        return int(self) < int(other)

class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
    def raise_salary(self, obj_employee, amount):
        if (obj_employee != self and isinstance(obj_employee, Employee)):
            obj_employee.salary += amount
    def cut_salary(self, obj_employee, amount):
        if(obj_employee != self and isinstance(obj_employee, Employee)):
            obj_employee.salary -= amount
    def __int__(self): return 0
    def __str__(self):
        return "[Manager] " + self.name + ": " + str(self.salary)

class Engineer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
        self.invented = []
    def invent(self, thing):
        self.invented.append(thing)
    def __int__(self): return 1
    def __str__(self):
        return "[Engineer] " + self.name + ": " + str(self.salary)

class Salesperson(Employee):
    def __init__(self, name, salary, sales_amount = 0):
        super().__init__(name, salary)
        self.sales_amount = sales_amount
    def sell(self, amount):
        self.sales_amount += amount
    def __int__(self): return 2
    def __str__(self):
        return "[Salesperson] " + self.name + ": " + str(self.salary)

employees = [Salesperson("Nicu", 2700), Manager("Ionut", 4900), Salesperson("Semion", 4550), Manager("Ion", 5000), Engineer("Maria", 4500)]
employees[1].raise_salary(employees[0], 500)
print("Employee hierarchy:")
for i in sorted(employees):
    print("  " * int(i), i)
