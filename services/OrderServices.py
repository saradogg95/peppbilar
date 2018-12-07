from models.Order import Order
from repositories.OrderRepo import OrderRepository

class OrderServices:

    def __init__(self):

        self.__repository = OrderRepository()
        self.__orders = []
    
    def add_order(self, new_order):
        self.__repository.add_order(new_order)

    def get_order(self, order_id):
        get_order = self.__repository.get_order(order_id)
        if get_order != None:
            return get_order
        else: 
            return "No order with registration number {} found".format(order_id)
    
    def get_customer_orders(self, customer_id):
        get_orders = self.__repository.get_customer_orders(customer_id)
        if not get_orders:
            return "No orders for customer number {} found".format(customer_id)
        else:
            return get_orders

    def get_all_orders(self):
        get_orders = self.__repository.get_all_orders()
        orders_string = ""
        if not get_orders:
            return "No orders found"
        else:
            for item in get_orders:
                orders_string += item.__str__() + "\n"
            orders_string = orders_string[:-1]
            return orders_string
    
    def change_order(self, order_number):
        pass

    def delete_order(self, order_number):
        pass