class Car:
    
    def __init__(self, reg_num="0", brand="", model="", category="", 
                 category_price="", registration_date="", mileage="0"):
        self.__reg_num = reg_num.upper()
        self.__brand = brand.upper()
        self.__model = model.upper()
        self.__category = category.upper()
        self.__registration_date = registration_date.upper()
        self.__mileage = mileage.upper()
        self.__category_price = category_price.upper()
    
    
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
    
    
    def set_mileage(self, mileage):
        self.__mileage = mileage
