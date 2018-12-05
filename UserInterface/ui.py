
class UserInterface:

    def __init__(self):

        #vantar að búa til service layers, en tengist öllum service layers rn
        self.__order_service = OrderService()
        self.__customer_service = CustomerService()
        self.__payment_service = PaymentService()
        self.__employee_service = EmployeeService()
        self.__car_service = CarService()

    def main_menu(self):
        
        location_flag = "Main menu"

   

        while action != "q":

            self.print_choices(location_flag)
            action = self.get_action()


            if action == 1:
                location_flag = "Order menu"
                while action != "r":
                    action = self.order_service_action()
                #prentar þá út main menu annar heldur áfram að halda áfram að prenta út
                #menu fyrir 1
                location_flag = "Main menu"
            elif action == 2:
                pass
            elif action == 3:
                pass
            elif action == 4:
                pass
            elif action == 5:
                pass

    def order_service_action(self, location_flag):
        self.print_choices(location_flag)
        action = self.get_action()
        if action == 1:
            self.__order_service.add_new_order(new_order)
        elif:
            pass
        return action

    def print_choices(self, location_flag):
        #main screent print options
        if location_flag == "Main menu":
            print("------------Main screen options------------")
            print("Please chose one of the following options:")
            print("1. Orders")
            print("2. Customers")
            print("3. Payments")
            print("4. Employees")
            print("5. Cars")
            print("Press q to quit")

        #order service options
        elif location_flag == "Order menu":
            print("------------Order menu options------------")
            print("Please chose one of the following options:")
            print("1. Place a new order")
            print("Press r to return to main menu")
        
        #customer service options
        elif:

        #payment service options
        elif:

        #employee service options
        elif:

        #car service options
        elif:


    def get_action(self):
        correct_input_list = [1, 2, 3, 4, 5, "q", "r"]
        action = input("Please choose an option: ").lower()

        done = False

        while not done:
            if action not in correct_input_list:
                action = ""
                print("Wrong action, please chose one of the following options:")
                self.print_choices(action)
                action = input("Please choose an option: ").lower()
            else:
                done = True

        return action

    #kannski mögulega prenta út fancy interface
    def __str__(self):
        pass



    def customer_service_action(self):
        pass

    def payment_service_action(self):
        pass
    
    def employee_service_action(self):
        pass

    def car_service_action(self):
        pass