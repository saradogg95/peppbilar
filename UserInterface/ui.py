
class UserInterface:

    def __init__(self):

        #vantar að búa til service layers, en tengist öllum service layers rn
        self.__order_service = OrderService()
        self.__customer_service = CustomerService()
        self.__payment_service = PaymentService()
        self.__employee_service = EmployeeService()
        self.__car_service = CarService()

    def main_menu(self):
        
        action = ""

        while action != "q":
            self.print_choices(action)
            action = self.get_action()
            if action == 1:
                pass
            elif action == 2:
                pass
            elif action == 3:
                pass
            elif action == 4:
                pass
            elif action == 5:
                pass



    def get_action(self):
        correct_input_list = [1, 2, 3, 4, 5, "q"]
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

    def print_choices(self, action):
        if action == "":
            print("")
        elif:
        
        elif:

        else:

    #kannski mögulega prenta út fancy interface
    def __str__(self):
        pass

    def order_service_action(self):
        pass

    def customer_service_action(self):
        pass

    def payment_service_action(self):
        pass
    
    def employee_service_action(self):
        pass

    def car_service_action(self):
        pass