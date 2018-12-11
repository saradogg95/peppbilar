
from models.Payment import Payment
from repositories.PaymentRepo import PaymentRepository

class PaymentServices:

        def __init__(self):
                self.__repository = PaymentRepository()
                self.__payments = []

        def get_payment_info(self, order_id):
                get_payment_info = self.__repository.get_payment_info(order_id)
                if get_payment_info != None:
                        return get_payment_info
                return "No payment information for order {} found".format(order_id)

        def add_payment(self, new_payment):
                #self.__repository.add_payment(new_payment)
                pass

        """def get_additional_insurance_cost(self, has_additional_cost):
                if has_additional_cost:
                        return self.__basic_price * 0.15
                else:
                        return 0 """
        
        def get_total_cost(self):
                pass