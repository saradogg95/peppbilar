import csv

class customerRepository:
    """Default values for every attribute, as the values will be provided in separate functions, 
    depending on whether customer is already registered, or not."""
    def __init__(self, identity_nr="", passport_nr="", first_names="", surname="", citizenship="", customer_ID=0):
        self.identity_nr = identity_nr
        self.passport_nr = passport_nr
        self.first_names = first_names
        self.surname = surname
        self.citizenship = citizenship
        self.customer_ID = customer_ID
    
    def __str__(self):
        """This printut is an overview, either for new customer, or customer who's already registered."""
        return ("\nCustomer ID: {}\nName: {} {}\nCountry code: {}\nIdentity number: {}\nPassport number: {}"
        .format(self.customer_ID, self.first_names, self.surname, self.citizenship, self.identity_nr, 
        self.passport_nr))


def get_identity_nr():
    """First requested value is kennitala; if left blank, next, passport number will be requested."""
    id = (input("\nPEPP CARS says:\nTo register order, please enter ICELANDIC IDENTITY NUMBER, "
    "or leave blank if not applicable:\n"))
    return id
    
def get_passport_nr():
    """Passport number requested, if Icelandic identity number is left blank."""
    pid = input("No Icelandic identity number; so please enter PASSPORT NUMBER:\n")
    return pid

def get_first_names():
    fn = input("Please enter first name, or first name and second name:\n")
    return fn

def get_surname():
    sn = input("Please enter surname:\n")
    return sn

def get_citizenship():
    cs = input("Please enter country code (from passport):\n")
    return cs

def get_new_customer_ID(newest_customer_ID):
    """The value for newest_customer_ID should be the highest value from the first column of the csv file."""
    ncid = newest_customer_ID + 1
    return ncid
        
def add_to_csv(customerRepository):
    """This creates a string to add to the csv file."""
    entry = ("{};{};{};{};{}".format(customerRepository.customer_ID, customerRepository.identity_nr, 
    customerRepository.first_names, customerRepository.surname, customerRepository.citizenship, 
    customerRepository.passport_nr))
    with open("Customer_grunnur_TBD.csv","a") as file:
        file.write(entry)


def get_customer(customerRepository):
    """This function calls on all the other functions, to create the customer."""
    key_value_provided = False
    """Becomes True when either identity number or passport number have been provided."""
    returning_customer = False
    """Becomes True when customer has been found in the csv file."""
    customer_IDs = []
    newest_customer_ID = 0
    """The last two variables are for creating a customer ID for new customers."""

    """Asks for Icelandic identity number:"""

    customerRepository.identity_nr = get_identity_nr()
        
    if customerRepository.identity_nr != "":

        """Passport number is not needed if customer has an Icelandic identity number."""

        key_value_provided = True
        customerRepository.passport_nr = ""
    else:

        """If customer doesn't have an Icelandic identity number, passport number is needed."""

        customerRepository.passport_nr = get_passport_nr()
        if customerRepository.passport_nr != "":
            key_value_provided = True
        
    while key_value_provided == False:

        """Activated if neither identity number, nor passport number are provided."""

        print("Customer must provide either Icelandic identity number or passport number!")
        operation = input("1. Icelandic identity number.\n2. Passport number\n3.Cancel")
        if operation == "1":
            customerRepository.identity_nr = get_identity_nr()
            if customerRepository.passport_nr != "":
                key_value_provided = True
        elif operation == "2":
            if customerRepository.passport_nr != "":
                key_value_provided = True
            customerRepository.passport_nr = get_passport_nr()
        elif operation == "3":
            exit()

    with open("Customer_grunnur_TBD.csv","r") as customer_db:
        csv_dict = csv.DictReader(customer_db)
        if customerRepository.identity_nr != "":
            for line in csv_dict:
                if line["Kennitala"] == customerRepository.identity_number:

                    """Customer found in csv, from identity number."""

                    returning_customer = True

                    """Rest auto-populates, from csv file."""

                    customerRepository.first_names = line["Eiginnafn/eiginnöfn"]
                    customerRepository.surname = line["Eftirnafn"]
                    customerRepository.citizenship = line["Ríkisfang"]
                    returning_customer == True
                    pass
        if customerRepository.passport_nr != "":
            for line in csv_dict:
                if line["Vegabréfsnúmer"] == customerRepository.passport_nr:

                    """Customer found in csv, from passport number."""

                    returning_customer = True

                    """Rest auto-populates, from csv file."""

                    customerRepository.first_names = line["Eiginnafn/eiginnöfn"]
                    customerRepository.surname = line["Eftirnafn"]
                    customerRepository.citizenship = line["Ríkisfang"]
                    returning_customer == True
                    pass

        """If customer not found in csv, the newest customer ID is extracted here, from the open file."""

        for line in csv_dict:
            customer_IDs.append(line["Customer_ID"])
            print(customer_IDs)
        newest_customer_ID = customer_IDs[0]
                                
        if returning_customer == True:
            """This is the end of the line, if customer exists in the csv file."""
            print(customerRepository)
            options = input("Press 1 to proceed, any other key to cancel.")
            if options == "1":
                return customerRepository
            else:
                return None
        else:
                
            """If customer doesn't exist in csv, info should be provided, though cutomer_ID will be generated."""
                
            customerRepository.customer_ID = get_new_customer_ID(newest_customer_ID)
            customerRepository.first_names = get_first_names()
            customerRepository.surname = get_surname()
            customerRepository.citizenship = get_citizenship()
            print(customerRepository)
            options = input("Press 1 to save and proceed, any other key to cancel.")                
            if options == "1":
                    
                """Customer added to csv file."""

                add_to_csv(customerRepository)
                return customerRepository
            else:
                return None


first_customer = get_customer(customerRepository)
#first_customer = customerRepository()
#first_customer = get_customer()
print(first_customer)

#test existing kennitala = '1405787219'
#test existing passport number = 'F51998059438'

