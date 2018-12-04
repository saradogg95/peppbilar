"""
id: int
type: string
category: string
manufacturer: string
registration_date: date
plate_number: string
mileage: int
is_available: bool
"""

class Car:
    def __init__(self, car_id=0, car_type="", category="", manufacturer="", registration_date="", plate_number="", mileage=0, is_available=True):
        self.__id = car_id
        self.__type = car_type
        self.__category = category
        self.__manufacturer = manufacturer
        self.__registration_date = registration_date
        self.__plate_number = plate_number
        self.__mileage = mileage
        self.__is_available = is_available
    
    def __str__(self):
        return "{} {} {} {} {} {} {} {}".format(self.__id, self.__type, self.__category, self.__manufacturer, self.__registration_date, self.__plate_number, self.__mileage, self.__is_available)