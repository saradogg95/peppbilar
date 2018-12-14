from models.Car import Car
from services.CarServices import CarServices



service = CarServices()


car1 = service.get_car("V79D")
print(car1)
car2 = service.get_car("VA579D")
print(car2)

#service.add_car(car2)

all_available = service.get_available_cars()
print("Available:")
for car in all_available:
    print(car)

all_cars = service.get_all_cars()
print("All:")
for car in all_cars:
    print(car)
