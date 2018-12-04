import csv
from models.car import Car


class carRepository:
    def __init__(self):
        self.__cars = []
        self.__regNum = 0
        self.__available_cars = []

    def get_car(self, reg_num):
        """ Tekur inn bílnúmer. Ef bílnúmerið finnst í gagnarunninum þá er bílnum skilað sem ordered dictionary. Prentar annars að bíllinn finnist ekki og skilar None"""
        self.__regNum = reg_num
        with open("./data/cars_test.csv", "r") as car_db: #breyta þessu í cars.csv fyrir fullan db
            csv_dict = csv.DictReader(car_db)
            for line in csv_dict:
                if line["regNum"] == self.__regNum:
                    return line
            #print("No car with registration number {} found".format(self.__regNum)) setja einhvern svona varnagla í layeri fyrir ofan ef gildið sem fengið er til baka er None
        return None

    def add_car(self, car):
        """ Bætir við bíl í gagnarunninn. """
        with open("./data/cars_test.csv", "a+") as car_db:
            regNum = car.get_regNum()
            make = car.get_make()
            category = car.get_category()
            manufacturer = car.get_manufacturer()
            registration_date = car.get_registration_date() #datetime á þetta
            mileage = car.get_mileage()
            availability = car.get_availability()
            car_db.write("{},{},{},{},{},{},{}\n".format(regNum, make, category, manufacturer, registration_date, mileage, availability))

    def get_all_cars(self):
        """ Fer í gegnum gagnagrunninn og bætir öllum bílum í lista sem er skilað """
        with open("./data/cars_test.csv", "r") as car_db: #breyta þessu í cars.csv fyrir fullan db
            csv_reader = csv.reader(car_db)
            next(csv_reader)
            for line in csv_reader:
                self.__cars.append(line)
        return self.__cars

    def get_available_cars(self):
        """ Fer í gegnum gagnagrunninn og bætir öllum tiltækum bílum í lista sem er skilað """
        with open("./data/cars_test.csv", "r") as car_db: #breyta þessu í cars.csv fyrir fullan db
            csv_dict = csv.DictReader(car_db)
            next(csv_dict)
            for line in csv_dict:
                if line["available"] == "True":
                    self.__available_cars.append(line)
        return self.__available_cars
