from models.Order import Order
from repositories.OrderRepo import OrderRepository
from services.CarServices import CarServices
from datetime import datetime

class OrderServices:

    def __init__(self):
        self.__order_db = OrderRepository()
        self.__car_services = CarServices()

    def add_order(self, new_order):
        """ Takes in an order and adds it to the database. """
        self.__order_db.add_order(new_order)

    def get_order(self, order_id):
        """ Takes in an order id and gets that order from the database and returns it. If no order is found returns a string """
        for order in self.__order_db.get_all_orders():
            if order.get_order_id() == order_id:
                return order
        return "No order with order number {} found.".format(order_id)

    def get_customer_orders(self, customer_id):
        """ Takes in a customer id and returns a list with all orders for that customer. Returns and empty list if nothing is found. """
        customer_order_list = []
        for order in self.__order_db.get_all_orders():
            if order.get_customer_id() == customer_id:
                customer_order_list.append(order)
        return customer_order_list

    def get_all_orders(self):
        """ Returns a list of all orders in the database. """
        return self.__order_db.get_all_orders()

    def change_order(self, order_number, new_order):
        """ Takes in an order number and an order and replaces the old order with the new order. If no order with the order number is found the order taken in is added as an order. """
        for index, order in enumerate(self.__order_db.get_all_orders()):
            if order.get_order_id() == order_number:
                self.__order_db.delete_order(index)
        self.__order_db.add_order(new_order)

    def delete_order(self, order_number):
        """ Takes in an order number and deletes it. Returns a string stating whether the order was deleted or not found. """
        for index, order in enumerate(self.__order_db.get_all_orders()):
            if order.get_order_id() == order_number:
                self.__order_db.delete_order(index)
                return "Order number {} was deleted.".format(order_number)
        return "No order number {} found.".format(order_number)

    def write_db_to_file(self):
        self.__order_db.write_db_to_file()

    def get_additional_insuarance_cost(self, order_id):
        """ Takes in an order id and gets that order from the database and calculates the cost of additional insurance"""        
        for order in self.__order_db.get_all_orders():
            if order.get_order_id() == order_id:           
                """Check if additional inusarance was ordered"""
                if order.get_additional_insurance() == "TRUE":                
                    """From the order object, we obtain the registration number for the car and send it into get_car_by_regnum to get car category price"""
                    car = self.__car_services.get_car(order.get_car_id()) #Ekkert get_car_by_regnum                 
                    """The cost of insurance is the 75% of the price of a days rental"""
                    return int(car[0].get_category_price()) * float(0.75)
                else:
                   return None 
            else:
                return "No order with order number {} found.".format(order_id)
    
    def get_additional_cost_extra_millage(self, order_id):
        """ Takes in an order id and gets that order from the database and calculates the cost of additional insurance"""        
        for order in self.__order_db.get_all_orders():
            if order.get_order_id() == order_id:                      
                """From the order object, we obtain the registration number for the car and send it into get_car_by_regnum to get car category price"""
                car = self.__car_services.get_car(order.get_car_id())                 
                """The cost of additional millage over 100km is 1% of daily rental cost"""
                return int(car[0].get_category_price()) * 0.01
            else:
                return "No order with order number {} found.".format(order_id)

    def get_cost_without_additions(self, order_id):
        """ Takes in an order id and gets that order from the database and calculates the cost without additions"""        
        for order in self.__order_db.get_all_orders():
            if order.get_order_id() == order_id:  
                """We need the number of days the car is being rent for to calculat the total cost"""
                start_date = datetime.strptime(order.get_rent_date_from(), "%d/%m/%Y")
                end_date = datetime.strptime(order.get_rent_date_to(), "%d/%m/%Y")           
                number_of_days = abs((end_date-start_date).days)
                """From the order object, we obtain the registration number for the car and send it into get_car_by_regnum to get car category price"""
                car = self.__car_services.get_car(order.get_car_id())
                return int(car[0].get_category_price()) * number_of_days                     
            else:
                return "No order with order number {} found.".format(order_id)

