from models.Employee import Empolyee

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
            with open("./data/employee.txt", "r") as video_file:
                for line in video_file.readlines():
                    name, age, address, username, password, admin = line.split(",")
                    new_employee = Employee(username, password, name, address, age, admin)
                    self.__employee.append(new_employee)    
        
        return self.__employee
    

