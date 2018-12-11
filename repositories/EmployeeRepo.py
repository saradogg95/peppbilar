from models.Employee import Employee

import csv


class EmployeeRepository:
    
    def __init__(self):
        self.__employee = []

        
    def __str__(self):
        return "{}".format(self.__employee)

    
    def __repr__(self):
            return self.__str__()
    
    
    def add_employee(self, employee):
        """Open file and write employee object attributes to empolyee files, which
           include employee data."""
        try:
            with open("./data/employee.csv", "a+") as employee_file:
                try:     
                    name = employee.get_name()

                    #If SSN is missing, an exception is thrown
                    if employee.get_ssn() == "":
                        raise Exception
                    else:
                        ssn = employee.get_ssn()

                    age = employee.get_age()
                    address = employee.get_address()
                    username = employee.get_name()
                    password = employee.get_password()
                    admin = employee.get_admin_status()
                    employee_file.write("{},{},{},{},{},{},{} \n".format
                                        (name, ssn, age, address, username, 
                                         password, admin))
                    return None
                except:
                    print("Something wrong")
                finally:
                    employee_file.close()
        except:
            print("File Error!")
 

    def get_employees(self):
        """Method returns all employees"""
        if self.__employee == []:
            with open("./data/employee.csv", "r") as employee_file:
                try:
                    csv_reader = csv.reader(employee_file, delimiter=",")
                    next(csv_reader)
                    for line in csv_reader:
                        self.__employee.append(line)      
                    return self.__employee
                except:
                    print("No employee data available")
                finally:
                    employee_file.close()
