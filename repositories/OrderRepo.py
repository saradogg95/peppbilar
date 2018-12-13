import csv

import datetime

from models.Order import Order

class OrderRepository:

    def __init__(self):
        self.__orders = []


    def populate_order_list(self):
        """ Opens the database (csv) file and reads its contents. 
        If the file doesn't exist it is created with the columns of the file. """
        try:
            with open("./data/orders.csv", "r") as orders_db:
                csv_dict = csv.DictReader(orders_db)
                for line in csv_dict:
                    new_order = Order(line["Order_id"], line["Order_date"], 
                                      line["Rent_date_from"], line["Rent_date_to"],                                    
                                      line["Insurance_with_credit_card"],
                                      line["Bought_km"],
                                      line["Additional_Insurance"],
                                      line["Customer_id"], line["Car_id"])
                    self.__orders.append(new_order)
        except FileNotFoundError:
            with open("./data/orders.csv", "a+") as orders_db:
                orders_db.write("Order_id,Order_date,Rent_date_from,Rent_date_to," + 
                "Insurance_with_credit_card,Bought_km,Additional_Insurance,Customer_id,Car_id\n")

            
    def check_empty(self):
        """ Checks if the database list is empty. 
        Calls populate_order_list() if it is """
        if len(self.__orders) == 0:
            self.populate_order_list()

            
    def add_order(self, new_order):
        """ Adds a new order to the list of orders. """
        self.check_empty()
        self.__orders.append(new_order)

        
    def delete_order(self, index_number):
        """ Takes in an index number and deletes 
        the corresponding index from the database. """
        self.check_empty()
        self.__orders.pop(index_number)

        
    def get_customer_orders(self, customer_id):
        """ Takes in a customer id, gets all orders for 
        that customer id and returns as a list. """
        self.check_empty()
        customer_orders_list = []
        for order in self.__orders:
            if order.get_customer_id() == customer_id:
                customer_orders_list.append(order)

                
    def get_all_orders(self):
        """ Gets all orders from the database 
        and returns them as a list """
        self.check_empty()
        return self.__orders

    
    def write_db_to_file(self):
        """ Writes the database (self.__orders) to file. 
        This writes over the existing file so use with care. """
        self.check_empty()
        with open("./data/orders.csv", "w") as orders_db:
            orders_db.write("Order_id, Order_date, Rent_date_from, Rent_date_to, Insurance_with_credit_card," +
                            "Mileage_out, Mileage_in, Additional_Insurance, Customer_id, Car_id\n")
            for order in self.__orders:
                order_id = order.get_order_id().upper()
                order_date = order.get_order_date().upper()
                rent_date_from = order.get_rent_date_from().upper()
                rent_date_to = order.get_rent_date_to().upper()
                insurance_with_credit_card = order.get_insurance_with_credit_card().upper()
                bought_km = order.get_bought_km().upper()
                additional_insurance = order.get_additional_insurance().upper()
                customer_id = order.get_customer_id().upper()
                car_id = order.get_car_id().upper()
                orders_db.write("{},{},{},{},{},{},{},{},{},{}\n".format(order_id, order_date, rent_date_from, 
                                                                         rent_date_to, 
                                                                         insurance_with_credit_card,
                                                                         bought_km,
                                                                         additional_insurance,
                                                                         customer_id, car_id))
