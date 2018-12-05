class Customers():
    def __init__(self, customer_ID=0, identity_number="", first_names="", surname="", citizenship="", passport_ID=""):
        self.customer_ID = customer_ID
        self.identity_number = identity_number
        self.first_names = first_names
        self.surname = surname
        self.citizenship = citizenship
        self.passport_ID = passport_ID

    def __str__(self):
        return "{} {} {} {} {} {}".format(self.customer_ID, self.identity_number, self.first_names, self.surname, self.country, self.passport_ID)

    def get_customer_ID(self):
        return self.customer_ID

    def get_identity_number(self):
        return self.identity_number

    def get_first_names(self):
        return self.first_names

    def get_surname(self):
        return self.surname
    
    def get_citizenship(self):
        return self.citizenship
    
    def get_passport_ID(self):
        return self.passport_ID

