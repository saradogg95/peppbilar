

class OrderRepository:

    def __init__(self):

        self.__orders = []

    def add_order(self, new_order):
        with open("./data/orders.csv", "a+") as order_db:
            order_id = new_order.get_order_id()
            order_date = new_order.get_order_date()
            rent_date_from = new_order.get_rent_date_from()
            rent_date_to = new_order.get_rent_date_to()
            customer_id = new_order.get_customer_id()
            car_id = new_order.get_car_id()
            order_db.write("{},{},{},{},{},{},{}\n".format(order_id, order_date, rent_date_from, rent_date_to, customer_id, car_id))