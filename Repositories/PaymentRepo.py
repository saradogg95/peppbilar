#Data Access Layer
#__payments: list
#get_payment_info(order_id): list
#add_payment(): none

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
            order_id = Payment.get_id()
            


#order_id: string
#order_date: datetime
#rent_date_from: date
#rent_date_to: date
#customer_id: int
#car_id: int