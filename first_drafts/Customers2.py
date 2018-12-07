class Customers():
    def __init__(self, customer_ID=0, kt="", first_names="", surname="", country="", password=""):
        self.customer_ID = customer_ID
        self.kt = kt
        self.first_names = first_names
        self.surname = surname
        self.country = country
        self.password = password

    def __str__(self):
        return "{} {} {} {} {} {}".format(self.customer_ID, self.kt, self.first_names, self.surnames, self.country, self.passport)


    def get_customer_ID(self):
        return self.customer_ID
    
    def get_kt(self):
        return self.kt

    def get_first_names(self):
        return self.first_names
    
    def get_surname(self):
        return self.surname
    
    def get_country(self):
        return self.country
    
    def get_passport(self):
        return self.passport
    
