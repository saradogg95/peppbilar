<<<<<<< HEAD
from models.Payment import Payment
from repositories.PaymentRepo import PaymentRepository

class PaymentServices():

        def __init__(self):
                self.__repository = PaymentRepository()
                self.__payments = []

=======
#Service Layer
#get_payment_info(order_id): list
#add_payment(): none

from models.Payment import Payment
from repositories.PaymentRepo import PaymentRepository

class PaymentServices():

        def __init__(self):
                self.__repository = PaymentRepository()
                self.__payments = []

>>>>>>> b4878ec26d15c181addc9787b4c3501de4c15191
        def get_payment_info(self, order_id):
                get_payment_info = self.__repository.get_payment_info(order_id)
                if get_payment_info != None:
                        return get_payment_info
                return "No payment information for order {} found".format(order_id)

        def add_payment(self, new_payment):
                #self.__repository.add_payment(new_payment)
                pass