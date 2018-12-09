import csv
from models.Car import Car

class CarRepository:
    def __init__(self):
        self.__cars = []

    def add_car(self, car):
        """ Takes in a car and writes to the database """
        with open("./data/cars.csv", "a+") as car_db:
            try:
                regNum = car.get_regNum()
                make = car.get_brand()
                category = car.get_category()
                category_price = car.get_category_price()
                manufacturer = car.get_manufacturer()
                registration_date = car.get_registration_date()
                mileage = car.get_mileage()
                availability = car.get_availability()
                car_db.write("{},{},{},{},{},{},{}\n"
                .format(regNum, make, category, manufacturer, registration_date, mileage, availability)) #laga þegar formatið á db er komið á hreint
            except:
                return None
            finally:
                car_db.close()

    def open_csv(self):
        """Returns list of cars from csv file"""
        self.__cars = []
        with open("./data/cars.csv", "r") as car_db:
            try:
                csv_dict = csv.DictReader(car_db)
                for line in csv_dict:
                    new_car = Car(line["regNum"], line["brand"], line["model"], line["category"], line["category_price"], line["registration_date"], line["mileage"], line["available"])
                    self.__cars.append(new_car)
                return self.__cars
            except:
                return self.__cars
            finally:
                car_db.close()

    def get_cars(self):
        """ Returns a list of all cars in the database """
        self.__cars = self.open_csv()
        return self.__cars


