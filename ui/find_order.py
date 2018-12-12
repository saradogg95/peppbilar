

done = False
while not done:
    order_id = input("Please input the order id (q to quite): ")
    order = self.__order_service.get_order(order_id)
    if len(order) == 0:
        print(order)
    elif order_id == "q":
        done = True
    else:
        done = True

def print_choices():
    print("Press 1 to change order id.")
    print("Press 2 to change order date.")
    print("Press 3 to change rent rate from.")
    print("Press 4 to change rent date to.")
    print("Press 5 to change additional insurance.")
    print("Press b for back.")

def choice():
    while True:
        try:
            self.__menu_action = input("Please input your choice: ").lower()
            if self.__menu_action == "b":
                return self.__menu_action
            value_error_check = int(self.__menu_action)
            return self.__menu_action
        except ValueError:
            print("Wrong input.")

print_choices()
self.__menu_action = choice()
while self.__menu_action.lower() != "b":
    if self.__menu_action == 1:
        change_order_id = input("Please input order id change: ")
        order.set_order_id(change_order_id)
        print(order)
    if self.__menu_action == 2:
        change_order_date = input("Please input order date change: ")
        order.set_order_date(change_order_date)
        print(order)
    if self.__menu_action == 3:
        change_rent_date_from = input("Please input rent rate from change: ")
        order.set_rent_date_from(change_rent_date_from)
        print(order)    
    if self.__menu_action == 4:
        change_rent_date_to = input("Please input rent date to change: ")
        order.set_rent_date_to(change_rent_date_to)
        print(order)
    if self.__menu_action == 5:
        change_additional_insurance = input("Please input additional insurance change: ")
        order.set_additional_insurance(change_additional_insurance)
        print(order)
    print_choices()
    self.__menu_action = choice()





