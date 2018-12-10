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
        self.__order_service = OrderServices()
        self.__customer_service = CustomerServices()
        self.__payment_service = PaymentServices()
        self.__employee_service = EmployeeServices()
        self.__car_service = CarServices()

        
    def main_menu(self):
        """Main menu with choices"""
        location_flag = "Main menu"
        self.print_choices(location_flag)
        action = self.get_action()
        while action != "q":
            if action == "1":
                location_flag = "Order menu"
                while action != "r":
                    action = self.order_service_action(location_flag)
                location_flag = "Main menu"
            elif action == "2":
                location_flag = "Customer menu"
                while action != "r":
                    action = self.order_service_action(location_flag)
                location_flag = "Main menu"
            elif action == "3":
                location_flag = "Payment menu"
                while action != "r":
                    action = self.order_service_action(location_flag)
                location_flag = "Main menu"
            elif action == "4":
                location_flag = "Employee menu"
                while action != "r":
                    action = self.order_service_action(location_flag)
                location_flag = "Main menu"
            elif action == "5":
                location_flag = "Car menu"
                while action != "r":
                    action = self.order_service_action(location_flag)
                location_flag = "Main menu"

            self.print_choices(location_flag)
            action = self.get_action()

            
    def order_service_action(self, location_flag):
        """Order service choices"""
        self.print_choices(location_flag)
        action = self.get_action()
        if action == "1":
            order_id = input("Order id: ")
            car_id = input("Car id: ")
            customer_id = input("Customer id: ")
            order_date = input("Order date: ")
            rent_date_from = input("Rent date from: ")
            rent_date_to = input("Rent date to: ")
            new_order = Order(order_id, order_date, rent_date_from, rent_date_to, customer_id, car_id)
            self.__order_service.add_order(new_order)
        #elif:
            #pass
        return action

    
    def customer_service_action(self):
        """Customer service choices"""
        self.print_choices(location_flag)
        action = self.get_action()
        if action == "1":
            customer_ID = input("Customer id: ")
            identity_number = input("Indentity number: ")
            first_names = input("First name: ")
            surname = input("Surname: ")
            citizenship = input("Citizenship: ")
            passport_ID = input("Passport id: ")
            new_customer = Customer(customer_ID, identity_number, first_names, surname, citizenship, passport_ID)
            self.__customer_service.add_customer(new_customer)
        #elif:
            #pass
        return action

    
    def payment_service_action(self, location_flag):
        """Payment service choices"""
        self.print_choices(location_flag)
        action = self.get_action()
        if action == "1":
            payment_id = input("Payment id: ")
            basic_price = input("Basic price: ")
            add_insurance = input("Add insurance: ")
            additional_cost = input("Additional cost: ")
            orders_id = input("Order id: ")
            new_payment = Payment(payment_id, basic_price, add_insurance, additional_cost, orders_id)
            self.__payment_service.add_payment(new_payment)
        #elif:
            #pass
        return action
    
    
    def employee_service_action(self, location_flag):
        """Employee service choices"""
        self.print_choices(location_flag)
        action = self.get_action()
        if action == "1":
            username = input("Username: ")
            password = input("Password: ")
            name = input("Name: ")
            address = input("Address: ")
            age = input("Age: ")
            admin = input("Admin: ")
            new_employee = Employee(username, password, name, address, age, admin)
            self.__employee_service.add_employee(new_employee)
        #elif:
            #pass
        return action

    
    def car_service_action(self, location_flag):
        """Car service choices"""
        self.print_choices(location_flag)
        action = self.get_action()
        if action == "1":
            reg_num = input("Registation number: ")
            brand = input("Brand: ")
            category = input("Category: ")
            manufacturer = input("Manufacturer: ")
            registration_date = input("Registration date: ")
            mileage = input("Mileage: ")
            is_available = input("Is available: ")
            new_car = Car(reg_num, brand, category, manufacturer, registration_date, mileage, is_available)
            self.__order_service.add_new_car(new_car)
        #elif:
            #pass
        return action

    
    def print_choices(self, location_flag):
        """Prints choices"""
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
        """Gets chosen option"""
        correct_input_list = ["1", "2", "3", "4", "5", "q", "r"]
        action = input("Please choose an option: ")

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
