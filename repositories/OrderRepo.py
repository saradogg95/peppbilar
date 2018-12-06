import csv
from models.Order import Order


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
            order_db.write("{},{},{},{},{},{}\n".format(order_id, order_date, rent_date_from, 
                                                            rent_date_to, customer_id, car_id))
    
    def get_order(self, order_id):
        """ tekur við númeri viðskiptavins, sækir pöntunina í gagnagrunninn og skilar pöntun. Skilar None ef engin pöntun finnst á viðskiptavin """
        with open("./data/orders.csv", "r") as order_db:
            csv_dict = csv.DictReader(order_db)
            for line in csv_dict:
                if line["Order_id"] == str(order_id):
                    new_order = Order(line["Order_id"], line["Order_date"], line["Rent_date_from"], line["Rent_date_to"], line["Customer_id"], line["Car_id"])
                    return new_order
        return None

    def get_customer_orders(self, customer_id):
        """ tekur við númeri viðskiptavins, nær í allar pantanir á hans númeri og skilar þeim sem lista """
        with open("./data/orders.csv", "r") as order_db:
            csv_dict = csv.DictReader(order_db)
            for line in csv_dict:
                if line["Customer_id"] == str(customer_id):
                    new_order = Order(line["Order_id"], line["Order_date"], line["Rent_date_from"], line["Rent_date_to"], line["Customer_id"], line["Car_id"])
                    self.__orders.append(new_order)
        return self.__orders

    def get_all_orders(self):
        """ Fer í gegnum gagnagrunninn og bætir öllum pöntunum í lista sem er skilað """
        with open("./data/orders.csv", "r", newline="") as order_db:
            csv_reader = csv.reader(order_db)
            next(csv_reader)
            for line in csv_reader:
                #Order_id,Order_date,Rent_date_from,Rent_date_to,Customer_id,Car_id
                new_order = Order(line[0], line[1], line[2], line[3], line[4], line[5])
                self.__orders.append(new_order)
        return self.__orders