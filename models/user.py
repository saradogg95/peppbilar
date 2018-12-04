

class Employee:

    def __init__(self, username, password, name, address, age, admin=0):
        
        self.__username = username
        self.__password = password
        self.__name = name
        self.__address = address
        self.__age = self.age_check(age)
        self.__admin = self.admin_check(admin)

    def age_check(self, age):
        done = False
        while not done:
            try:
                age = int(age)
                if age >= 0:
                    done = True
                else:
                    age = input("Please input a number >= 0 for age: ")
            except:
                print("Wrong input.")
            return age

    def __str__(self):
        return "{}, {}, {}, {}, {}, {}".format(self.__username, self.__password, self.__name, 
                                    self.__address, self.__age, self.__admin)

    def __repr__(self):
            return self.__str__()

    def admin_check(self, admin):
        done = False
        while not done:
            if admin == 0:
                return 0
            elif admin == 1:
                return 1
            try:
                admin = int(input("Please input 1 if admin permision is true and 0 for false: "))
            except:
                print("Wrong input.")

    def get_username(self):
        return self.__username

    def 


abi = Employee("doctor", 123, "Valtýr Oddsson", "Sævangur 22", -1, admin=2)
print(abi)