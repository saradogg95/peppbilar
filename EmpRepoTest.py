from repositories.EmployeeRepository import EmployeeRepository
from models.Employee import Employee


def main():
    employee = Employee("Halli Einars", "2302895639" "123", "Halli da pimp", "kjkj", 29, 0)

    empRepo = EmployeeRepository()
    empRepo.add_employee(employee);
    print(empRepo.get_employees())


main()