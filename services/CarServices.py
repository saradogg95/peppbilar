from repositories.CarRepo import CarRepository


class CarServices():
    def __init__(self):
        self.__repository = CarRepository()

    def get_car(self, id):
        """ tekur inn bílnúmer og biður gagnagrunninn á að senda það. gagnagrunnurinn skilar ordered dict með bíl sem finnst en annars None. 
        Þetta fall vinnur úr gögnunum og skilar streng með bílnum en annars """

    def add_car(self, car):
        pass

    def get_all_cars(self):
        pass

    def get_available_cars(self):
        pass

