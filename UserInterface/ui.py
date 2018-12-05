
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
            

    def print_choices(self, action):
        pass

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