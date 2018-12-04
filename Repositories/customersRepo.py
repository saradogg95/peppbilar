import csv

class customerRepository:
    def __init__(self):
        self.customer = []

    def __str__(self):
        return "Name: {} {}, Citizenship: {}, Customer ID: {}".format(self.customer["Eiginnafn/eiginnöfn"],self.customer["Eftirnafn"],self.customer["Ríkisfang"])

    def search_identity_number(identity_number):
        with open("Customer_grunnur.csv","r") as customer_db:
            csv_dict = csv.DictReader(customer_db)
            for line in csv_dict:
                if line["Kennitala"] == identity_number:
                    return line
        return None

    def search_passport(passport_number):
        with open("Customer_grunnur.csv","r") as customer_db:
            csv_dict = csv.DictReader(customer_db)
            for line in csv_dict:
                if line["Vegabréfsnúmer"] == passport_number:
                    return line
        return None
                
    def search_key():
        """Leitar eftir kennitölu eða vegabréfsnúmer."""
        customer = []
        input_key = input("Search by:\n1.Icelandic identity number\n2.Passport number\n")
        if input_key == "1":
            identity_number = input("Enter identity number:\n")
            customer = search_identity_number(identity_number)
            return customer
        elif input_key == "2":
            passport_number = input("Enter passport number:\n")
            customer = search_passport(passport_number)
            return customer
        else:
            return None

    customer = search_key()
    print(customer)

#test kennitala = '1405787219'
#test passport number = 'F51998059438'

#    def get_customer(self, customer_ID):
#        """Leitar að viðskiptavini í grunni."""
#        with open("Customer_grunnur.csv", "r") as customer_db:
#            csv_dict = csv.DictReader(customer_db)
#            for line in csv_dict:
#                if line["customer_ID"] == self.customer_ID:
#                    return line
#            return None

