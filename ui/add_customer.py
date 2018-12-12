from os import system, name
from services.CarServices import CarServices
from services.CustomerServices import CustomerServices
from services.EmployeeServices import EmployeeServices
from services.OrderServices import OrderServices
#from services.PaymentServices import PaymentServices verður sennilega ekki notað
from datetime import datetime
from datetime import date
import calendar

from models.Car import Car
from models.Order import Order
from models.Employee import Employee
from models.Payment import Payment
from models.Customer import Customer

class test:
    def __init(self):
        self.__car_service = CarServices()
        self.__customer_service = CustomerServices()
        self.__employee_service = EmployeeServices()
        self.__order_service = OrderServices()
        self.__today = date.today()
        self.__menu_action = ""
        self.__max_kilometer_per_day = 100

    def returning_customer(self):

        def identity_number_check():
            while True:
                identity_number = input("Enter valid identity number: ")
                try:
                    if identity_number[-1] == '9':
                        reference_year = 1900
                    elif identity_number[-1] == '0':
                        reference_year = 2000
                    else:
                        print("Wrong input.")
                        continue
                    birthday_day = int(identity_number[0:2])
                    birthday_month = int(identity_number[2:4])
                    birthday_year = int(identity_number[4:6]) + reference_year
                    birthday = datetime.date(birthday_year, birthday_month, birthday_day)
                    return identity_number
                except:
                    print("{} is not a valid kennitala!".format(identity_number))
                    
        def customer_id_check():
            while True:
                try:
                    customer_id = int(input("Please input customer id: "))
                    return customer_id
                except ValueError:
                    print("Wrong input.")
        
        print("Please press 1 to add new customer.")
        print("Please press 2 to find costumer.")

        def get_user_input():
            while True:
                try:
                    customer_input = int(input("Option: "))
                    if customer_input == 1 or customer_input == 2:
                        return customer_input
                    else:
                        print("Please 1 or 2 for your choice.")
                except ValueError:
                    print("Wrong input.")

        user_choice = get_user_input()

        if user_choice == 1:
            customer_id = customer_id_check()
            identity_number = identity_number_check()
            first_names = input("Please input first name: ")
            surname = input("Please input last name: ")
            citizenship = input("Please input citizenship: ")
            passport_id = input("Please input passport id: ")        
            credit_card_no = input("Please input credit card number: ")
            new_customer = Customer(customer_id, identity_number, 
                                    first_names, surname, citizenship, passport_id, credit_card_no) 
            self.__customer_service.add_customer(new_customer)
            return new_customer

        elif user_choice == 2:
            print("Press 1 to find customer after identity number.")
            print("Press 2 to find customer after passport id.")
            user_choice = get_user_input()
            if user_choice == 1:
                id_num = input("Please input identity number: ")
                customer = self.__customer_service.get_customer_after_id_num_or_pass_id(identity_number=id_num)
                print(customer[0])
            elif user_choice == 2:
                pass_id = input("Please input passport id: ")
                customer = self.__customer_service.get_customer_after_id_num_or_pass_id(passport_id=pass_id)
                print(customer[0])
            
def main():
    ui = test()
    ui.returning_customer()



