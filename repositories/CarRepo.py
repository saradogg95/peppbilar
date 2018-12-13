import csv
from models.Car import Car


class CarRepository:
    
    def __init__(self):
        self.__cars = []

    def check_empty(self):
        """ Checks if the database list is empty. 
        Calls populate_order_list() if it is """
        if len(self.__cars) == 0:
            self.populate_car_list()

    def add_car(self, car):
        """ Takes in a car and writes to the database """
        self.check_empty()
        self.__cars.append(car)

    def populate_car_list(self):
        """ Opens the database (csv) file and reads its contents. 
        If the file doesn't exist it is created with the columns of the file. """
        try:
            with open("./data/cars.csv", "r") as cars_db:
                csv_dict = csv.DictReader(cars_db)
                for line in csv_dict:
                    new_car = Car(line["reg_num"],line["brand"], 
                                  line["model"],line["category"],line["category_price"],line["registration_date"],line["mileage"])
                    self.__cars.append(new_car)
        except FileNotFoundError:
            with open("./data/cars.csv", "w") as cars_db:
                cars_db.write("reg_num,brand,model,category,category_price,registration_date,mileage")

    def get_cars(self):
        """ Returns a list of all cars in the database """
        self.check_empty()
        return self.__cars

    def write_db_to_file(self):
        """ Writes the database (self.__cars) to file. 
        This writes over the existing file so use with care. """
        self.check_empty()
        with open("./data/cars.csv", "w") as cars_db:
                cars_db.write("reg_num,brand,model,category,category_price,registration_date, mileage\n")
                for car in self.__cars:
                    reg_num = car.get_reg_num()
                    brand = car.get_brand()
                    model = car.get_model()
                    category = car.get_category()
                    category_price = car.get_category_price()
                    registration_date = car.get_registration_date()
                    mileage = car.get_mileage()
                    cars_db.write("{},{},{},{},{},{},{}\n".format(reg_num, brand, model, category, category_price, registration_date, mileage))