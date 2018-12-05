from models.Employee import Empolyee
from repositories.EmployeeRepository import EmployeeRepository


from models.Employee import Empolyee
def main():
    empRepo = EmployeeRepository()
    emps = empRepo.get_employees()
    print(emps)

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