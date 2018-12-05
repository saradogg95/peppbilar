from models.Employee import Employee
import csv

class EmployeeRepository:
    def __init__(self):
        self.__employee = []

    def __str__(self):
        return "{}".format(self.__employee)

    def __repr__(self):
            return self.__str__()
    
    def add_Employee(self, employee):
        with open("./data/employee.txt", "a+") as employee_file:
            name = employee.get_name()
            age = employee.get_age()
            address = employee.get_address()
            username = employee.get_user_name()
            password = employee.get_password()
            admin = employee.get_admin()
            employee_file.write("{},{},{},{},{},{} \n".format(name, age, address, username, password, admin))

 
    def get_employees(self):
        if self.__employee == []:
            with open("./data/Employees.csv", "r") as employee_file:
                csv_reader = csv.reader(employee_file, delimiter=";")
                for line in csv_reader:
                    self.__employee.append(line)        
        return self.__employee
    

