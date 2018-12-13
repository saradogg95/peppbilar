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


    hist = ui_test.get_car_rent_history("RM198B\t")
    print(hist)
    cust_hist = ui_test.get_customer_rent_history("201710021")
    print(cust_hist)

    car = car_db.get_cars()
    print(car)

   # print(brands)
   # cars = car_service.get_price_by_category()
   # print(car_service.get_price_by_category())
   # orders = OrderServices()
   # print("Viðbótarkostnaður er", orders.get_additional_insuarance_cost("1"))
   # print("Heildarkostnaður er", orders.get_cost_without_additions("1"))
   # print(cars)


main()
