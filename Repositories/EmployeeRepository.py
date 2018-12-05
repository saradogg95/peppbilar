import models.Empolyee from Employee




class EmployeeRepository:
    def __init__(self):
        self.__employee = []

    def __str__(self):
        return "{}".format(self.__employee)

    def __repr__(self):
            return self.__str__()
    
    def add_Employee(self, employee):
        with open("./data/employee.txt", "a+") as employee_file:
            name = employees.get_name()
            age = employees.get_age()
            address = employees.get_address()
            username = employees.get_user_name()
            password = employees.get_password()
            admin = employees.get_admin()
            employee_file.write("{},{},{}\n".format(name, age, address, username, password, admin))
    
    def get_employees(self):
        if self.__employee == []:
            with open("./data/employee.txt", "r") as video_file:
                for line in video_file.readlines():
                    name, age, address, username, password, admin = line.split(",")
                    new_employee = Employee(username, password, name, address, age, admin=0)
                    self.__employee.append(new_video)    
        
        return self.__employee
    

