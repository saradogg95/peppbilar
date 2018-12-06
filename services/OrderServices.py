#from models.Car import Car P.S. vantar fyrir order class ef við ætlum að hafa hann
from repositories.OrderRepo import OrderRepository

class OrderServices:

    def __init__(self):

        self.__repository = OrderRepository()
        self.__orders = []
    
    def add_order(self, new_order):
        self.__repository.add_order(new_order)