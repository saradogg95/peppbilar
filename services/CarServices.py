from models.Car import Car
from repositories.CarRepo import CarRepository


class CarServices():
    def __init__(self):
        self.__repository = CarRepository()
        self.__cars = []

    def get_car(self, regNum):
        """ Takes in a registration number and asks the database to get it. If no such car is found it returns None otherwise return the car """     
        all_cars = self.__repository.get_cars()
        for line in all_cars:
            if line.get_regNum() == regNum:
                self.__cars.append(line)
                return self.__cars
            else:
                return "No car with registration number {} found".format(regNum)

    def add_car(self, car):
        """ Takes in a car and send to the database for writing """
        self.__repository.add_car(car)

    def get_all_cars(self):
        """ Gets all cars from the database and returns as a list """
        all_cars = self.__repository.get_cars()
        for line in all_cars:
            self.__cars.append(line.get_brand())
        return self.__cars

    def get_available_cars(self):
        """ Gets all cars from the database and returns as a list """
        all_cars = self.__repository.get_cars()
        for line in all_cars:
            if line.get_availability() == "True":
                self.__cars.append(line)
        return self.__cars

    def get_price_by_category(self):
        """ Gets all cars from the database and returns as a list """
        all_cars = self.__repository.get_cars()
        for line in all_cars:
            if line.get_category_price() not in self.__cars:
                self.__cars.append(line)
        return self.__cars

    def get_brands(self):
        """ Gets all cars from the database and returns as a list """
        all_cars = self.__repository.get_cars()
        for line in all_cars:
            if line.get_brand() not in self.__cars:
                self.__cars.append(line.get_brand())
        return self.__cars
