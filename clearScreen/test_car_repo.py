from repositories.CarRepo import CarRepository
from services.CarServices import CarServices

def main():
    car_db = CarRepository()
    car_service = CarServices()
    car = car_db.get_cars()
    cars = car_service.get_price_by_category()
    print(cars)


main()