from models.Customer import Customer
from repositories.CustomerRepo import customerRepository

class CustomerServices:
    
    def __init__(self):
        
        self.__repository = customerRepository()
        self.__customers = []
    
    def add_customer(self, new_customer):
        self.__repository.add_customer(new_customer)

    def change_customer(self, new_customer):
        """ Takes in a customer and updates their information """
        new_list = []
        if len(self.__customers) == 0:
            self.__customers = self.__repository.get_all_customers()
        for customer in self.__customers:
            if customer.get_customer_ID() == new_customer.get_customer_ID():
                customer.append(new_customer)
            else:
                customer.append(customer)
        self.__customers = new_list
        return self.__customers
