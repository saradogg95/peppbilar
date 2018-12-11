from repositories.CarRepo import CarRepository

from services.CarServices import CarServices
from services.OrderServices import OrderServices


def main():
    car_db = CarRepository()
    car_service = CarServices()
    car = car_db.get_cars()
    brands = car_service.get_brands()
    print(brands)
    cars = car_service.get_price_by_category()
    print(car_service.get_price_by_category())
    orders = OrderServices()
    print("Viðbótarkostnaður er", orders.get_additional_insurance_cost("1"))
    print("Heildarkostnaður er", orders.get_cost_without_additions("1"))
    print(cars)


main()
