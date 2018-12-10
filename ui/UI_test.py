from os import system, name
from services.CarServices import CarServices
from services.CustomerServices import CustomerServices
from services.EmployeeServices import EmployeeServices
from services.OrderServices import OrderServices
#from services.PaymentServices import PaymentServices verður sennilega ekki notað
from datetime import date
import calendar

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
        #self.__payment_service = PaymentServices()
        self.__today = date.today()
        self.__menu_action = ""

    def clear_screen(self):
        # for windows 
            if name == 'nt': 
                _ = system('cls') 
        # for mac and linux(here, os.name is 'posix') 
            else: 
                _ = system('clear')
    
    def print_header(self):
        """ Prints the header file of the menu and resets the menu action comparsion string. """
        self.clear_screen()
        self.__menu_action = ""
        print("\n" * 10)
        print("{:>100}".format("PEPP BÍLAR"))
        print("{:>115}".format("-" * 40))
        print("{:>106}".format(self.__today.strftime("%A, %B, %Y")))
        print()

    def main_menu(self):
        """ Main menu. """
        while self.__menu_action.lower() != "q":
            self.print_header()
            print("{:>98}".format("1. Show available cars"))
            print("{:>89}".format("2. Find order"))
            print("{:>92}".format("3. Find customer"))
            print("{:>96}".format("4. Open car database"))
            print("{:>91}".format("Q. Quit program"))
            print("\n" * 2)
            self.__menu_action = input("{:>95}".format("Enter menu action: "))

            if self.__menu_action == "1":
                self.show_available_cars()
            if self.__menu_action == "2":
                self.find_order()
            if self.__menu_action == "3":
                self.find_customer()
            if self.__menu_action == "4":
                self.open_car_database()

    def show_available_cars(self):
        """ Order menu for the system. Its sub menus are nested functions within this function. """
        def place_order():
            """ Menu method for placing a new order. """
            pass

        def change_order():
            pass

        def delete_order():
            pass

        while self.__menu_action.lower() != "b":
            self.print_header()
            print("{:>100}".format("Show availability from:\n"))
            print("{:>84}".format("1. Today"))
            print("{:>95}".format("2. A day this month"))
            print("{:>111}".format("3. A day of another month this year"))
            print("{:>94}".format("4. A day next year"))
            print("{:>96}".format("B. Back to main menu"))
            print("\n" * 2)
            self.__menu_action = input("{:>95}".format("Enter menu action: "))

            if self.__menu_action == "1":
                place_order()
            if self.__menu_action == "2":
                change_order()
            if self.__menu_action == "3":
                delete_order()

    def find_order(self):
        pass

    def find_customer(self):
        """ Customer options. All sub menus are nested functions within this function. """
        def change_customer():
            """ Changes or deletes a customer. """
            def update_first_name():
                """ Updates a customer first name. """
                while self.__menu_action.lower() != "b":
                    self.print_header()
                    print("{:>94}".format("Change customer first name:\n")) #færa þetta í find customer menu
                    customer_id = input("Please enter customer id:")
                    if len(self.__customer_service.get_customer(customer_id)) == 0:
                        print("No customer with {} customer number found".format(customer_id))
                    else:
                        for customer in self.__customer_service.get_customer(customer_id):
                            print(customer)
                    
                    print("{:>96}".format("B. Back to main menu"))
                    print("\n" * 2)
                    self.__menu_action = input("{:>95}".format("Enter menu action: "))
            while self.__menu_action.lower() != "b":
                self.print_header()
                print("{:>94}".format("Change customer options:\n"))
                print("{:>107}".format("1. Update first name"))
                print("{:>94}".format("2. Update surname"))
                print("{:>94}".format("3. Update passport number"))
                print("{:>96}".format("B. Back to main menu"))
                print("\n" * 2)
                self.__menu_action = input("{:>95}".format("Enter menu action: "))
                if self.__menu_action == "1":
                    update_first_name()
                if self.__menu_action == "2":
                    delete_customer()
        def delete_customer():
            pass
        while self.__menu_action.lower() != "b":
            self.print_header()
            print("{:>94}".format("Customer options:\n"))
            print("{:>107}".format("1. Change customer registration"))
            print("{:>94}".format("2. Delete customer"))
            print("{:>96}".format("B. Back to main menu"))
            print("\n" * 2)
            self.__menu_action = input("{:>95}".format("Enter menu action: "))
            if self.__menu_action == "1":
                change_customer()
            if self.__menu_action == "2":
                delete_customer()



    def open_car_database(self):
        """ Car database options. Its sub menus are nested within this function. """
        def print_all_available_cars():
            """ Prints a list of all available cars. """
            while self.__menu_action.lower() != "b":
                self.print_header()
                all_cars = self.__car_service.get_all_cars()
                for car in all_cars:
                    if car.get_availability() == "TRUE":
                        print("{:>100}".format(car.__str__()))
                print("\n" * 2)
                print("{:>96}".format("B. Back to main menu"))
                print("\n" * 2)
                self.__menu_action = input("{:>95}".format("Enter menu action: "))

        def print_all_unavailable_cars():
            """ Prints a list of all cars currently out. """
            while self.__menu_action.lower() != "b":
                self.print_header()
                all_cars = self.__car_service.get_all_cars()
                for car in all_cars:
                    if car.get_availability().upper() == "FALSE":
                        print("{:>100}".format(car.__str__()))
                print("\n" * 2)
                print("{:>96}".format("B. Back to main menu"))
                print("\n" * 2)
                self.__menu_action = input("{:>95}".format("Enter menu action: "))
        while self.__menu_action.lower() != "b":
            self.print_header()
            print("{:>100}".format("Car options:\n"))
            print("{:>113}".format("1. Print a list of all available cars"))
            print("{:>117}".format("2. Print a list of all cars currently out"))
            print("{:>96}".format("B. Back to main menu"))
            print("\n" * 2)
            self.__menu_action = input("{:>95}".format("Enter menu action: "))

            if self.__menu_action == "1":
                print_all_available_cars()
            if self.__menu_action == "2":
                print_all_unavailable_cars()


    def write_to_db(self):
        """ Writes all databases to files. Call this method before program ends. """
        self.__order_service.write_db_to_file()