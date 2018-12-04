

class Employee:

    def __init__(self, username, password, name, address, age, admin=False):
        
        self.__username = username
        self.__password = password
        self.__name = name
        self.__address = address
        self.__age = self.age_check(age)
        self.__admin = admin

    def age_check(self, age):
        done = False
        while not done:
            try:
                age = int(age)
                if age >= 0:
                    done = True
                else:
                    done = False
                    age = input("Please input a number >= 0 for age: ")
            except:
                age = input("Please input a number >= 0 for age: ")
            return age

    def __str__(self):
        return "{}, {}, {}, {}, {}, {}".format(self.__username, self.__password, self.__name, 
                                    self.__address, self.__age, self.__admin)

    def admin_check(self)

abi = Employee("doctor", 123, "Valtýr Oddsson", "Sævangur 22", -1, admin=True)
print(abi)