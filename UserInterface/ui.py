from services.CarServices import CarServices
from services.CustomerServices import CustomerServices
from services.EmployeeServices import EmployeeServices
from services.OrderServices import OrderServices
from services.PaymentServices import PaymentServices

from models.Car import Car
from models.Order import Order
from models.User import Employee
from 



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
            #eh til að deala við new order
            self.__order_service.add_new_order(new_order)
        elif:
            pass
        return action

    def customer_service_action(self):
        self.print_choices(location_flag)
        action = self.get_action()
        if action == 1:
            #eh til að deala við new customer
            self.__order_service.add_new_customer(new_customer)
        elif:
            pass
        return action

    def payment_service_action(self):
        self.print_choices(location_flag)
        action = self.get_action()
        if action == 1:
            #eh til að deala við new payment
            self.__order_service.add_new_payment(new_payment)
        elif:
            pass
        return action

    def employee_service_action(self):
        self.print_choices(location_flag)
        action = self.get_action()
        if action == 1:
            #eh til að deala við new employee
            self.__order_service.add_new_employee(new_employee)
        elif:
            pass
        return action

    def car_service_action(self):
        self.print_choices(location_flag)
        action = self.get_action()
        if action == 1:
            #eh til að deala við new car
            self.__order_service.add_new_car(new_car)
        elif:
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
            print("Press r to return to main menu"):

        #payment service options
        elif location_flag == "Payment menu":
            print("------------Payment menu options------------")
            print("Please chose one of the following options:")
            print("1. Add a new payment")
            print("Press r to return to main menu"):

        #employee service options
        elif location_flag == "Employee menu":
            print("------------Employee menu options------------")
            print("Please chose one of the following options:")
            print("1. Add a new employee")
            print("Press r to return to main menu"):

        #car service options
        elif location_flag == "Car menu":
            print("------------Car menu options------------")
            print("Please chose one of the following options:")
            print("1. Add a new car")
            print("Press r to return to main menu"):


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

    #kannski mögulega prenta út fancy interface
    def __str__(self):
        pass
