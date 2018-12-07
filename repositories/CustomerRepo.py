import csv
from models.Customer import Customer

class customerRepository:
    
    def __init__(self):
        self.__customers = []

    def add_customer(self,identity_number):
        with open("Customer_grunnur_TBD.csv", "r") as customer_db:
            customer_ID = Customer.get_customer_ID
            identity_number = Customer.get_identity_number
            first_names = Customer.get_first_names
            surname = Customer.get_surname
            citizenship = Customer.get_citizenship
            passport_ID = Customer.get_passport_ID
            customer_db.write("{},{},{},{},{}").format(customer_ID, first_names, surname, citizenship,passport_ID)

    
    def get_customer(self, identity_number):
        with open("Customer_grunnur_TBD.csv", "a+") as customer_db:
            csv_dict = csv.DictReader(customer_db)
            for line in csv_dict:
                if line["kennitala"] == str(identity_number):
                    return line
        return None
    
    def get_all_customers(self):
        """ Returns a list of all customers """
        if len(self.__customers) == 0:
            self.__customers = self.read_customer_db()
        return self.__customers

    def read_customer_db(self):
        """ Reads a file with all customers and returns as a list"""
        try:
            with open("./data/customers.csv", "r") as customer_db:
                csv_dict = csv.DictReader(customer_db)
                for line in csv_dict:
                    new_customer = Customer(line["customer_ID"],line["identity_number"],line["first_names,surname"],line["citizenship"],line["passport_ID"])
                    self.__customers.append(new_customer)
        except FileNotFoundError:
            with open("./data/customers.csv", "a+") as customer_db:
                customer_db.write("customer_ID,identity_number,first_names,surname,citizenship,passport_ID\n")
        return self.__customers
