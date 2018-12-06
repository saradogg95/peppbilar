#from models.Car import Car P.S. vantar fyrir order class ef við ætlum að hafa hann
from repositories.CarRepo import CarRepository

class OrderServices:

    def __init__(self):

        self.__repository = CarRepository()
        self.__cars = []
    
    def add_car(self, order):
        
        self.__repository.add_order(order)