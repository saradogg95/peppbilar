import csv

from models.Customer import Customer


class CustomerRepository:
    
    def __init__(self):
        self.__customers = []
      
    
    def populate_customer_list(self):
        """ Opens the database (csv) file and reads its contents. 
        If the file doesn't exist it is created with the columns of the file. """
        try:
            with open("./data/customers.csv", "r") as customer_db:
                csv_dict = csv.DictReader(customer_db)
                for line in csv_dict:
                    new_customer = Customer(line["customer_ID"],line["identity_number"],
                                            line["first_names"],line["surname"],
                                            line["citizenship"],line["passport_ID"],
                                            line["credit_card_no"])
                    self.__customers.append(new_customer)
        except FileNotFoundError:
            with open("./data/customers.csv", "a+") as customer_db:
                customer_db.write("customer_ID,identity_number,first_names,surname,citizenship,passport_ID,credit_card_no\n")

                
    def check_empty(self):
        """ Checks if the database list is empty. Calls populate_customer_list() if it is """
        if len(self.__customers) == 0:
            self.populate_customer_list()

            
    def add_customer(self, new_customer):
        """ Takes in a new customer and adds it to the database. """
        self.check_empty()
        self.__customers.append(new_customer)

        
    def delete_customer(self, index_number):
        """ Takes in an index number ad removes it from the customer list. """
        self.check_empty()
        self.__customers.pop(index_number)

        
    def get_all_customers(self):
        """ Returns a list of all customers """
        self.check_empty()
        return self.__customers

    
    def write_customer_db_to_file(self):
        """ Writes the database (self.__customers) to file. 
        This writes over the existing file so use with care. """
        self.check_empty()
        with open("./data/customers.csv", "w") as customer_db:
            customer_ID = Customer.get_customer_id
            identity_number = Customer.get_identity_number
            first_names = Customer.get_first_names
            surname = Customer.get_surname
            citizenship = Customer.get_citizenship
            passport_ID = Customer.get_passport_id
            credit_card_no = Customer.get_credit_card_no
            customer_db.write("{},{},{},{},{}").format(customer_ID, identity_number, first_names, 
                                                       surname, citizenship, passport_ID, credit_card_no)
