class Car:
    def __init__(self, regNum=0, make="", category="", manufacturer="", registration_date="", mileage=0, is_available=True):
        self.__regNum = regNum
        self.__make = make
        self.__category = category
        self.__manufacturer = manufacturer
        self.__registration_date = registration_date
        self.__mileage = mileage
        self.__availability = is_available
    
    def __str__(self): #gera þetta print aðeins flottara
        return "{} {} {} {} {} {} {}".format(self.__regNum, self.__make, self.__category, self.__manufacturer, self.__registration_date, self.__mileage, self.__availability)

    def get_regNum(self):
        return self.__regNum

    def get_make(self):
        return self.__make

    def get_category(self):
        return self.__category

    def get_manufacturer(self):
        return self.__manufacturer

    def get_registration_date(self): #datetime á þetta
        return self.__registration_date

    def get_mileage(self):
        return self.__mileage

    def get_availability(self):
        return self.__availability