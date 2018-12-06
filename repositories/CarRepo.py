import csv
from models.Car import Car



class CarRepository:
    def __init__(self):
        self.__cars = []
        self.__available_cars = []

    def get_car(self, get_regNum):
        """ Takes in a registration number and returns the car with that registration number. If no car is found returns None """
        with open("./data/cars.csv", "r", newline="") as car_db:
            csv_dict = csv.DictReader(car_db)
            for line in csv_dict:
                if line["regNum"] == get_regNum:
                    new_car = Car(line["regNum"], line["make"],line["model"],line["category"],line["registration_date"],line["mileage"],line["available"])
                    return new_car
        return None

    def add_car(self, car):
        """ Takes in a car and writes to the database """
        with open("./data/cars.csv", "a+") as car_db:
            regNum = car.get_regNum()
            make = car.get_make()
            category = car.get_category()
            manufacturer = car.get_manufacturer()
            registration_date = car.get_registration_date()
            mileage = car.get_mileage()
            availability = car.get_availability()
            car_db.write("{},{},{},{},{},{},{}\n".format(regNum, make, category, manufacturer, registration_date, mileage, availability)) #laga þegar formatið á db er komið á hreint

    def get_all_cars(self):
        """ Returns a list of all cars in the database """
        self.__cars = []
        with open("./data/cars.csv", "r", newline="") as car_db:
            csv_dict = csv.DictReader(car_db)
            for line in csv_dict:
                new_car = new_car = Car(line["regNum"], line["make"],line["model"],line["category"],line["registration_date"],line["mileage"],line["available"]) # laga þegar formatið á db er komið á hreint
                self.__cars.append(new_car)
        return self.__cars

    def get_available_cars(self):
        """ Returns a list of all available cars in the database """
        self.__cars = []
        with open("./data/cars.csv", "r") as car_db:
            csv_dict = csv.DictReader(car_db)
            for line in csv_dict:
                if line["available"] == "True":
                    new_car = new_car = Car(line["regNum"], line["make"],line["model"],line["category"],line["registration_date"],line["mileage"],line["available"]) # laga þegar formatið á db er komið á hreint
                    self.__cars.append(new_car)
        return self.__cars