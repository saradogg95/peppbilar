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
        def customer_lookup(menu_action):
            """ Changes or deletes a customer. """
            def update_first_name(customer_to_change):
                """ Takes in a customer, asks the user to input a new first name and then updates the customer with the new first name. """
                while self.__menu_action.lower() != "b":
                    self.print_header()
                    print("{:>94}{}".format("Change customer first name: ", ("\n" * 2)))
                    new_first_name = input("Enter customer new first name: ")
                    customer_to_change.set_first_name(new_first_name)
                    #write_to_customer_db call here to save changes to hd file
                    print("{:>96}".format("B. Back to main menu"))
                    print("\n" * 2)
                    self.__menu_action = input("{:>95}".format("Enter menu action: "))
            def update_surname(customer_to_change):
                """ Takes in a customer, asks the user to input a new surname and then updates the customer with the new surname. """
                while self.__menu_action.lower() != "b":
                    self.print_header()
                    print("{:>94}{}".format("Change customer surname: ", ("\n" * 2)))
                    new_surname = input("Enter customer new surname: ")
                    customer_to_change.set_surname(new_surname)
                    #write_to_customer_db call here to save changes to hd file
                    print("{:>96}".format("B. Back to main menu"))
                    print("\n" * 2)
                    self.__menu_action = input("{:>95}".format("Enter menu action: "))
            def update_passport_number(customer_to_change):
                """ Takes in a customer, asks the user to input a new passport number and then updates the customer with the new passport number. """
                while self.__menu_action.lower() != "b":
                    self.print_header()
                    print("{:>94}{}".format("Change customer passport number: ", ("\n" * 2)))
                    new_passport_no = input("Enter customer new passport number: ")
                    customer_to_change.set_surname(new_passport_no)
                    #write_to_customer_db call here to save changes to hd file
                    print("{:>96}".format("B. Back to main menu"))
                    print("\n" * 2)
                    self.__menu_action = input("{:>95}".format("Enter menu action: "))

            while self.__menu_action.lower() != "b":
                customer_to_change = ""
                if menu_action == "1": #look up customer by icelandic registration number
                    self.print_header()
                    icelandic_registration_number = input("{:>100}".format("Enter Icelandic registration number: "))
                    print("\n" * 2)
                    if len(self.__customer_service.get_customer_by_icelandic_id(icelandic_registration_number)) == 0:
                        print("{:>100} {} {}".format("No customer with registration number", 
                                                     icelandic_registration_number, "found."))
                    else:
                        for customer in self.__customer_service.get_all_customers():
                            if customer.get_identity_number() == icelandic_registration_number:
                                customer_to_change = customer
                                print("{:>100}".format(customer_to_change.__str__()))
                        print("\n" * 2)
                        print("{:>94}".format("Change customer options:\n"))
                        print("{:>107}".format("1. Update first name"))
                        print("{:>94}".format("2. Update surname"))
                        print("{:>94}".format("3. Update passport number"))
                if menu_action == "2": #look up customer by passport number
                    self.print_header()
                    passport_number = input("{:>100}".format("Enter passport number: "))
                    print("\n" * 2)
                    if len(self.__customer_service.get_customer_by_passport_no(passport_number)) == 0:
                        print("{:>100} {} {}".format("No customer with passport number", 
                                                     passport_number, "found."))
                    else:
                        for customer in self.__customer_service.get_all_customers():
                            if customer.get_passport_id().upper() == passport_number.upper():
                                print("{:>100}".format(customer.__str__()))
                        print("\n" * 2)
                        print("{:>94}".format("Change customer options:\n"))
                        print("{:>107}".format("1. Update first name"))
                        print("{:>94}".format("2. Update surname"))
                        print("{:>94}".format("3. Update passport number"))
                print("{:>96}".format("B. Back to main menu"))
                print("\n" * 2)
                self.__menu_action = input("{:>95}".format("Enter menu action: "))
                if self.__menu_action == "1":
                    update_first_name(customer_to_change)
                if self.__menu_action == "2":
                    update_surname(customer_to_change)
                if self.__menu_action == "3":
                    update_passport_number(customer_to_change)
        
        while self.__menu_action.lower() != "b":
            self.print_header()
            print("{:>94}".format("Find customer by:\n"))
            print("{:>107}".format("1. Icelandic registration number"))
            print("{:>94}".format("2. Passport number"))
            print("{:>96}".format("B. Back to main menu"))
            print("\n" * 2)
            self.__menu_action = input("{:>95}".format("Enter menu action: "))
            if self.__menu_action == "1" or self.__menu_action == "2":
                customer_lookup(self.__menu_action)

    def open_car_database(self):
        """ Car database options. Its sub menus are nested within this function. """
        
        def print_all_available_cars():
            """ Prints a list of all available cars. """
            
            while self.__menu_action.lower() != "b":
                self.print_header()
                all_cars = self.__car_service.get_all_cars()
                for car in all_cars:
                    if car.get_availability().upper() == "TRUE":
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
