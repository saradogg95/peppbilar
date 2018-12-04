import csv

class carRepository:
    def __init__(self):
        self.__cars = []
        self.__carId = 0

    def get_car(self):
        """ fallið opnar skránna, les það inn sem csv uppflettiskrá og skilar svo gildinu með key sem er bílnúmerið(car_id) """
        #self.__carId = car_id
        with open(".data/cars_test.csv", "r") as car_data:
            csv_dict = csv.DictReader(car_data)
            print(csv_dict)

    def add_car(self):
        pass

    def get_all_cars(self):
        with open(".data/cars_test.csv", "r") as car_data:
            csv_reader = csv.reader(car_data)
            next(csv_reader)
            for line in csv_reader:
                self.__cars.append(line)
        return self.__cars

    def get_available_cars(self):
        pass


#test

def main():
    carRepository()
    print(carRepository.get_car())

main()