# -*- coding: cp1251 -*-
"""name = input("Введите имя сотрудника: ")
salary = int(input("Введите зарплату сотрудника за месяц: "))

employee = {"name" : "Daniil","salary" : "120000"}
print(f'{employee["name"]} имеет зарплату в размере {employee.get("salary")}')
employee["age"] = 23
print(employee)"""



"""employee_list = [
    {
        "name": "Kate",
        "salary": "230000",
    },
    {
        "name": "Daniil",
        "salary": "420000",
    },
    {
        "name": "Alice",
        "salary": "315000",
    },
]
new_emloyee = {
    "name": "Alex",
    "salary": "120000",
}
for employee in employee_list:
    #print(f' У {employee["name"]} зарплата в размере {employee["salary"]}')
    if employee["name"] == "Daniil":
        employee_list.remove(employee)
        break
print(employee_list)
employee_list.append(new_emloyee)
print(employee_list)
print(len(employee_list))"""






"""class Employee:
    name = "Kate"
    salary = "300000"
    on_vacation = False

employee = Employee()
print(employee.name)
print(employee.salary)
print(employee.on_vacation)

employee.name = "Daniil"
employee.salary = "200000"
print(employee.name)
print(employee.salary)
print(employee.on_vacation)"""




"""class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.on_vacation = False

    def get_info(self):
        return f"У {employee.name} зарплата {employee.salary}, отпуск: {employee.on_vacation}"

employee_list = {
    Employee("Kate", 300000),
    Employee("Daniil", 400000),
    Employee("Alice", 250000)
}
for employee in employee_list:
    print(employee.get_info())"""







"""class Employee:
    def __init__(self, name, salary, on_vacation):
        self.name = name
        self.salary = salary
        self.on_vacation = on_vacation

    def get_info(self):
        return f"У {employee.name} зарплата {employee.salary}, отпуск: {employee.on_vacation}"

employee_list = {
    Employee("Kate", 300000, True),
    Employee("Daniil", 400000, True),
    Employee("Alice", 250000, False)
}
for employee in employee_list:
    print(employee.get_info())"""






class Employee:
    def __init__(self, name, salary, on_vacation, is_good_employee):
        self.name = name
        self.salary = salary
        self.on_vacation = on_vacation
        self.is_good_employee = is_good_employee

    def get_info(self):
        return f"У {employee.name} зарплата {employee.salary}, отпуск: {employee.on_vacation}, статус работника: {employee.is_good_employee}"

employee_list = {
    Employee("Nikita", 900000, False, True),
    Employee("Kate", 300000, True, True),
    Employee("Daniil", 400000, True, True),
    Employee("Alice", 250000, False, True),
    Employee("Ann", 700000, True, False)
}
for employee in employee_list:
    if not employee.is_good_employee:
        employee_list.remove(employee)
        break
    print(employee.get_info())
