class Order:
    
    def __init__(self, order_id="", order_date="", rent_date_from="", 
                 rent_date_to="", insurance_with_credit_card = "", 
                 bought_km = "100", additional_insurance="False", customer_id="0", 
                 car_id="0", additional_cost="0"):
        self.__order_id = order_id.upper()
        self.__order_date = order_date.upper()
        self.__rent_date_from = rent_date_from
        self.__rent_date_to = rent_date_to.upper()
        self.__insurance_with_credit_card = insurance_with_credit_card.upper()
        self.__additional_insurance = additional_insurance.upper()
        self.__customer_id = customer_id.upper()
        self.__car_id = car_id.upper()
        self.__bought_km = bought_km.upper()
        self.__additional_cost = additional_cost.upper()

    def __str__(self):
        return "{} {} {} {} {} {} {} {} {}".format(self.__order_id, self.__order_date, 
                                          self.__rent_date_from, self.__rent_date_to,
                                          self.__insurance_with_credit_card,
                                          self.__bought_km,
                                          self.__additional_insurance,
                                          self.__customer_id, 
                                          self.__car_id)
                                          

    def get_order_id(self):
        return self.__order_id
 
    def get_order_date(self):
        return self.__order_date

    def get_rent_date_from(self):
        return self.__rent_date_from

    def get_rent_date_to(self):
        return self.__rent_date_to

    def get_additional_insurance(self):
        return self.__additional_insurance

    def get_insurance_with_credit_card(self):
        return self.__insurance_with_credit_card

    def get_customer_id(self):
        return self.__customer_id

    def get_car_id(self):
        return self.__car_id

    def get_bought_km(self):
        return self.__bought_km

    def set_order_id(self, order_id):
        self.__order_id = order_id
 
    def set_order_date(self, order_date):
        self.__order_date = order_date
 
    def set_rent_date_from(self, rent_date_from):
        self.__rent_date_from = rent_date_from

    def set_rent_date_to(self, rent_date_to):
        self.__rent_date_to = rent_date_to
        
    def set_additional_insurance(self, additional_insurance):
        self.__additional_insurance = additional_insurance

    def get_additional_cost(self):
        return self.__additional_cost

    def set_additional_cost(self, additional_cost):
        self.__additional_cost = additional_cost

