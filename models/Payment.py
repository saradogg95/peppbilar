#id: string
#basic_price: float
#add_insurance: bool
#additional_cost: float
#orders_id: string
class Payment:

    def __init__(self, id_="", basic_price=0.0, add_insurance=False,
                 additional_cost=0.0, orders_id=""):
        self.__id_ = id_
        self.__basic_price = basic_price
        self.__add_insurance = add_insurance
        self.__additional_cost = additional_cost
        self.__orders_id = orders_id
        
    def __str__(self):
        return "{} {} {} {} {}".format(self.__id_, self.__basic_price, 
                                       self.__add_insurance, 
                                       self.__additional_cost, self.__orders_id)

    def get_id(self):
        return self.__id_

    def get_basic_price(self):
        return self.__basic_price

    def get_insurance(self):
        return self.__add_insurance

    def get_additional_cost(self):
        return self.__additional_cost

    def get_orders_id(self):
        return self.__orders_id