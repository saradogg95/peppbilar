from os import system, name
from services.CarServices import CarServices
from services.CustomerServices import CustomerServices
from services.EmployeeServices import EmployeeServices
from services.OrderServices import OrderServices
#from services.PaymentServices import PaymentServices verður sennilega ekki notað
from datetime import datetime
from datetime import date
import calendar
import datetime

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

    def print_back_to_main_menu(self):
        print("{:>96}".format("B. Back to main menu"))
        print("\n" * 2)
        self.__menu_action = input("{:>95}".format("Enter menu action: "))

    def main_menu(self):
        """ Main menu. """
        while self.__menu_action.lower() != "q":
            self.print_header()
            print("{:>98}".format("1. Show available cars"))
            print("{:>89}".format("2. Find order"))
            print("{:>92}".format("3. Find customer"))
            print("{:>96}".format("4. Open car database"))
            print("{:>96}".format("5. Return car"))
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
            if self.__menu_action == "5":
                self.return_car()

    def show_available_cars(self):
        """ Order menu for the system. Its sub menus are nested functions within this function. """
        def place_order():
            """ Menu method for placing a new order. """ 

            def add_or_find_customer():
                customer = None
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
                            print("{} is not a valid identity number!".format(identity_number))
                            
                def customer_id_check():
                    while True:
                        try:
                            customer_id = int(input("Please input customer id: "))
                            return customer_id
                        except ValueError:
                            print("Wrong input.")

                def get_user_input():
                    while True:
                        try:
                            customer_input = input("Option: ").lower()
                            if customer_input == "1" or customer_input == "2" or customer_input == "b":
                                return customer_input
                            else:
                                print("Please 1 or 2 for your choice.")
                        except ValueError:
                            print("Wrong input.")

                def print_options_for_user():
                    print("Please press 1 to add new customer.")
                    print("Please press 2 to find costumer.")
                    print("Please press b to back.")

                print_options_for_user() 
                user_choice = get_user_input()
                while user_choice != "b":
                    if user_choice == "1":
                        customer_id = self.__customer_service.automatic_id_generation()
                        identity_number = identity_number_check()
                        first_names = input("Please input first name: ")
                        surname = input("Please input last name: ")
                        citizenship = input("Please input citizenship: ")
                        passport_id = input("Please input passport id: ")        
                        credit_card_no = input("Please input credit card number: ")
                        new_customer = Customer(customer_id, identity_number, 
                                                first_names, surname, citizenship, passport_id, credit_card_no) 
                        self.__customer_service.add_customer(new_customer)
                        customer = new_customer
                        print(new_customer)

                    elif user_choice == "2":
                        print("Press 1 to find customer after identity number.")
                        print("Press 2 to find customer after passport id.")
                        user_choice = get_user_input()
                        if user_choice == "1":
                            id_num = input("Please input identity number: ")
                            customer = self.__customer_service.get_customer_after_id_num(id_num)
                            if customer:
                                print(customer[0])
                            else:
                                print("Customer not found.")
                        elif user_choice == "2":
                            pass_id = input("Please input passport id: ")
                            customer = self.__customer_service.get_customer_after_pass_id(pass_id)
                            if customer:
                                print(customer[0])
                            else:
                                print("Customer not found.")

                    print_options_for_user()
                    user_choice = get_user_input()
                if type(customer) == list:
                    return customer[0]
                else:
                    return customer
            
            found_customer = add_or_find_customer()


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
        done = False
        while not done:
            order_id = input("Please input the order id (q to quite): ")
            order = self.__order_service.get_order(order_id)
            if order == type(Order):
                print(order)
            elif order_id == "q":
                done = True
            else:
                done = True

        def print_choices():
            print("Press 1 to change order id.")
            print("Press 2 to change order date.")
            print("Press 3 to change rent rate from.")
            print("Press 4 to change rent date to.")
            print("Press 5 to change additional insurance.")
            print("Press b for back.")

        def choice():
            while True:
                try:
                    self.__menu_action = input("Please input your choice: ").lower()
                    if self.__menu_action == "b":
                        return self.__menu_action
                    value_error_check = int(self.__menu_action)
                    return self.__menu_action
                except ValueError:
                    print("Wrong input.")

        print_choices()
        self.__menu_action = choice()
        while self.__menu_action.lower() != "b":
            if self.__menu_action == "1":
                change_order_id = input("Please input order id change: ")
                order.set_order_id(change_order_id)
                print(order)
            if self.__menu_action == "2":
                change_order_date = input("Please input order date change: ")
                order.set_order_date(change_order_date)
                print(order)
            if self.__menu_action == "3":
                change_rent_date_from = input("Please input rent rate from change: ")
                order.set_rent_date_from(change_rent_date_from)
                print(order)    
            if self.__menu_action == "4":
                change_rent_date_to = input("Please input rent date to change: ")
                order.set_rent_date_to(change_rent_date_to)
                print(order)
            if self.__menu_action == "5":
                change_additional_insurance = input("Please input additional insurance change: ")
                order.set_additional_insurance(change_additional_insurance)
                print(order)
            print_choices()
            self.__menu_action = choice()

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

    def return_car(self):
        """ Function to return a car. """
        def mileage_lower_check(return_car, total_mileage):
            """ Checks wheter the entered mileage is lower than the mileage of the car when it went out. Returns True if so otherwise False. """
            for car in return_car:
                if car.get_mileage() < total_mileage:
                    return True
            return False

        while self.__menu_action.lower() != "b":
            self.print_header()
            order_to_return_id = input("{:>100}".format("Enter order number: "))
            valid_input = False
            while not valid_input:
                try:
                    int(order_to_return_id)
                    order_to_return = self.__order_service.get_order(order_to_return_id)
                except ValueError:
                    print("{} is not a valid order number.")
                    order_to_return_id = input("{:>100}".format("Enter order number: "))
            car_to_return_id = input("{:>100}".format("Enter licence plate of car to return: "))
            print("\n" * 2)
            return_car = self.__car_service.get_car(car_to_return_id)
            if len(return_car) == 0:
                print("{:>100}".format("No car with licence plate {} found.".format(car_to_return_id)))
                print("\n" * 2)
            else:
                mileage_complete = False
                while not mileage_complete:
                    total_mileage = input("{:>100}".format("Enter total mileage of car at return: "))
                    try:
                        total_mileage = int(total_mileage)
                        mileage_too_low = False
                        while not mileage_too_low:
                            print("Mileage entered is lower than when car went out. Please enter again.")
                            total_mileage =  input("{:>100}".format("Enter total mileage of car at return: "))
                            mileage_too_low = mileage_lower_check(return_car, total_mileage)
                            mileage_complete = True
                        
                    except ValueError:
                        print("{:>100}".format("Invalid mileage entered. Please try again"))
            self.print_back_to_main_menu()

                
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

