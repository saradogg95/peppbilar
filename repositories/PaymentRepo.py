#Data Access Layer
#__payments: list
#get_payment_info(order_id): list
#add_payment(): none

#Þarf að skoða þennan klasa betur kv Sara

from models.Payment import Payment
import csv

class PaymentRepository:

    def __init__(self):
        self.__payments = []

    def __str__(self):
        return "{}".format(self.__payments)

    def __repr__(self):
        return self.__str__()

    def get_payment_info(self, order_id):
        """Get payment info from order id"""
        self.__order_id = order_id
        with open("./data/payment.csv", "r", newline="") as payment_db:
            csv_dict = csv.DictReader(payment_db)
            for line in csv_dict:
                if line["order_id"] == self.__order_id:
                    new_id = Order(line["order_id"], line["order_date"], line["rent_date_from"],
                    ["rent_date_to"], ["customer_id"], ["car_id"])
                    return new_id

    def add_payment():
        """Adds payment"""
        with open("./data/payment.csv", "a+") as payment_db:
            id_ = Payment.get_id()
            basic_price = Payment.get_basic_price()
            insurance = Payment.get_add_insurance()
            additional_cost = Payment.get_additional_cost()
            orders_id = Payment.get_orders_id()
            payment_db.write("{}, {}, {}, {}, {}").format(id_, basic_price, insurance, 
                                                          additional_cost, orders_id)