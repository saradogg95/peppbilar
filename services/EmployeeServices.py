from models.Employee import Employee

from repositories.EmployeeRepo import EmployeeRepository 


class EmployeeServices:

    def __init__(self):
        self.__repo = EmployeeRepository()
        self.__employees = []

        
    def add_employee(self, new_employee):
        self.__repo.add_employee(new_employee)
