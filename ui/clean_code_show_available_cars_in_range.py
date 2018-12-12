#NOTE FOR TESTING: runs based on data-files: cars_afrit_afs and orders_afrit_afs.

#Clear screen:
from os import system, name 
  
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 
 
import datetime
from datetime import date
import calendar

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
        clear()
        print(("Date of car going out is: {}, {} {}, {}?".format(outdate_weekday.upper(), outdate_month.upper(), 
        working_date[0], working_date[2])))
        confirmation = input("1. Confirm\n2. Change\n")
        if confirmation == '1':
            valid_confirmation == True
            return True
        elif confirmation == '2':
            valid_confirmation == True
            return False

def start_and_return_confirmation(start_date, return_date):
#    from datetime import datetime
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
        clear()   
        quick_starting_date = input("Show availability FROM:\n1. Today.\n2. Another day this month.\n3. A day of another month this year.\n4. Next year.\n5. Cancel.\n")
        if quick_starting_date == '1':
            starting_date_registered = True
        elif quick_starting_date == '2':
            clear()
            change_working_date_day(working_date_out)
            valid_date = date_validation(working_date_out, this_is_today, working_date_out_saved)
            while valid_date == False:
                change_working_date_day(working_date_out)
                valid_date = date_validation(working_date_out, this_is_today, working_date_out_saved)
            else:
                starting_date_registered = True
        elif quick_starting_date == '3':
            clear()
            change_working_date_day_month(working_date_out)
            valid_date = date_validation(working_date_out, this_is_today, working_date_out_saved)
            while valid_date == False:
                change_working_date_day_month(working_date_out)
                valid_date = date_validation(working_date_out, this_is_today, working_date_out_saved)
            else:
                starting_date_registered = True
        elif quick_starting_date == '4':
            clear()
            change_working_date_day_month_year(working_date_out)
            starting_date_registered = True
        elif quick_starting_date == '5':
            order.clear()
            return False
        else:
            print("{} not a valid input".format(quick_starting_date))

        #Prompt for confirmation, control value updated:        
        clear()
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
    clear()
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
            clear()
            print("Invalid input. Check starting date.")
            print(("FROM: {}, {} {}, {}".format(outdate_weekday.upper(), outdate_month.upper(), 
            working_date[0], working_date[2])))
            valid_input = False
        else:
            clear()
            confirmation = start_and_return_confirmation(outdate, return_date)
            if confirmation == True:
                order.append(return_date)
                return True
            else:
                order.clear()
                return False


from services.OrderServices import OrderServices
from services.CarServices import CarServices
#For a list of all cars:
car_service = CarServices()
#For a list of all orders:
order_service = OrderServices()


def date_from_string(date_as_string):
    from datetime import date
    date_as_list = date_as_string.split('-')
    date_format = date(int(date_as_list[0]),int(date_as_list[1]),int(date_as_list[2]))
    return date_format

def get_clashing_orders(list_of_order_objects, out_date_car1, return_date_car1):
    #Car1 is the car that's being ordered, while car0 would be whichever car in database.
    clashing_orders_list = []
    for order in list_of_order_objects:
        if return_date_car1 >= date_from_string(str(order.get_rent_date_from())) and date_from_string(str(order.get_rent_date_to())) >= out_date_car1:
            clashing_orders_list.append(order.get_car_id())
    clashing_orders_set = set(clashing_orders_list)
    return clashing_orders_set

from datetime import date
from datetime import timedelta

#Listi yfir bíla sem eru lausir:
def get_clean_list(list_of_all_cars, clashing_orders):
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

#A new list for cars that meet criteria:
def filter_list(working_list, brand="", category="", registration_date=""):
    if brand == "" and category == "" and registration_date == "":
        filtered_working_list = working_list.copy()
    else:
        filtered_working_list = []
        if brand != "":
            for car in working_list:
                if car.get_brand() == brand:
                    filtered_working_list.append(car)
        if category != "":
            for car in working_list:
                if car.get_category().lower() == category.lower():
                    filtered_working_list.append(car)
        if registration_date != "":
            for car in working_list:
                if car.get_registration_date().lower() == registration_date.lower():
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
    clear()
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
            if category in categories:
                filter_list.append(category)
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
    
        list_of_all_cars = car_service.get_all_cars()
        list_of_all_orders = order_service.get_all_orders()
        clashing_orders = get_clashing_orders(list_of_all_orders, order[0], order[1])

        all_brands = get_all_brands(list_of_all_cars)
        all_categories = get_all_categories(list_of_all_cars)
        all_registration_dates = get_all_registration_dates(list_of_all_cars)

        specifications = search_filters(list_of_all_cars,filter_option,all_brands, all_categories, all_registration_dates)
        list_of_available = get_clean_list(list_of_all_cars, clashing_orders)
        filtered_list = filter_list(list_of_available, brand=specifications[0], category=specifications[1], registration_date=specifications[2])
        available_car_printout(filtered_list)
        index_num_or_quit = choose_car_from_list(filtered_list)
        while index_num_or_quit != 999:
            car_confirmation_prompt(order,filtered_list, index_num_or_quit)
            full_order_confirmed = True
            return True


def show_available_cars_in_range():
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
            print(order_X)
        else:
                return False
    else:
        return False
                        

show_available_cars_in_range()
