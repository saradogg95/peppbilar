from repositories.CarRepo import CarRepository

def main():
    car_db = CarRepository()
    car = car_db.get_cars()
    print(car)


main()