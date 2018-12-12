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


class UserInterface:
    def __init__(self):
        self.__car_service = CarServices()
        self.__customer_service = CustomerServices()
        self.__employee_service = EmployeeServices()
        self.__order_service = OrderServices()
        self.__today = date.today()
        self.__menu_action = ""
        self.__max_kilometer_per_day = 100

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
        self.__submenu_action = ""
        print("\n" * 10)
        print("{:>100}".format("PEPP BÍLAR"))
        print("{:>115}".format("-" * 40))
        print("{:>106}".format(self.__today.strftime("%A, %B %d, %Y")))
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
                """ Takes in a customer, asks the user to input a new first name and 
                then updates the customer with the new first name. """
                while self.__submenu_action.lower() != "b":
                    self.print_header()
                    print("{:>94}{}".format("Change customer first name: ", ("\n" * 2)))
                    new_first_name = input("Enter customer new first name: ")
                    customer_to_change.set_first_name(new_first_name)
                    #write_to_customer_db call here to save changes to hd file
                    print("{:>96}".format("B. Back to previous menu"))
                    print("\n" * 2)
                    self.__menu_action = input("{:>95}".format("Enter menu action: "))
                    
            def update_surname(customer_to_change):
                """ Takes in a customer, asks the user to input a new surname and 
                then updates the customer with the new surname. """
                while self.__submenu_action.lower() != "b":
                    self.print_header()
                    print("{:>94}{}".format("Change customer surname: ", ("\n" * 2)))
                    new_surname = input("Enter customer new surname: ")
                    customer_to_change.set_surname(new_surname)
                    #write_to_customer_db call here to save changes to hd file
                    print("{:>96}".format("B. Back to previous menu"))
                    print("\n" * 2)
                    self.__submenu_action = input("{:>95}".format("Enter menu action: "))
                    
            def update_passport_number(customer_to_change):
                """ Takes in a customer, asks the user to input a new passport number and 
                then updates the customer with the new passport number. """
                while self.__submenu_action.lower() != "b":
                    self.print_header()
                    print("{:>94}{}".format("Change customer passport number: ", ("\n" * 2)))
                    new_passport_no = input("Enter customer new passport number: ")
                    customer_to_change.set_surname(new_passport_no)
                    #write_to_customer_db call here to save changes to hd file
                    print("{:>96}".format("B. Back to previous menu"))
                    print("\n" * 2)
                    self.__submenu_action = input("{:>95}".format("Enter menu action: "))
                    
            def update_cc_number(customer_to_change):
                """ Takes in a customer, asks the user to input a new credit card number and 
                then updates the customer with the new credit card number. """
                while self.__menu_action.lower() != "b":
                    self.print_header()
                    print("{:>94}{}".format("Change credit card number: ", ("\n" * 2)))
                    new_credit_card_no = input("Enter customer credit card number: ")
                    customer_to_change.set_surname(new_credit_card_no)
                    #write_to_customer_db call here to save changes to hd file
                    print("{:>96}".format("B. Back to main menu"))
                    print("\n" * 2)
                    self.__submenu_action = input("{:>95}".format("Enter menu action: "))
                    
            def print_bottom_menu():
                print("\n" * 2)
                print("{:>94}".format("Change customer options:\n"))
                print("{:>107}".format("1. Update first name"))
                print("{:>94}".format("2. Update surname"))
                print("{:>94}".format("3. Update passport number"))
                print("{:>94}".format("4. Update credit card number"))
                
            while self.__menu_action.lower() != "b":
                #self.print_header()
                if menu_action == "1": #look up customer by icelandic registration number
                    self.print_header()
                    icelandic_registration_number = input("{:>100}".format("Enter Icelandic registration number: "))
                    if len(self.__customer_service.get_customer_by_icelandic_id(icelandic_registration_number)) == 0:
                        print("{:>100} {} {}".format("No customer with registration number", icelandic_registration_number, "found."))
                    else:
                        for customer in self.__customer_service.get_all_customers():
                            if customer.get_identity_number() == icelandic_registration_number:
                                customer_to_change = customer
                                print("{:>100}".format(customer_to_change.__str__()))
                        print_bottom_menu()
                if menu_action == "2": #look up customer by passport number
                    self.print_header()
                    passport_number = input("{:>100}".format("Enter passport number: "))
                    if len(self.__customer_service.get_customer_by_passport_no(passport_number)) == 0:
                        print("{:>100} {} {}".format("No customer with passport number", passport_number, "found."))
                    else:
                        for customer in self.__customer_service.get_all_customers():
                            if customer.get_passport_id().upper() == passport_number.upper():
                                print("{:>100}".format(customer.__str__()))
                        print_bottom_menu()
                print("{:>96}".format("R. Back to previous menu"))
                print("{:>96}".format("B. Back to main menu"))
                print("\n" * 2)
                self.__menu_action = input("{:>95}".format("Enter menu action: "))
                if self.__menu_action == "1":
                    update_first_name(customer_to_change)
                if self.__menu_action == "2":
                    update_surname(customer_to_change)
                if self.__menu_action == "3":
                    update_passport_number(customer_to_change)
                if self.__menu_action == "4":
                    update_cc_number(customer_to_change)
                if self.__menu_action.lower() == "r":
                    self.find_customer()
        
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
                        print("{:>150}".format(car.__str__()))
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

                
    def get_additional_insuarance_cost(self, order_id):
        """ Takes in an order id and gets that order from the database and calculates the cost of additional insurance"""        
        order = self.__order_service.get_order(order_id)        
        #Check if additional inusarance was ordered
        if order.get_additional_insurance() == "TRUE":                
            #From the order object, we obtain the registration number for the car and send it into get_car_by_regnum to get car category price
            car = self.__car_service.get_car(order.get_car_id())                 
            #The cost of insurance is the 75% of the price of a days rental
            return int(car[0].get_category_price()) * float(0.75)
        else:
            return None 

    
    
    def get_additional_cost_extra_millage(self, order_id):
        """ Takes in an order id and gets that order from the database and calculates the cost of additional insurance"""        
        order = self.__order_service.get_order(order_id)                   
        #From the order object, we obtain the registration number for the car and send it into get_car_by_regnum to get car category price
        car = self.__car_service.get_car(order.get_car_id())                 
        #The cost of additional millage over 100km is 1% of daily rental cost
        return int(car[0].get_category_price()) * 0.01


            
    def get_cost_without_additions(self, order_id):
        """ Takes in an order id and gets that order from the database and calculates the cost without additions"""        
        order = self.__order_service.get_order(order_id)
        #We need the number of days the car is being rent for to calculat the total cost
        start_date = datetime.strptime(order.get_rent_date_from(), "%d/%m/%Y")
        end_date = datetime.strptime(order.get_rent_date_to(), "%d/%m/%Y")           
        number_of_days = abs((end_date-start_date).days)
        #From the order object, we obtain the registration number for the car and send it into get_car_by_regnum to get car category price
        car = self.__car_services.get_car(order.get_car_id())
        return int(car[0].get_category_price()) * number_of_days                     


    def write_to_db(self):
        """ Writes all databases to files. Call this method before program ends. """
        self.__order_service.write_db_to_file()


    def update_car_mileage_and_availability(self, reg_num, mileage):
        ''' Updates milage of a car, with mileage driven by customer'''
        car = self.__car_service.get_car(reg_num)
        #gets current mileage stauts and adds to mileage driven by customer
        new_mileage = int(car[0].get_mileage()) + int(mileage)
        car[0].set_mileage(new_mileage)
        car[0].set_availability(True)
        return car[0]


    def update_order_mileage(self, order_id, mileage):
        ''' Updates milage of a car, with mileage driven by customer'''
        order = self.__order_service.get_order(order_id)
        #update mileage
        order.set_mileage_in(mileage)
        return order

    def get_car_rent_history(self, reg_num):
        orders = []
        for order in self.__order_service.get_all_orders():
            if order.get_car_id() == reg_num:
                orders.append("Registration nr.: " + reg_num
                + " - Mileage from: " + order.get_mileage_out() 
                + " Mileage to: " + order.get_mileage_in()
                + " From: " + order.get_rent_date_from()
                + " To: " + order.get_rent_date_to())
        return orders

    def get_customer_rent_history(self, customer_id):
        orders = []
        for order in self.__order_service.get_all_orders():
            if order.get_customer_id() == customer_id:
                orders.append("Customer id.: " + customer_id
                + " - Car: " + order.get_car_id() 
                + " From: " + order.get_rent_date_from()
                + " To: " + order.get_rent_date_to())
        return orders

    def get_total_cost_for_extra_kilometers(self, order_id):
        orders = []
        for order in self.__order_service.get_all_orders():
            if order.get_order_id() == order_id:
                #get total number of days rented for
                start_date = datetime.strptime(order.get_rent_date_from(), "%d/%m/%Y")
                end_date = datetime.strptime(order.get_rent_date_to(), "%d/%m/%Y")           
                number_of_days = abs((end_date-start_date).days)
                
                #get total number of kilometers driven on rental period
                number_of_kilometers_driven = int(order.get_mileage_in()) - int(order.get_mileage_out()) 
                #get max number of kilometers allowed to be driven
                max_driven = self.__max_kilometer_per_day * number_of_days

                #calculate the cost of extra kilometers
                if number_of_kilometers_driven > max_driven:
                    extra_kilometers = number_of_kilometers_driven - max_driven
                    return extra_kilometers * self.get_additional_cost_extra_millage(order_id)

