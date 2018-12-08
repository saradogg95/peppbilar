from os import system, name
from services.CarServices import CarServices
from services.CustomerServices import CustomerServices
from services.EmployeeServices import EmployeeServices
from services.OrderServices import OrderServices
from services.PaymentServices import PaymentServices

from models.Car import Car
from models.Order import Order
from models.Employee import Employee
from models.Payment import Payment
from models.Customer import Customer


class UserInterface:
    def __init__(self):
        self.__car_service = CarServices()
        self.__customer_service = CustomerServices()
        self.__employee_service = EmployeeServices()
        self.__order_service = OrderServices()
        self.__payment_service = PaymentServices()
        self.__menu_action = ""

    def clear_screen(self):
        # for windows 
            if name == 'nt': 
                _ = system('cls') 
        # for mac and linux(here, os.name is 'posix') 
            else: 
                _ = system('clear')
    
    def main_menu(self):
        while self.__menu_action.lower() != "q":
            self.clear_screen()
            print("\n" * 10)
            print("{:>100}".format("PEPP BÍLAR"))
            print("{:>115}".format("-" * 40))
            print("{:>100}".format("Main menu\n"))
            print("{:>100}".format("1. Order menu"))
            print("{:>103}".format("2. Customer menu"))
            print("{:>102}".format("3. Payment menu"))
            print("{:>98}".format("4. Car menu"))
            print("{:>103}".format("5. Employee menu"))
            print("{:>102}".format("Q. Quit program"))
            print("\n" * 2)
            self.__menu_action = input("{:>95}".format("Enter menu action: "))

            if self.__menu_action == "1":
                self.order_menu()
            if self.__menu_action == "2":
                self.customer_menu()
            if self.__menu_action == "3":
                self.payment_menu()


    def order_menu(self):
        """ Order menu for the system. Its menu functions are nested methods within this method. """
        def place_order():
            """ Menu method for placing a new order. """
            leave_place_order = ""
            confirm_order = ""
            while leave_place_order.lower() != "n":
                self.clear_screen()
                print("\n" * 10)
                print("{:>100}".format("PEPP BÍLAR"))
                print("{:>115}".format("-" * 40))
                print("{:>105}".format("Place a new order:\n"))
                print("\n" * 2)
                order_id = input("{:>95}".format("Enter order id: "))
                order_date = input("{:>95}".format("Enter order date: "))
                rent_date_from = input("{:>95}".format("Enter first date of rent: "))
                rent_date_to = input("{:>95}".format("Enter last day of rent: "))
                customer_id = input("{:>95}".format("Enter customer id: "))
                car_id = input("{:>95}".format("Enter car registration number: "))
                confirm_order = input("{:>95}".format("Complete order? (y/n): "))
                if confirm_order.lower() == "y":
                    new_order = Order(order_id, order_date, rent_date_from, rent_date_to, customer_id, car_id)
                    self.__order_service.add_order(new_order)
                leave_place_order = input("{:>95}".format("Place another order? (y/n): "))



        def change_order():
            pass
        
        def delete_order():
            pass

        while self.__menu_action.lower() != "b":
            self.clear_screen()
            print("\n" * 10)
            print("{:>100}".format("PEPP BÍLAR"))
            print("{:>115}".format("-" * 40))
            print("{:>101}".format("Order menu\n"))
            print("{:>101}".format("1. Place order"))
            print("{:>102}".format("2. Change order"))
            print("{:>102}".format("3. Delete order"))
            print("{:>107}".format("B. Back to main menu"))
            print("\n" * 2)
            self.__menu_action = input("{:>95}".format("Enter menu action: "))

            if self.__menu_action == "1":
                place_order()
            if self.__menu_action == "2":
                change_order()
            if self.__menu_action == "3":
                delete_order()

    def customer_menu(self):
        pass


    def payment_menu(self):
        while self.__menu_action.lower() != "b":
            self.clear_screen()

    def write_to_db(self):
        """ Writes all databases to files. Call this method before program ends. """
        self.__order_service.write_db_to_file()