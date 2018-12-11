import csv

from models.Car import Car


class CarRepository:
    
    def __init__(self):
        self.__cars = []

        
    def add_car(self, car):
        """ Takes in a car and writes to the database """
        with open("./data/cars.csv", "a+") as car_db:
            try:
                reg_num = car.get_reg_num()
                brand = car.get_brand()
                category = car.get_category()
                model = car.get_model()
                category_price = car.get_category_price()
                registration_date = car.get_registration_date()
                mileage = car.get_mileage()
                availability = car.get_availability()
                car_db.write("{},{},{},{},{},{},{},{},{}\n"
                .format(reg_num, brand, model, category, category_price, 
                        registration_date, mileage, availability))   
            except:
                return None

            
    def open_csv(self):
        """Returns list of cars from csv file"""
        self.__cars = []
        with open("./data/cars.csv", "r") as car_db:
            try:
                csv_dict = csv.DictReader(car_db)
                for line in csv_dict:
                    new_car = Car(line["reg_num"], line["brand"], line["model"], 
                                  line["category"], line["category_price"], 
                                  line["registration_date"], line["mileage"], 
                                  line["available"])
                    self.__cars.append(new_car)
                return self.__cars
            except:
                return self.__cars

            
    def get_cars(self):
        """ Returns a list of all cars in the database """
        self.__cars = self.open_csv()
        return self.__cars


