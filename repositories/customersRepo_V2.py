import csv
from Models.Customers import Customers

class customerRepository:
    
    def __init__(self):
        self.customers = []

    def add_customer(self,identity_number):
        with open("Customer_grunnur_TBD.csv", "r") as customer_db:
            customer_ID = Customers.get_customer_ID
            identity_number = Customers.get_identity_number
            first_names = Customers.get_first_names
            surname = Customers.get_surname
            citizenship = Customers.get_citizenship
            passport_ID = Customers.get_passport_ID
            customer_db.write("{},{},{},{},{}").format(customer_ID, first_names, surname, citizenship,passport_ID)

    
    def get_customer(self, identity_number):
        with open("Customer_grunnur_TBD.csv", "a+") as customer_db:
            csv_dict = csv.DictReader(customer_db)
            for line in csv_dict:
                if line["kennitala"] == self.identity_number:
                    return line
        return None

