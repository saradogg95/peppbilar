class Car:
    
    def __init__(self, reg_num=0, brand="", model="", category="", 
                 category_price="", registration_date="", mileage=0, 
                 is_available=True):
        self.__reg_num = reg_num
        self.__brand = brand
        self.__model = model
        self.__category = category
        self.__registration_date = registration_date
        self.__mileage = mileage
        self.__availability = is_available
        self.__category_price = category_price
    
    
    def __str__(self):
        car_info = self.__brand + " " + self.__model + ", " + self.__registration_date
        return "{:<15s}{:<45s}{:<15s}{:<15s}".format(self.__reg_num, car_info, self.__category, 
                                                self.__category_price)

    def get_reg_num(self):
        return self.__reg_num
    
    
    def get_brand(self):
        return self.__brand
 

    def get_category(self):
        return self.__category
        
        
    def get_model(self):
            return self.__model   
    
    
    def get_category_price(self):
        return self.__category_price
  

    def get_registration_date(self):
        return self.__registration_date
    
    
    def get_mileage(self):
        return self.__mileage
    
    
    def get_availability(self):
        return self.__availability

    
    def set_mileage(self, mileage):
        self.__mileage = mileage
