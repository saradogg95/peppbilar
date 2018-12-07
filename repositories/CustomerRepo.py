import csv
from models.Customer import Customer

class customerRepository:
    
    def __init__(self):
        self.customers = []

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
                if line["kennitala"] == self.identity_number:
                    return line
        return None