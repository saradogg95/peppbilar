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

from datetime import datetime


class UserInterface:

    def __init__(self):
        #vantar að búa til service layers, en tengist öllum service layers rn
        self.__order_service = OrderServices()
        self.__customer_service = CustomerServices()
        self.__payment_service = PaymentServices()
        self.__employee_service = EmployeeServices()
        self.__car_service = CarServices()

    def main_menu(self):
        location_flag = "Main menu"
        while action != "q":
            self.print_choices(location_flag)
            action = self.get_action()
            if action == 1:
                location_flag = "Order menu"
                while action != "r":
                    action = self.order_service_action()
                location_flag = "Main menu"
            elif action == 2:
                location_flag = "Customer menu"
                while action != "r":
                    action = self.order_service_action()
                location_flag = "Main menu"
            elif action == 3:
                location_flag = "Payment menu"
                while action != "r":
                    action = self.order_service_action()
                location_flag = "Main menu"
            elif action == 4:
                location_flag = "Employee menu"
                while action != "r":
                    action = self.order_service_action()
                location_flag = "Main menu"
            elif action == 5:
                location_flag = "Car menu"
                while action != "r":
                    action = self.order_service_action()
                location_flag = "Main menu"

    def order_service_action(self, location_flag):
        self.print_choices(location_flag)
        action = self.get_action()
        if action == 1:
            order_id = input("Order id: ")
            car_id = input("Car id: ")
            customer_id = input("Customer id: ")
            order_date = input("Order date: ")
            rent_date_from = input("Rent date from: ")
            rent_date_to = input("Rent date to: ")
            new_order = Order(order_id, order_date, rent_date_from, rent_date_to, customer_id, car_id)
            self.__order_service.add_order(new_order)
        else:
            pass
        return action

    def customer_service_action(self):
        self.print_choices(location_flag)
        action = self.get_action()
        if action == 1:
            #eh til að deala við new customer
            self.__order_service.add_new_customer(new_customer)
        else:
            pass
        return action

    def payment_service_action(self):
        self.print_choices(location_flag)
        action = self.get_action()
        if action == 1:
            #eh til að deala við new payment
            self.__order_service.add_new_payment(new_payment)
        else:
            pass
        return action

    def employee_service_action(self):
        self.print_choices(location_flag)
        action = self.get_action()
        if action == 1:
            #eh til að deala við new employee
            self.__order_service.add_new_employee(new_employee)
        else:
            pass
        return action

    def car_service_action(self):
        self.print_choices(location_flag)
        action = self.get_action()
        if action == 1:
            #eh til að deala við new car
            self.__order_service.add_new_car(new_car)
        else:
            pass
        return action

    def print_choices(self, location_flag):
        #main screent print options
        if location_flag == "Main menu":
            print("------------Main screen options------------")
            print("Please chose one of the following options:")
            print("1. Orders")
            print("2. Customers")
            print("3. Payments")
            print("4. Employees")
            print("5. Cars")
            print("Press q to quit")

        #order service options
        elif location_flag == "Order menu":
            print("------------Order menu options------------")
            print("Please chose one of the following options:")
            print("1. Place a new order")
            print("Press r to return to main menu")
        
        #customer service options
        elif location_flag == "Customer menu":
            print("------------Customer menu options------------")
            print("Please chose one of the following options:")
            print("1. Add a new Customer")
            print("Press r to return to main menu")

        #payment service options
        elif location_flag == "Payment menu":
            print("------------Payment menu options------------")
            print("Please chose one of the following options:")
            print("1. Add a new payment")
            print("Press r to return to main menu")

        #employee service options
        elif location_flag == "Employee menu":
            print("------------Employee menu options------------")
            print("Please chose one of the following options:")
            print("1. Add a new employee")
            print("Press r to return to main menu")

        #car service options
        elif location_flag == "Car menu":
            print("------------Car menu options------------")
            print("Please chose one of the following options:")
            print("1. Add a new car")
            print("Press r to return to main menu")


    def get_action(self):
        correct_input_list = [1, 2, 3, 4, 5, "q", "r"]
        action = input("Please choose an option: ").lower()
        done = False
        while not done:
            if action not in correct_input_list:
                action = ""
                print("Wrong action, please chose one of the following options:")
                self.print_choices(action)
                action = input("Please choose an option: ").lower()
            else:
                done = True
        return action


    def get_additional_insuarance_cost(self, order_id):
        """ Takes in an order id and gets that order from the database and calculates the cost of additional insurance"""        
        for order in self.__order_db.get_all_orders():
            if order.get_order_id() == order_id:           
                #Check if additional inusarance was ordered
                if order.get_additional_insurance() == "TRUE":                
                    #From the order object, we obtain the registration number for the car and send it into get_car_by_regnum to get car category price
                    car = self.__car_services.get_car(order.get_car_id())                 
                    #The cost of insurance is the 75% of the price of a days rental
                    return int(car[0].get_category_price()) * float(0.75)
                else:
                   return None 
            else:
                return "No order with order number {} found.".format(order_id)
    
    def get_additional_cost_extra_millage(self, order_id):
        """ Takes in an order id and gets that order from the database and calculates the cost of additional insurance"""        
        for order in self.__order_db.get_all_orders():
            if order.get_order_id() == order_id:                      
                #From the order object, we obtain the registration number for the car and send it into get_car_by_regnum to get car category price
                car = self.__car_services.get_car(order.get_car_id())                 
                #The cost of additional millage over 100km is 1% of daily rental cost
                return int(car[0].get_category_price()) * 0.01
            else:
                return "No order with order number {} found.".format(order_id)

    def get_cost_without_additions(self, order_id):
        """ Takes in an order id and gets that order from the database and calculates the cost without additions"""        
        for order in self.__order_db.get_all_orders():
            if order.get_order_id() == order_id:  
                #We need the number of days the car is being rent for to calculat the total cost
                start_date = datetime.strptime(order.get_rent_date_from(), "%d/%m/%Y")
                end_date = datetime.strptime(order.get_rent_date_to(), "%d/%m/%Y")           
                number_of_days = abs((end_date-start_date).days)
                #From the order object, we obtain the registration number for the car and send it into get_car_by_regnum to get car category price
                car = self.__car_services.get_car(order.get_car_id())
                return int(car[0].get_category_price()) * number_of_days                     
            else:
                return "No order with order number {} found.".format(order_id)

    #kannski mögulega prenta út fancy interface
    def __str__(self):
        pass
