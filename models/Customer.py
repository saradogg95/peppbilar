class Customer():
    def __init__(self, customer_ID=0, identity_number="", first_names="", surname="", citizenship="", passport_ID=""):
        self.__customer_ID = customer_ID
        self.__identity_number = identity_number
        self.__first_names = first_names
        self.__surname = surname
        self.__citizenship = citizenship
        self.__passport_ID = passport_ID

    def __str__(self):
        return "{} {} {} {} {} {}".format(self.__customer_ID, self.__identity_number, self.__first_names, self.__surname, self.__citizenship, self.__passport_ID)

    def get_customer_ID(self):
        return self.__customer_ID

    def get_identity_number(self):
        return self.__identity_number

    def get_first_names(self):
        return self.__first_names

    def get_surname(self):
        return self.__surname
    
    def get_citizenship(self):
        return self.__citizenship
    
    def get_passport_ID(self):
        return self.__passport_ID