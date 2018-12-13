from os import system, name
from services.CarServices import CarServices
from services.CustomerServices import CustomerServices
from services.EmployeeServices import EmployeeServices
from services.OrderServices import OrderServices
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
        """ Prints the header file of the menu and resets 
        the menu action comparsion string. """
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
            print("{:>100}".format("2. Show unavailable cars"))
            print("{:>89}".format("3. Find order"))
            print("{:>92}".format("4. Find customer"))
            print("{:>89}".format("5. Return car"))
            print("{:>92}".format("6. Usage history"))
            print("{:>94}".format("7. Show price list"))
            print("{:>91}".format("Q. Quit program"))
            print("\n" * 2)
            self.__menu_action = input("{:>95}".format("Enter menu action: "))

            if self.__menu_action == "1":
                self.show_available_cars()
            if self.__menu_action == "2":
                self.show_unavailable_cars()
            if self.__menu_action == "3":
                self.find_order()
            if self.__menu_action == "4":
                self.find_customer()
            if self.__menu_action == "5":
                self.return_car()
            if self.__menu_action == "6":
                self.usage_history()
            if self.__menu_action == "7":
                self.show_price_list()

    def show_price_list(self):
        self.print_header()
        print("{:>87}".format("Car prices:\n"))
        print("{:>103}".format("Compact car price: 10000 ISK"))
        print("{:>100}".format("Jeep car price: 20000 ISK"))
        print("{:>103}".format("Family car price: 15000 ISK\n"))
        print("{:>93}".format("Insurance prices:\n"))
        print("{:>116}".format("Base insurance cost: 75% of one days rent"))
        print("{:>111}".format("Additional insurance cost: 2000 ISK\n"))
        print("{:>104}".format("Press any button to continue\n"))
        input("{:>90}".format("*. Any buttom: "))

                
#    def show_available_cars(self):
#        """ Order menu for the system. Its sub menus are nested functions within this function. """
#        def place_order():
#            """ Menu method for placing a new order. """ 

    def get_additional_insuarance_cost(self, reg_num):
        """ Takes in the car registration number and gets the cost of daily rental
        and calculates the cost of additional insurance"""        
        car = self.__car_service.get_car(reg_num)                 
        #The cost of insurance is the 75% of the price of a days rental
        return int(car.get_category_price()) * float(0.75)



    def show_available_cars(self):

        #Set a day this month as starting date:
        def change_working_date_day(working_date, logic="STARTING"):
            set_outday = int(input("Set a day this month as {} date: ".format(logic)))
            working_date[0] = set_outday
          
        #Set a day of a month this year as a starting date:
        def change_working_date_day_month(working_date, logic="STARTING"):
            set_out_day = int(input("Set a day of month as {} date: ".format(logic)))
            working_date[0] = set_out_day
            set_out_month = int(input("Set month as {} date: ".format(logic)))
            working_date[1] = set_out_month
        
        #Set a day next year as a starting date:
        def change_working_date_day_month_year(working_date, logic="STARTING"):
            set_out_day = int(input("Set a day of month as {} date: ".format(logic)))
            working_date[0] = set_out_day
            set_out_month = int(input("Set month as {} date: ".format(logic)))
            working_date[1] = set_out_month
            working_date[2] = working_date[2]+1
        
        #Printout of date for confirmation prompt:
        def outdate_confirmation(working_date):
            outdate = datetime.date(working_date[2], working_date[1], working_date[0])
            outdate_weekday = calendar.day_name[outdate.weekday()]
            outdate_month = calendar.month_name[outdate.month]
    
            valid_confirmation = False
            while valid_confirmation == False:
                self.print_header()
                print(("Date of car going out is: {}, {} {}, {}?".format(outdate_weekday.upper(), 
                                                                         outdate_month.upper(), 
                                                                         working_date[0], working_date[2])))
                confirmation = input("1. Confirm\n2. Change\n")
                if confirmation == '1':
                    valid_confirmation == True
                    return True
                elif confirmation == '2':
                    valid_confirmation == True
                    return False
           
        def start_and_return_confirmation(start_date, return_date):
            length = abs((return_date - start_date).days)
            valid_confirmation = False
            while valid_confirmation == False:
                print(("Rent a car from:\n\n{}\n\nto:\n\n{}\n\n{} days?\n".format(start_date.strftime("%A, %B %d, %Y"),
                return_date.strftime("%A, %B %d, %Y"), length)))
                confirmation = input("1. Confirm\n2. Cancel\n")
                if confirmation == '1':
                    valid_confirmation = True
                    return True
                elif confirmation == '2':
                    valid_confirmation = True
                    return False
                else:
                    print("Invalid input.")
       
        def date_validation(working_date, reference_date, working_date_saved):
            date_to_validate = datetime.date(working_date[2], working_date[1], working_date[0])
            if date_to_validate <= reference_date:
                print("This date is out of scope.")
                working_date = working_date_saved.copy()
                return False
            else:
                return True
        
        def get_starting_date(order, working_date_out, this_is_today):
            starting_date_registered = False
            working_date_out_saved = working_date_out.copy()
            while starting_date_registered == False:
                self.print_header()   
                quick_starting_date = input("Show availability FROM:\n1. Today.\n2. Another day this month.\n3." + 
                                            "A day of another month this year.\n4. Next year.\n5. Cancel.\n")
                if quick_starting_date == '1':
                    starting_date_registered = True
                elif quick_starting_date == '2':
                    self.print_header()
                    change_working_date_day(working_date_out)
                    valid_date = date_validation(working_date_out, this_is_today, working_date_out_saved)
                    while valid_date == False:
                        change_working_date_day(working_date_out)
                        valid_date = date_validation(working_date_out, this_is_today, working_date_out_saved)
                    else:
                        starting_date_registered = True
                elif quick_starting_date == '3':
                    self.print_header()
                    change_working_date_day_month(working_date_out)
                    valid_date = date_validation(working_date_out, this_is_today, working_date_out_saved)
                    while valid_date == False:
                        change_working_date_day_month(working_date_out)
                        valid_date = date_validation(working_date_out, this_is_today, working_date_out_saved)
                    else:
                        starting_date_registered = True
                elif quick_starting_date == '4':
                    self.print_header()
                    change_working_date_day_month_year(working_date_out)
                    starting_date_registered = True
                elif quick_starting_date == '5':
                    self.print_header()
                    return False
                else:
                    print("{} not a valid input".format(quick_starting_date))

                #Prompt for confirmation, control value updated:        
                self.print_header()
                confirmation = outdate_confirmation(working_date_out)
                if confirmation == True:
                    outdate = datetime.date(working_date_out[2], working_date_out[1], working_date_out[0])
                    order.append(outdate)
                    return True
                else:
                    starting_date_registered = False
                  
        def get_return_date(order, working_date):
            outdate = datetime.date(working_date[2], working_date[1], working_date[0])
            outdate_weekday = calendar.day_name[outdate.weekday()]
            outdate_month = calendar.month_name[outdate.month]
            self.print_header()
            print(("FROM: {}, {} {}, {}".format(outdate_weekday.upper(), outdate_month.upper(), 
            working_date[0], working_date[2])))
            valid_input = False
            while valid_input == False:
                valid_to_date_day = False
                while valid_to_date_day == False:
                    try:
                        to_date_day = int(input("TO (set day): "))
                        if to_date_day < 100:
                            valid_to_date_day = True
                    except ValueError:
                        pass
                valid_to_date_month = False
                while valid_to_date_month == False:
                    try:
                        to_date_month = int(input("TO (set month): "))
                        if to_date_month < 100:
                            valid_to_date_month = True
                    except ValueError:
                        pass
                valid_to_date_year = False
                while valid_to_date_year == False:
                    try:
                        to_date_year = int(input("TO (set year): "))
                        if to_date_month < 100:
                            valid_to_date_year = True
                    except ValueError:
                        pass
                try:
                    return_date = datetime.date(to_date_year, to_date_month, to_date_day)
                    valid_input = True
                except ValueError:
                    print("Invalid input.")
                if outdate >= return_date:
                    self.print_header()
                    print("Invalid input. Check starting date.")
                    print(("FROM: {}, {} {}, {}".format(outdate_weekday.upper(), outdate_month.upper(), 
                    working_date[0], working_date[2])))
                    valid_input = False
                else:
                    self.print_header()
                    confirmation = start_and_return_confirmation(outdate, return_date)
                    if confirmation == True:
                        order.append(return_date)
                        return True
                    else:
                        order.clear()
                        return False


        #For a list of all cars:
        self.__car_service = CarServices()
        #For a list of all orders:
        self.__order_service = OrderServices()

        def date_from_string(date_as_string):
            date_as_list = date_as_string.split('-')
            date_format = date(int(date_as_list[0]),int(date_as_list[1]),int(date_as_list[2]))
            return date_format
  
        def get_clashing_orders(list_of_order_objects, out_date_car1, return_date_car1):
            '''Car1 is the car that's being ordered, while car0 would be whichever car in database.'''
            clashing_orders_list = []
            for order in list_of_order_objects:
                if return_date_car1 >= date_from_string(str(order.get_rent_date_from())) and date_from_string(str(order.get_rent_date_to())) >= out_date_car1:
                    clashing_orders_list.append(order.get_car_id())
            clashing_orders_set = set(clashing_orders_list)
            return clashing_orders_set  

        def get_clean_list(list_of_all_cars, clashing_orders):
            '''List of available cars'''
            working_list =  []
            for licence_plate in clashing_orders:
                for car in list_of_all_cars:
                    if car.get_reg_num() == licence_plate:
                        working_list.append(car)
            working_list_available = []
            for car in list_of_all_cars:
                if car not in working_list:
                    working_list_available.append(car) 
            return working_list_available
     
        def filter_list(working_list, brand="", category="", registration_date=""):
            '''A new list for cars that meet criteria:'''
            if brand == "" and category == "" and registration_date == "":
                filtered_working_list = working_list.copy()
            else:
                filtered_working_list = []
            if brand != "" and category != "" and registration_date != "":
                for car in working_list:
                    if car.get_brand() == brand and car.get_category() == category and car.get_registration_date() == registration_date:
                        filtered_working_list.append(car)
            elif brand == "" and category != "" and registration_date != "":
                for car in working_list:
                    if car.get_category() == category and car.get_registration_date() == registration_date:
                        filtered_working_list.append(car)
            elif brand != "" and category == "" and registration_date != "":
                for car in working_list:
                    if car.get_brand() == brand and car.get_registration_date() == registration_date:
                        filtered_working_list.append(car)
            elif brand != "" and category != "" and registration_date == "":
                for car in working_list:
                    if car.get_brand() == brand and car.get_category() == category:
                        filtered_working_list.append(car)
            elif brand != "":
                for car in working_list:
                    if car.get_brand() == brand:
                        filtered_working_list.append(car)
            elif category != "":
                for car in working_list:
                    if car.get_category() == category:
                        filtered_working_list.append(car)
            elif registration_date != "":
                for car in working_list:
                    if car.get_registration_date() == registration_date:
                        filtered_working_list.append(car)
            return filtered_working_list
        
        def available_car_printout(filtered_working_list):
            if filtered_working_list == []:
                print("NO CARS AVAILABLE FOR THIS DATE WITH THIS CRITERIA.")
            else:
                for index, line in enumerate(filtered_working_list):
                    print(index+1, line)
                
        def choose_car_from_list(filtered_working_list):
            if filtered_working_list == []:
                selection = input("Press any key to go back.")
                return 999
            else:
                selection = input("\nSelect car from list by typing in index, or press 'c' to cancel and go back.")
                if selection.lower() == 'c':
                    return 999
                else:
                    try: 
                        selection_int = int(selection)
                        selection_as_index = selection_int - 1
                        return selection_as_index
                    except ValueError:
                        print("Invalid input.")

        def car_confirmation_prompt(order, final_list, selection_as_index):
            print(final_list[selection_as_index])
            valid_confirmation = False
            while valid_confirmation == False:
                confirmation = input("Confirm(y/n): ")
                if confirmation.lower() == "y":
                    order.append(final_list[selection_as_index])
                    return True
                elif confirmation.lower() == "n":
                    order.clear()
                    return False
           
        def filter_prompt():
            valid_input = False
            self.print_header()
            while valid_input == False:
                filter_input = input("Add filter (by brand, category, or registration date?\n1. Yes.\n2. No.\n")
                if filter_input == "1":
                    return 1
                elif filter_input == "2":
                    return 0
                else:
                    print("Invalid input.")
                    
        def search_filters(list_of_all_cars,filter_dummy,all_brands, all_categories, all_registration_dates):
            filter_values = []
            if filter_dummy == 0:
                filter_values = ["","",""]
            else:
                filter_values = filter_menu(all_brands, all_categories, all_registration_dates)
            return filter_values
    
        def get_all_brands(list_of_all_cars):
            brand_set = set()
            for car in list_of_all_cars:
                brand_set.add(car.get_brand())
            return brand_set
        
        def get_all_categories(list_of_all_cars):
            category_set = set()
            for car in list_of_all_cars:
                category_set.add(car.get_category())
            return category_set
       
        def get_all_registration_dates(list_of_all_cars):
            registration_date_set = set()
            for car in list_of_all_cars:
                registration_date_set.add(car.get_registration_date())
            return registration_date_set

        
        def filter_menu(brands, categories, registration_dates):
            filter_list = []
            valid_brand = False
            while valid_brand == False:
                print("\nFilter option 1/3:\nAvailable brands:")
                for item in brands:
                    print(item)
                brand = input("Filter by brand (or leave empty):\n")
                if brand == "":
                    filter_list.append("")
                    valid_brand = True
                else: 
                    if brand.upper() in brands:
                        filter_list.append(brand.upper())
                        valid_brand = True
                    else:
                        print("{} not available.".format(brand))

            valid_category = False
            while valid_category == False:
                print("\nFilter option 2/3:\nAvailable categories:")
                for item in categories:
                    print(item)
                category = input("Filter by category (or leave empty):\n")
                if category == "":
                    filter_list.append("")
                    valid_category = True
                else: 
                    if category.upper() in categories:
                        filter_list.append(category.upper())
                        valid_category = True
                    else:
                        print("{} not available.".format(category))

            valid_registration_date = False
            while valid_registration_date == False:
                print("\nFilter option 3/3:\nAvailable registration dates:")
                for item in registration_dates:
                    print(item)
                registration_date = input("Filter by registration date (or leave empty):\n")
                if registration_date == "":
                    filter_list.append("")
                    valid_registration_date = True
                else: 
                    if registration_date in registration_dates:
                        filter_list.append(registration_date)
                        valid_registration_date = True
                    else:
                        print("{} not available.".format(registration_date))

            return filter_list
      
        def get_cars(order):
            full_order_confirmed = False
            while full_order_confirmed == False:
                filter_option = filter_prompt()
                if filter_option == "3":
                    return False
    
                list_of_all_cars = self.__car_service.get_all_cars()
                list_of_all_orders = self.__order_service.get_all_orders()
                clashing_orders = get_clashing_orders(list_of_all_orders, order[0], order[1])

                all_brands = get_all_brands(list_of_all_cars)
                all_categories = get_all_categories(list_of_all_cars)
                all_registration_dates = get_all_registration_dates(list_of_all_cars)

                specifications = search_filters(list_of_all_cars,filter_option,all_brands, 
                                                all_categories, all_registration_dates)
                list_of_available = get_clean_list(list_of_all_cars, clashing_orders)
                filtered_list = filter_list(list_of_available, brand=specifications[0], category=specifications[1], 
                                            registration_date=specifications[2])
                available_car_printout(filtered_list)
                index_num_or_quit = choose_car_from_list(filtered_list)
                while index_num_or_quit != 999:
                    car_confirmation_prompt(order,filtered_list, index_num_or_quit)
                    full_order_confirmed = True
                    return True

        def add_or_find_customer(order):
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

            def cancellation_prompt():
                valid_cancellation = False
                while valid_cancellation == False:
                    cancellation = input("Cancel order?\n1. Yes\n2. No\n")
                    if cancellation == "1":
                        valid_cancellation = True
                        return True
                    elif cancellation == "2":
                        valid_cancellation = True
                        return False
                    else:
                        print("Please choose one of the two options.")
                                             
            def print_options_for_user():
                self.print_header()
                print("Please provide customer details:\n\n")
                print("Press 1 to add new customer.")
                print("Press 2 to find customer.")
                print("Or press 'c' to cancel the order.")

            print_options_for_user() 
            user_choice = get_user_input()
            #while user_choice != "c":
            if user_choice == "1":
                customer_id = self.__customer_service.automatic_id_generation()
                self.print_header()
                identity_number = identity_number_check()
                self.print_header()
                valid = False
                while valid == False:
                    first_names = input("Please provide first name, or press 0 to cancel: ")
                    if first_names == "0":
                        check = cancellation_prompt()
                        if check == True:
                            valid = True
                            return False
                    valid = True
                self.print_header()
                valid = False
                while valid == False:
                    surname = input("Please provide last name, or press 0 to cancel: ")
                    if surname == "0":
                        check = cancellation_prompt()
                        if check == True:
                            valid = True
                            return False
                    valid = True
                self.print_header()
                valid = False
                while valid == False:
                    citizenship = input("Please provide citizenship, or press 0 to cancel: ")
                    if citizenship == "0":
                        check = cancellation_prompt()
                        if check == True:
                            valid = True
                            return False
                    valid = True
                self.print_header()
                valid = False
                while valid == False:
                    passport_id = input("Please provide passport id, or press 0 to cancel: ")
                    if citizenship == "0":
                        check = cancellation_prompt()
                        if check == True:
                            valid = True
                            return False
                    valid = True
                self.print_header()
                valid = False
                while valid == False:
                    credit_card_no = input("Please provide credit card number, or press 0 to cancel: ")
                    if citizenship == "0":
                        check = cancellation_prompt()
                        if check == True:
                            valid = True
                            return False
                    valid = True
                new_customer = Customer(customer_id, identity_number, 
                                        first_names, surname, citizenship, 
                                        passport_id, credit_card_no) 
                self.__customer_service.add_customer(new_customer)
                customer = new_customer
                order.append(customer.get_customer_id())
                return True

            elif user_choice == "2":
                print("Press 1 to find customer by identity number.")
                print("Press 2 to find customer by passport id.")
                user_choice = get_user_input()
                if user_choice == "1":
                    id_num = input("Please provide identity number, or press 'c' to cancel: ")
                    customer = self.__customer_service.get_customer_after_id_num(id_num)
                    if customer:
                        order.append(customer.get_customer_id())
                        return True
                    else:
                        print("Customer not found.")
                elif user_choice == "2":
                    pass_id = input("Please provide passport id, or press 'c' to cancel: ")
                    customer = self.__customer_service.get_customer_after_pass_id(pass_id)
                    if customer:
                        order.append(customer.get_customer_id())
                        return True
                    else:
                        print("Customer not found.")

        
            if type(customer) == list:
                order.append[customer[0]]
                return True
            else:
                order.clear()
                return False

        """Printout function, to confirm order."""
        def confirmation_to_save_order(order):
            start_date = order[0]
            end_date = order[1]
            total_days = abs((end_date - start_date).days)
            car_in_question = order[2]
            billing_customer = order[3]
            proper_customer = self.__customer_service.get_customer(billing_customer)
            customer_first_names = proper_customer.get_first_names()
            customer_surname = proper_customer.get_surname()
            price = int(car_in_question.get_category_price()) * total_days
            licence_plate = car_in_question.get_reg_num()
            brand = car_in_question.get_brand()
            model = car_in_question.get_model()
            category = car_in_question.get_category()
            self.print_header()
            print(("{} {}\nType of car: {}\nDate of car going out: {}\nDate of car coming back: {}\nTotal number of days: {}\nTotal price: {} isk.\n{} {}\n".format(
                brand, model, category, start_date, end_date, total_days, price, customer_first_names, customer_surname)))
            valid_confirmation = False
            while valid_confirmation == False:
                final_confirmation = input("Confirm?\n1. Yes.\n2. No, cancel order.\n")
                if final_confirmation == "1":
                    valid_insurance_decision = False
                    while valid_insurance_decision == False:
                        additional_insurance = input("Add additional insurance?\n1. Yes.\n2. No.\n")
                        if additional_insurance == '1':
                            additional_insurance_column = 'TRUE'
                            additional_insurance_cost = self.get_additional_insuarance_cost(licence_plate)
                            price = price + additional_insurance_cost
                            valid_insurance_decision = True
                        elif additional_insurance == '2':
                            additional_insurance_column = 'FALSE'
                            additional_insurance_cost = 0
                            valid_insurance_decision = True
                        else:
                            print("Invalid input!")


                    valid_credit_card = False
                    while valid_credit_card == False:
                        credit_card_info = input("Please provide credit card info: ")
                        if len(credit_card_info) == 16:
                            try:
                                int(credit_card_info)
                                valid_credit_card == True
                            except ValueError:
                                print("Invalid card number (16 digits required).")
                                pass
                    valid_credit_card == True
                    valid_confirmation == True
                    new_order_id = CustomerServices.automatic_id_generation()
                    date_of_order = date.today()
                    included_km = total_days * 100
                    new_order = Order(new_order_id, date_of_order, start_date, end_date, credit_card_info, included_km, additional_insurance_column, billing_customer, licence_plate, additional_insurance_cost)
                    OrderServices.add_order(new_order)
                    return False

                elif final_confirmation == "2":
                    valid_confirmation == True
                    order.clear()
                    return False
                else:
                    print("Invalid input!")
            

        order_X = [] #Here, order details will gradually be inserted.
        ongoing_order = True #Control variable.

        #Today's date values, for printout:
        this_is_today = date.today()
        this_is_today_month_num = this_is_today.month
        this_is_today_number = this_is_today.day
        this_is_today_year = this_is_today.year
    
        #The date today turned into list:
        working_date_out = []
        working_date_out.append(this_is_today_number)
        working_date_out.append(this_is_today_month_num)
        working_date_out.append(this_is_today_year)

        #Control variable checked at the end of every action:
        ongoing_order = get_starting_date(order_X, working_date_out, this_is_today)
        if ongoing_order == True:
            ongoing_order = get_return_date(order_X, working_date_out)
            if ongoing_order == True:
                ongoing_order = get_cars(order_X)
                if ongoing_order == True:
                    ongoing_order = add_or_find_customer(order_X) 
                    if ongoing_order == True:
                        ongoing_order = confirmation_to_save_order(order_X)
                        if ongoing_order == True:
                            return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def show_unavailable_cars(self):
        pass

    def find_order(self):
        done = False
        while not done:
            self.print_header()
            print("{:>96}".format("B. Back to main menu\n"))
            print("{:>101}".format("Please input the order id "))
            order_id = input("{:>85}".format("Order id: "))
            print()
            order = self.__order_service.get_order(order_id)
            if type(order) == Order:
                self.print_header()
                print("{:>88}".format("Order found.\n"))
                print("{:>104}".format("Press any button to continue\n"))
                input("{:>90}".format("*. Any buttom: "))
                done = True
            elif order_id.lower() == "b":
                return None
            elif type(order) == str:
                print("{:>109}".format(order))
                print()
                print("{:>104}".format("Press any button to continue\n"))
                input("{:>90}".format("*. Any buttom: "))
                
        def print_choices():
            print("{:>92}".format("Change order by:\n"))
            print("{:>86}".format("1. Order id"))
            print("{:>88}".format("2. Order date"))
            print("{:>92}".format("3. Rent rate from"))
            print("{:>90}".format("4. Rent date to"))
            print("{:>98}".format("5. Additional insurance"))
            print("{:>89}".format("6. Delet order"))
            print("{:>95}".format("B. Back to main menu"))

        def choice():
            while True:
                try:
                    print()
                    self.__menu_action = input("{:>101}".format("Please input your choice: "))
                    if self.__menu_action == "b":
                        return self.__menu_action
                    value_error_check = int(self.__menu_action)
                    return self.__menu_action
                except ValueError:
                    print("Wrong input")

        self.print_header()            
        print_choices()
        self.__menu_action = choice()
        while self.__menu_action.lower() != "b":
            if self.__menu_action == "1":
                self.print_header()
                order_id = input("{:>92}".format("Order id change: "))
                order.set_order_id(order_id)
                self.__order_service.write_db_to_file()
                print(order)
                print()
            if self.__menu_action == "2":
                done = False
                while not done:
                    try:
                        self.print_header()
                        change_order_date = input("{:>107}".format("Order date change (YYYY-MM-DD): "))
                        print()
                        year, month, day = change_order_date.split("-")
                        datetime.datetime(int(year), int(month), int(day))
                        done = True
                    except:
                        print("{:>96}".format("Wrong datetime input\n"))
                        print("{:>104}".format("Press any button to continue\n"))
                        input("{:>90}".format("*. Any buttom: "))

                order.set_order_date(change_order_date)
                self.__order_service.write_db_to_file()
                print(order)
                print()
            if self.__menu_action == "3":
                done = False
                while not done:
                    try:
                        self.print_header()
                        change_rent_date_from = input("{:>111}".format("Rent date from change (YYYY-MM-DD): "))
                        print()
                        year, month, day = change_order_date.split("-")
                        datetime.datetime(int(year), int(month), int(day))
                        done = True
                    except:
                        print("{:>96}".format("Wrong datetime input\n"))
                        print("{:>104}".format("Press any button to continue\n"))
                        input("{:>90}".format("*. Any buttom: "))

                order.set_rent_date_from(change_rent_date_from)
                self.__order_service.write_db_to_file()
                print(order) 
                print()   
            if self.__menu_action == "4":
                done = False
                while not done:
                    try:
                        self.print_header()
                        change_rent_date_to = input("{:>109}".format("Rent date to change (YYYY-MM-DD): "))
                        print()
                        year, month, day = change_order_date.split("-")
                        datetime.datetime(int(year), int(month), int(day))
                        done = True
                    except:
                        print("{:>96}".format("Wrong datetime input\n"))
                        print("{:>104}".format("Press any button to continue\n"))
                        input("{:>90}".format("*. Any buttom: "))

                order.set_rent_date_to(change_rent_date_to)
                self.__order_service.write_db_to_file()
                print(order)
                print()
            if self.__menu_action == "5":
                self.print_header()
                change_additional_insurance = input("{:>117}".format("Please input additional insurance change: "))
                order.set_additional_insurance(change_additional_insurance)
                self.__order_service.write_db_to_file()
                print(order)
                print()
            if self.__menu_action == "6":
                self.print_header()
                deleted_order_msg = self.__order_service.delete_order(order_id)
                print("{:>109}".format(deleted_order_msg))
                print()
                self.__order_service.write_db_to_file()
                print("{:>104}".format("Press any button to continue\n"))
                input("{:>90}".format("*. Any buttom: "))
                break
                
            print_choices()
            self.__menu_action = choice()
      
    def find_customer(self):
        """ Customer options. All sub menus are nested functions within this function. """
    
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
                
        def delete_customer(customer_to_change):
            """ Takes in a customer and removes them from the database. """
            while self.__submenu_action.lower() != "b":
                self.print_header()
                customer_id = customer_to_change.get_customer_id()
                print("{:>100}".format(self.__customer_service.delete_customer(customer_id)))
                self.__customer_service.write_db_to_file()
                print("\n" * 2)
                
                print("{:>101}".format("R. Back to previous menu"))
                print("{:>97}".format("B. Back to main menu"))
                self.__submenu_action = input("{:>97}".format("Enter menu action: "))
                if self.__submenu_action.lower() == "r":
                    break
                if self.__submenu_action.lower() == "b":
                    self.__menu_action = "b"
                    break

        def print_bottom_menu():
            print("\n" * 2)
            print("{:>102}".format("Change customer options:\n"))
            print("{:>97}".format("1. Update first name"))
            print("{:>94}".format("2. Update surname"))
            print("{:>102}".format("3. Update passport number"))
            print("{:>105}".format("4. Update credit card number"))
            print("{:>95}".format("5. Delete customer"))        
            
        def find_customer_by_icelandic_id():
            """ Operations for looking for a customer using and Icelandic id number. """
            self.__submenu_action = ""
            while self.__submenu_action.lower() != "b":
                self.print_header()
                icelandic_registration_number = input("{:>113}".format("Enter Icelandic registration number: "))
                if len(self.__customer_service.get_customer_by_icelandic_id(icelandic_registration_number)) == 0:
                    print("{:>114} {} {}".format("No customer with registration number", 
                                                 icelandic_registration_number, "found."))
                    print("{:>105}".format("R. Back to previous menu"))
                    print("{:>96}".format("B. Back to main menu"))
                    print("\n" * 2)
                    self.__submenu_action = input("{:>95}".format("Enter menu action: "))
                    if self.__submenu_action.lower() == "r":
                        break
                    if self.__submenu_action.lower() == "b":
                        self.__menu_action = "b"
                        break
                else:
                    for customer in self.__customer_service.get_all_customers():
                        if customer.get_identity_number() == icelandic_registration_number:
                            customer_to_change = customer
                            print("{:>100}".format(customer_to_change.__str__()))
                    print_bottom_menu()
                    print("{:>101}".format("R. Back to previous menu"))
                    print("{:>97}".format("B. Back to main menu"))
                    print("\n" * 2)
                    self.__submenu_action = input("{:>96}".format("Enter menu action: "))
                    if self.__submenu_action.lower() == "r":
                        break
                    if self.__submenu_action == "1":
                        update_first_name(customer_to_change)
                    if self.__submenu_action == "2":
                        update_surname(customer_to_change)
                    if self.__submenu_action == "2":
                        update_passport_number(customer_to_change)
                    if self.__submenu_action == "4":
                        update_cc_number(customer_to_change)
                    if self.__submenu_action == "5":
                        delete_customer(customer_to_change)
                    if self.__submenu_action.lower() == "b":
                        self.__menu_action = "b"
                        break
                    
        def find_customer_by_passport_id():
            """ Available operations when customer has been looked up by passport id. """
            self.__submenu_action = ""
            while self.__submenu_action.lower() != "b":
                self.print_header()
                passport_number = input("{:>100}".format("Enter passport number: "))
                if len(self.__customer_service.get_customer_by_passport_no(passport_number)) == 0:
                    print("{:>100} {} {}".format("No customer with passport number", passport_number, "found."))
                    print("{:>101}".format("R. Back to previous menu"))
                    print("{:>97}".format("B. Back to main menu"))
                    print("\n" * 2)
                    if self.__submenu_action.lower() == "r":
                        break
                    if self.__submenu_action.lower() == "b":
                        self.__menu_action = "b"
                        break
                else:
                    for customer in self.__customer_service.get_all_customers():
                        if customer.get_passport_id().upper() == passport_number.upper():
                            customer_to_change = customer
                            print("\n" * 2)
                            print("{:>100}".format(customer.__str__()))
                    print_bottom_menu()
                    print("{:>101}".format("R. Back to previous menu"))
                    print("{:>97}".format("B. Back to main menu"))
                    print("\n" * 2)
                    self.__submenu_action = input("{:>95}".format("Enter menu action: "))
                    if self.__submenu_action.lower() == "r":
                        break
                    if self.__submenu_action == "1":
                        update_first_name(customer_to_change)
                    if self.__submenu_action == "2":
                        update_surname(customer_to_change)
                    if self.__submenu_action == "2":
                        update_passport_number(customer_to_change)
                    if self.__submenu_action == "4":
                        update_cc_number(customer_to_change)
                    if self.__submenu_action == "5":
                        delete_customer(customer_to_change)
                    if self.__submenu_action.lower() == "b":
                        self.__menu_action = "b"
                        break

        while self.__menu_action.lower() != "b":
            self.print_header()
            print("{:>93}".format("Find customer by:\n"))
            print("{:>107}".format("1. Icelandic registration number"))
            print("{:>93}".format("2. Passport number"))
            print("{:>95}".format("B. Back to main menu"))
            print("\n" * 2)
            self.__menu_action = input("{:>94}".format("Enter menu action: "))
            if self.__menu_action == "1":
                find_customer_by_icelandic_id()
            if self.__menu_action == "2":
                find_customer_by_passport_id()
        self.__menu_action = ""

    def return_car(self):
        """ Function to return a car. """
        order_to_return = ""
        valid_input = False
        while self.__menu_action.lower() != "b":
            self.print_header()
            order_to_return_id = input("{:>96}".format("Enter order number: "))
            while not valid_input:
                try:
                    int(order_to_return_id)
                    order_to_return_id = order_to_return_id.upper()
                    valid_input = True
                except ValueError:
                    print("Invalid order number. Please enter a new order number.")
                    order_to_return_id = input("{:>96}".format("Enter order number: "))
            order_to_return = self.__order_service.get_order(order_to_return_id)
            if isinstance(order_to_return, str):
                print()
                print("{:>111}".format(order_to_return))
                print()
            else:
                valid_input = False
                mileage_at_return = input("{:>113}".format("Enter car's total mileage at return: "))
                while not valid_input:
                    try:
                        mileage_at_return = int(mileage_at_return)
                        valid_input = True
                    except ValueError:
                        print("Invalid mileage entered. Please enter a valid mileage number.")
                        mileage_at_return = input("{:>113}".format("Enter car's total mileage at return: "))
                car_to_return = self.__car_service.get_car(order_to_return.get_car_id())
                mileage_at_departure = int(car_to_return.get_mileage())
                extra_cost = self.get_total_cost_for_extra_kilometers(order_to_return_id, mileage_at_return, mileage_at_departure)
                print()
                print("{:>132}{}{}".format("Extra cost to be paid for additional kilometers driven: ", int(extra_cost), " ISK"))
                print()
                car_to_return.set_mileage(str(mileage_at_return)) #SETJA NÝJA MILAGEIÐ Á BÍLINN
                order_to_return.set_additional_cost(str(extra_cost)) #SETJA EXTRA COST Á ORDER
                self.__order_service.write_db_to_file() #SAVEA BÁÐA DB
                self.__car_service.write_db_to_file()
            print("{:>96}".format("B. Back to main menu"))
            print("\n" * 2)
            self.__menu_action = input("{:>95}".format("Enter menu action: "))
            if self.__menu_action.lower() == "b":
                self.__menu_action = "b"
                break



    def usage_history(self):
        """ Menu for showing usage history for cars/customers. """
        def usage_history_customer():
            """ Shows the usage history for a customer. """
            while self.__submenu_action.lower() != "b":
                self.print_header()
                customer_id = input("{:>103}".format("Please enter a customer id: "))
                valid_input = False
                while not valid_input:
                    try:
                        int(customer_id)
                        customer_orders_list = self.__order_service.get_all_orders_for_customer(customer_id)
                        valid_input = True
                    except ValueError:
                        print("Invalid customer id. Please try again.")
                        customer_id = input("{:>103}".format("Please enter a customer id: "))
                print("\n" * 2)
                if len(customer_orders_list) == 0:
                    print("{:>100}".format("No orders for customer found."))
                else:
                    for order in customer_orders_list:
                        print("{:>100}".format(order.__str__()))
                print("\n" * 2)
                print("{:>99}".format("R. Back to previous menu"))
                print("{:>95}".format("B. Back to main menu"))
                print("\n" * 2)
                self.__submenu_action = input("{:>94}".format("Enter menu action: "))
                if self.__submenu_action.lower() == "r":
                    break
                if self.__submenu_action.lower() == "b":
                    self.__menu_action = "b"
                    break



        def usage_history_car():
            """ Shows the usage history for a car. """
            while self.__submenu_action.lower() != "b":
                self.print_header()
                car_id = input("{:>98}".format("Please enter a car id: "))
                valid_input = False
                while not valid_input:
                    try:
                        str(car_id)
                        car_orders_list = self.__order_service.get_all_orders_for_car(car_id)
                        valid_input = True
                    except ValueError:
                        print("{:>100}".format("Invalid customer id. Please try again."))
                        car_id = input("{:>98}".format("Please enter a car id: "))
                print("\n" * 2)
                if len(car_orders_list) == 0:
                    print("{:>100}".format("No orders for car found."))
                else:
                    for order in car_orders_list:
                        print("{:>120}".format(order.__str__()))
                print("\n" * 2)
                print("{:>99}".format("R. Back to previous menu"))
                print("{:>95}".format("B. Back to main menu"))
                print("\n" * 2)
                self.__submenu_action = input("{:>94}".format("Enter menu action: "))
                if self.__submenu_action.lower() == "r":
                    break
                if self.__submenu_action.lower() == "b":
                    self.__menu_action = "b"
                    break

        while self.__menu_action.lower() != "b":
            self.print_header()

            print("{:>111}".format("1. Show usage history for a customer"))
            print("{:>106}".format("2. Show usage history for a car"))
            print("{:>95}".format("B. Back to main menu"))
            print("\n" * 2)
            self.__menu_action = input("{:>94}".format("Enter menu action: "))
            if self.__menu_action.lower() == "1":
                usage_history_customer()
            if self.__menu_action.lower() == "2":
                usage_history_car()
            
    def get_additional_insuarance_cost(self, reg_num):
        """ Takes in the car registration number and gets the cost of daily rental
        and calculates the cost of additional insurance"""        
        car = self.__car_service.get_car(reg_num)                 
        #The cost of insurance is the 75% of the price of a days rental
        return int(car.get_category_price()) * float(0.75)
     
     
    def get_cost_without_additions(self, order_id):
        """ Takes in an order id and gets that order from the database 
        and calculates the cost without additions"""        
        order = self.__order_service.get_order(order_id)
        #We need the number of days the car is being rent for to calculat the total cost
        start_date = datetime.datetime.strptime(order.get_rent_date_from(), "%d/%m/%Y")
        end_date = datetime.datetime.strptime(order.get_rent_date_to(), "%d/%m/%Y")           
        number_of_days = abs((end_date-start_date).days)
        #From the order object, we obtain the registration number for the car and 
        #send it into get_car_by_regnum to get car category price
        car = self.__car_service.get_car(order.get_car_id())
        return int(car.get_category_price()) * number_of_days                     

    def write_to_db(self):
        """ Writes all databases to files. Call this method before program ends. """
        #KLÁRA AÐ SKRIFA ÞESSI METHOD FYRIR ALLA KLASA OG BÆTA VIÐ HÉR SVO DRASLIÐ SAVEIST ÞEGAR FORRITIÐ HÆTTIR
        self.__order_service.write_db_to_file()
        self.__car_service.write_db_to_file()


    def update_car_mileage(self, reg_num, mileage):
        ''' Updates milage of a car, with mileage driven by customer'''
        car = self.__car_service.get_car(reg_num)
        #gets current mileage stauts and adds to mileage driven by customer
        new_mileage = int(car.get_mileage()) + int(mileage)
        car.set_mileage(new_mileage)
        #Write changes to db
        self.__car_service.write_db_to_file()
        return car

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
                + " - Kilometers driven: " + order.get_bought_km()
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

    
    def get_total_cost_for_extra_kilometers(self, order_id, mileage_driven, mileage_at_departure):
        for order in self.__order_service.get_all_orders():
            if order.get_order_id() == order_id:
                #get total number of days rented for
                start_date = datetime.datetime.strptime(order.get_rent_date_from(), "%Y-%m-%d")
                end_date = datetime.datetime.strptime(order.get_rent_date_to(), "%Y-%m-%d")           
                number_of_days = abs((end_date-start_date).days)
                
                #get total number of kilometers driven on rental period
                number_of_kilometers_included = number_of_days * self.__max_kilometer_per_day

                #calculate the cost of extra kilometers
                if mileage_driven > number_of_kilometers_included + mileage_at_departure:
                    extra_kilometers = mileage_driven - (number_of_kilometers_included + mileage_at_departure)
                    return extra_kilometers * self.get_additional_cost_extra_mileage(order_id)
                else:
                    return 0
    
    def get_additional_cost_extra_mileage(self, order_id):
        """ Takes in an order id and gets that order from the database and calculates the cost of additional insurance"""        
        order = self.__order_service.get_order(order_id)                   
        #From the order object, we obtain the registration number for the car and send 
        #it into get_car_by_regnum to get car category price
        car = self.__car_service.get_car(order.get_car_id())                 
        #The cost of additional millage over 100km is 1% of daily rental cost
        return (int(car.get_category_price()) * 0.01)

