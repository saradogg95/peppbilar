from models.Customer import Customer
from repositories.CustomerRepo import CustomerRepository

class CustomerServices:
    
    def __init__(self):
        
        self.__repository = CustomerRepository()
        self.__customers = []
    
    def add_order(self, new_order):
        self.__repository.add_customer(new_customer)