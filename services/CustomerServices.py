from models.Customer import Customer
from repositories.CustomerRepo import customerRepository

class CustomerServices:
    
    def __init__(self):
        
        self.__repository = customerRepository()
        self.__customers = []
    
    def add_customer(self, new_customer):
        self.__repository.add_customer(new_customer)