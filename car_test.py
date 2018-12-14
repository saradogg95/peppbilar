from models.Car import Car
from repositories.CarRepo import CarRepository

def main():
    car_db = CarRepository()
    get_car = car_db.get_car("VA579D")
    print(get_car)

    #car1 = Car()
    #print(car1)
    #car_db.add_car(car1)

    all_cars = car_db.get_all_cars()
    for car in all_cars:
        print(car)
    print(all_cars)
    #available_cars = car_db.get_available_cars()
    #for car in available_cars:
    #    print(car)
    #print(available_cars)


main()