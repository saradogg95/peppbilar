import csv

class customerRepository:
    def __init__(self):
        self.customers = []
        self.identity_number = ""

    def get_customer(self,identity_number):
        self.identity_number = identity_number
        with open("Customer_grunnur_TBD.csv", "r") as customer_db:
            cvs_dict = csv.DictReader(customer_db)
            for line in csv_dict:
                if line["kennitala"] == self.identity_number:
                    return line
        return None
    
    def add_customer(self, identity_number):
        with open("Customer_grunnur_TBD.csv", "a+") as customer_db:
            identity_number = customer.get_identity_number()
            first_names = customer.get_first_names()
            surname = customer.get_surname()
            citizenship = customer.get_citizenship()
            customer_ID = customer.get_customer_ID()
            customer_db.write("{},{},{},{}").format(customer_ID, first_names, surname, citizenship,)

