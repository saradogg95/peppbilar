from models.Customer import Customer

from repositories.CustomerRepo import CustomerRepository


class CustomerServices:
    
    def __init__(self):
        self.__customer_db = CustomerRepository()

        
    def add_customer(self, new_customer):
        self.__customer_db.add_customer(new_customer)

        
    def change_customer(self, customer_id, new_customer):
        """ Takes in a customer id and a customer and replaces the old customer with the new customer. 
        If no customer with the customer id is found the new customer added as a customer. """
        for index, customer in enumerate(self.__customer_db.get_all_customers()):
            if customer.get_customer_id() == customer_id:
                self.__customer_db.delete_customer(index)
        self.__customer_db.add_customer(new_customer)
    
    
    def get_customer(self, customer_id):
<<<<<<< HEAD
        """ Takes in a customer id, looks it up in the database and returns the customer. If no customer is found a empty list is returned. """
=======
        """ Takes in a customer id, looks it up in the database and returns the customer. 
        If no customer is found a string is returned. """
>>>>>>> 39afcb9f96bd3ac39d952aa57f18cc7f7fd1e253
        get_customer = []
        for customer in self.__customer_db.get_all_customers():
            if customer.get_customer_id() == customer_id:
                get_customer.append(customer)
        return get_customer

    
    def delete_customer(self, customer_id):
        """ Takes in a customer id and deletes it from the database. 
        Returns a string stating whether the customer was deleted or not. """
        for index, customer in self.__customer_db.get_all_customers():
            if customer.get_customer_id() == customer_id:
                self.__customer_db.delete_customer(index)
                return "Customer with customer id {} was deleted.".format(customer_id)
        return "No customer with customer id {} was found.".format(customer_id)

    
    def write_db_to_file(self):
        """ Writes the database to a file. Call this before the 
        program ends to save the state of the database. """
        self.__customer_db.write_customer_db_to_file()

        
    def get_all_customers(self):
        """ Returns a list of all customers. """
        return self.__customer_db.get_all_customers()

    
    def get_customer_by_icelandic_id(self, identity_number):
        """ Takes in a customer id, looks it up in the database and 
        returns the customer. If no customer is found a string is returned. """
        get_customer = []
        for customer in self.__customer_db.get_all_customers():
            if customer.get_identity_number() == identity_number:
                get_customer.append(customer)
        return get_customer

    
    def get_customer_by_passport_no(self, passport_no):
        """ Takes in a customer id, looks it up in the database and returns the customer. 
        If no customer is found a string is returned. """
        get_customer = []
        for customer in self.__customer_db.get_all_customers():
            if customer.get_passport_id().upper() == passport_no.upper(): #bæta svona á hin services föllin til að gera þau ekki case sensitive
                get_customer.append(customer)
        return get_customer
