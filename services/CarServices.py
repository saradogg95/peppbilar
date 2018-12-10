from models.Car import Car
from repositories.CarRepo import CarRepository


class CarServices():
    def __init__(self):
        self.__repository = CarRepository()

    def get_car(self, regNum):
        """ Takes in a registration number and asks the database to get it. If no such car is found it returns None otherwise return the car """     
        all_cars = self.__repository.get_cars()
        cars = []
        for line in all_cars:
            if line.get_reg_num() == regNum:
                cars.append(line)
                return cars
        return "No car with registration number {} found".format(regNum)

    def add_car(self, car):
        """ Takes in a car and send to the database for writing """
        self.__repository.add_car(car)

    def get_all_cars(self):
        """ Gets all cars from the database and returns as a list """
        all_cars = self.__repository.get_cars()
        cars = []
        for line in all_cars:
            cars.append(line)
        return self.__cars

    def get_unavailable_cars(self):
        """ Gets all cars from the database and returns as a list """
        cars = []
        for line in self.__repository.get_cars():
            if line.get_availability().upper() == "False":
                cars.append(line)
        return cars

    def get_price_by_category(self):
        """ Gets all cars from the database and returns as a list """
        all_cars = self.__repository.get_cars()
        cars = []
        for line in all_cars:
            if line.get_category() + " - " + line.get_category_price() + " ISK" not in cars:
                cars.append(line.get_category() + " - " + line.get_category_price() + " ISK")
        return cars

    def get_brands(self):
        """ Gets all cars from the database and returns as a list """
        all_cars = self.__repository.get_cars()
        cars = []
        for line in all_cars:
            if line.get_brand() not in cars:
                cars.append(line.get_brand())
        return cars
