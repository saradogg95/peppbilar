from models.Car import Car
from repositories.CarRepo import CarRepository


class CarServices():
    def __init__(self):
        self.__repository = CarRepository()
        self.__cars = []

    def get_car(self, id):
        """ tekur inn bílnúmer og biður gagnagrunninn um það. gagnagrunnurinn skilar ordered dict með bíl sem finnst en annars None. 
        Þetta fall vinnur úr gögnunum og skilar streng með bílnum en annars streng að bíllinn finnist ekki"""
        get_car = self.__repository.get_car(id)
        if get_car != None:
            return get_car
        return "No car with registration number {} found".format(id)

    def add_car(self, car):
        """ tekur eintak af bíl og sendir áfram í gagnagrunninn til skrifunar """
        self.__repository.add_car(car)

    def get_all_cars(self):
        """ biður um að fá lista yfir alla bíla senda úr gagnagrunninum og skilar í lista """
        self.__cars = self.__repository.get_all_cars()
        return self.__cars

    def get_available_cars(self):
        """ biður um lista yfir alla sem eru ekki í útleigu úr gagnagrunninum og skilar í lista """
        self.__cars = self.__repository.get_available_cars()
        return self.__cars