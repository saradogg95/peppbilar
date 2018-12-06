

class OrderRepository:

    def __init__(self):

        self.__orders = []

    def add_order(self, new_order):
        with open("./data/orders.csv", "a+") as order_db:
        
        # laga tilit til order

            regNum = car.get_regNum()
            make = car.get_make()
            category = car.get_category()
            manufacturer = car.get_manufacturer()
            registration_date = car.get_registration_date()
            mileage = car.get_mileage()
            availability = car.get_availability()
            car_db.write("{},{},{},{},{},{},{}\n".format(regNum, make, category, manufacturer, registration_date, mileage, availability))