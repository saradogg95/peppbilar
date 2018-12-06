from models.Order import Order
from repositories.OrderRepo import OrderRepository

class OrderServices:

    def __init__(self):

        self.__repository = OrderRepository()
        self.__orders = []
    
    def add_order(self, new_order):
        self.__repository.add_order(new_order)