

class Order:
    
    def __init__(self, order_id="", order_date="", rent_date_from="", 
                rent_date_to="", customer_id=0, car_id=0):
        self.__order_id = order_id
        self.__order_date = order_date
        self.__rent_date_from = rent_date_from
        self.__rent_date_to = rent_date_to
        self.__customer_id = customer_id
        self.__car_id = car_id

    def __str__(self):
        return "{} {} {} {} {} {}".format(self.__order_id, self.__order_date, 
                                          self.__rent_date_from, self.__rent_date_to, 
                                          self.__customer_id, self.__car_id)

    def get_order_id(self):
        return self.__order_id

    def get_order_date(self):
        return self.__order_date

    def get_rent_date_from(self):
        return self.__rent_date_from

    def get_rent_date_to(self):
        return self.__rent_date_to

    def get_customer_id(self):
        return self.__customer_id

    def get_car_id(self):
        return self.__car_id