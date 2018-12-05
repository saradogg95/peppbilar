#from models.Employee import Employee
from repositories.EmployeeRepository import EmployeeRepository
from models.Employee import Employee


def main():
    employee = Employee("kalli", "123", "Ari", "kjkj", 29)

    empRepo = EmployeeRepository()
    print(empRepo.get_employees())
    print(employee.get_age())
    print(employee.get_name())

    #car1 = Car()
    #print(car1)
    #car_db.add_car(car1)

    #all_cars = car_db.get_all_cars()
    #for car in all_cars:
    #    print(car)

    #available_cars = car_db.get_available_cars()
    #for car in available_cars:
    #    print(car)
    #print(available_cars)


main()