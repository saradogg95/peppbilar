class Customer:
    
    def __init__(self, customer_id=0, identity_number="", first_names="", 
                 surname="", citizenship="", passport_id="", credit_card_no=""):
        self.__customer_id = customer_id
        self.__identity_number = identity_number
        self.__first_names = first_names
        self.__surname = surname
        self.__citizenship = citizenship
        self.__passport_id = passport_id
        self.__credit_card_no = credit_card_no

        
    def __str__(self):
        return "{}, {}, {}, {}, {}, {}, {}".format(self.__customer_id, self.__identity_number, 
                                             self.__first_names, self.__surname, 
                                             self.__citizenship, self.__passport_id,
                                             self.__credit_card_no)

    def get_customer_id(self):
        return self.__customer_id

    
    def get_identity_number(self):
        return self.__identity_number
 

    def get_first_names(self):
        return self.__first_names
 

    def get_surname(self):
        return self.__surname
       
        
    def get_citizenship(self):
        return self.__citizenship

    
    def get_credit_card_no(self):
        return self.__credit_card_no
   

    def get_passport_id(self):
        return self.__passport_id

    
    def set_citizenship(self, citizenship):
        self.__citizenship = citizenship

        
    def set_first_name(self, first_name):
        self.__first_names = first_name
    
    
    def set_surname(self, surname):
        self.__surname = surname
    
    
    def set_credit_card_no(self, credit_card_no):
        self.__credit_card_no = credit_card_no
