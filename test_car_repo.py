from repositories.CarRepo import CarRepository

from services.CarServices import CarServices
from services.OrderServices import OrderServices
from ui.UI_test import UserInterface


def main():
    car_db = CarRepository()
    car_service = CarServices()
    order_service = OrderServices()
    brands = car_service.get_brands()
    ui_test = UserInterface()
    all_orders = order_service.get_all_orders()
    updated_order = ui_test.update_order_mileage("1", 900)

    print(updated_order)
    print(all_orders)
    
    extra_cost = ui_test.get_total_cost_for_extra_kilometers("1")
    print(extra_cost)


    car_m_a = ui_test.update_car_mileage_and_availability("VA579D", "500")
    hist = ui_test.get_car_rent_history("VA579D")
    print(hist)
    cust_hist = ui_test.get_customer_rent_history("100")
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
