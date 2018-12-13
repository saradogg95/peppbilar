from repositories.CarRepo import CarRepository

from services.CarServices import CarServices
from services.OrderServices import OrderServices

from ui.UI_test import UserInterface


def main():
    #car_db = CarRepository()
    #car_service = CarServices()
    order_service = OrderServices()
    #brands = car_service.get_brands()
    ui_test = UserInterface()
    all_orders = order_service.get_all_orders()

    upd_car = ui_test.update_car_mileage("FL447R","909")
    print(upd_car)
    history = ui_test.get_car_rent_history("RM198B")
    print(history)
    customer_history = ui_test.get_customer_rent_history("201710021")
    print(customer_history)

    car = car_db.get_cars()
    print(car)

   # print(brands)
   # cars = car_service.get_price_by_category()
   # print(car_service.get_price_by_category())
   # orders = OrderServices()
   # print("Additional cost is", orders.get_additional_insuarance_cost("1"))
   # print("Total cost is", orders.get_cost_without_additions("1"))
   # print(cars)


main()
