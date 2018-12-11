from os import system, name
from services.CarServices import CarServices
from services.CustomerServices import CustomerServices
from services.EmployeeServices import EmployeeServices
from services.OrderServices import OrderServices
#from services.PaymentServices import PaymentServices verður sennilega ekki notað
from datetime import date
import datetime #skoða þetta aðeins
import calendar

from models.Car import Car
from models.Order import Order
from models.Employee import Employee
from models.Payment import Payment
from models.Customer import Customer

def identity_number_check():
    while True:
        identity_number = input("Enter valid identity number: ")
        try:
            if identity_number[-1] == '9':
                reference_year = 1900
            elif identity_number[-1] == '0':
                reference_year = 2000
            else:
                print("Wrong input.")
                continue
            birthday_day = int(identity_number[0:2])
            birthday_month = int(identity_number[2:4])
            birthday_year = int(identity_number[4:6]) + reference_year
            birthday = datetime.date(birthday_year, birthday_month, birthday_day)
            return identity_number
        except:
            print("{} is not a valid kennitala!".format(identity_number))

def customer_id_check():
    while True:
        try:
            customer_id = int(input("Please input customer id: "))
            return customer_id
        except ValueError:
            print("Wrong input.")

print("Please press 1 for icelandic customers.\nPress 2 for international customers.")

done = False
while not done:
    try:
        customer_input = int(input("Customer: "))
        done = True
    except ValueError:
        print("Wrong input.")

if customer_input == 1:

    customer_id = customer_id_check()
    if len(self.__customer_service.get_customer(customer_id)) == 0:

        identity_number = identity_number_check()
        first_names = input("Please input first name: ")
        surname = input("Please input last name: ")
        citizenship = input("Please input citizenship: ")
        passport_id = input("Please input passport id: ")        

        new_customer = Employee() 
        self.__customer_service.add_customer(new_customer)
    else:
        pass

elif customer_input == 2:

    customer_id = customer_id_check()

    passport_id = input("Enter valid passport id: ")