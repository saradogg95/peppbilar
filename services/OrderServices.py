from models.Order import Order
from repositories.OrderRepo import OrderRepository
from services.CarServices import CarServices


class OrderServices:

    def __init__(self):
        self.__order_db = OrderRepository()
     
    def add_order(self, new_order):
        """ Takes in an order and adds it to the database. """
        self.__order_db.add_order(new_order)
       
    def get_order(self, order_id):
        """ Takes in an order id and gets that order from the database and 
        returns it. If no order is found returns a string """
        for order in self.__order_db.get_all_orders():
            if order.get_order_id().upper() == order_id.upper():
                return order
        return "No order with order number {} found".format(order_id)
  
    def get_customer_orders(self, customer_id):
        """ Takes in a customer id and returns a list with all orders for 
        that customer. Returns and empty list if nothing is found. """
        customer_order_list = []
        for order in self.__order_db.get_all_orders():
            if order.get_customer_id() == customer_id:
                customer_order_list.append(order)
        return customer_order_list
 
    def get_all_orders(self):
        """ Returns a list of all orders in the database. """
        return self.__order_db.get_all_orders()

    def change_order(self, order_number, new_order):
        """ Takes in an order number and an order and replaces the old order with the new order. 
        If no order with the order number is found the order taken in is added as an order. """
        for index, order in enumerate(self.__order_db.get_all_orders()):
            if order.get_order_id() == order_number:
                self.__order_db.delete_order(index)
        self.__order_db.add_order(new_order)
   
    def delete_order(self, order_number):
        """ Takes in an order number and deletes it. Returns a string 
        stating whether the order was deleted or not found. """
        for index, order in enumerate(self.__order_db.get_all_orders()):
            if order.get_order_id() == order_number:
                self.__order_db.delete_order(index)
                return "Order number {} was deleted".format(order_number)
        return "No order number {} found".format(order_number)

    def get_all_orders_for_customer(self, customer_id):
        """ Takes in a customer id and returns a list with all orders for that customer. """
        orders = []
        for order in self.__order_db.get_all_orders():
            if order.get_customer_id() == customer_id:
                orders.append(order)
        return orders

    def get_all_orders_for_car(self, car_id):
        """ Takes in a car id and returns a list with all orders for that car. """
        orders = []
        for order in self.__order_db.get_all_orders():
            if order.get_car_id() == car_id:
                orders.append(order)
        return orders

    def write_db_to_file(self):
        self.__order_db.write_db_to_file()
