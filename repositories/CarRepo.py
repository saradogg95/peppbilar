import csv
from models.Car import Car



class CarRepository:
    def __init__(self):
        self.__cars = []
        self.__regNum = 0
        self.__available_cars = []

    def get_car(self, reg_num):
        """ Tekur inn bílnúmer. Ef bílnúmerið finnst í gagnarunninum þá er bílnum skilað. Skilar annars None"""
        self.__regNum = reg_num
        with open("./data/cars_test.csv", "r", newline="") as car_db: #breyta þessu í cars.csv fyrir fullan db
            csv_dict = csv.DictReader(car_db)
            for line in csv_dict:
                if line["regNum"] == self.__regNum:
                    new_car = Car(line["regNum"], line["make"],line["model"],line["category"],line["registration_date"],line["mileage"],line["available"])
                    return new_car
        return None

    def add_car(self, car):
        """ Bætir við bíl í gagnarunninn. """
        with open("./data/cars_test.csv", "a+") as car_db:
            regNum = car.get_regNum()
            make = car.get_make()
            category = car.get_category()
            manufacturer = car.get_manufacturer()
            registration_date = car.get_registration_date()
            mileage = car.get_mileage()
            availability = car.get_availability()
            car_db.write("{},{},{},{},{},{},{}\n".format(regNum, make, category, manufacturer, registration_date, mileage, availability))

    def get_all_cars(self):
        """ Fer í gegnum gagnagrunninn og bætir öllum bílum í lista sem er skilað """
        with open("./data/cars_test.csv", "r", newline="") as car_db: #breyta þessu í cars.csv fyrir fullan db
            csv_reader = csv.reader(car_db)
            next(csv_reader)
            for line in csv_reader:
                #regNum,make,model,category,registration_date,mileage,available
                new_car = new_car = Car(line[0], line[1],line[2],line[3],line[4],line[5],line[6])
                self.__cars.append(new_car)
        return self.__cars

    def get_available_cars(self):
        """ Fer í gegnum gagnagrunninn og bætir öllum tiltækum bílum í lista sem er skilað """
        with open("./data/cars_test.csv", "r") as car_db: #breyta þessu í cars.csv fyrir fullan db
            csv_dict = csv.DictReader(car_db)
            for line in csv_dict:
                if line["available"] == "True":
                    new_car = new_car = Car(line["regNum"], line["make"],line["model"],line["category"],line["registration_date"],line["mileage"],line["available"])
                    self.__available_cars.append(new_car)
        return self.__available_cars
