class Employee:
    
    def __init__(self, username="", password="", name="", address="", age=0, admin=0):
        
        self.__username = username
        self.__password = password
        self.__name = name
        self.__address = address
        self.__age = self.age_check(age)
        self.__admin = self.admin_check(admin)

    #Checks if the user input correct age e.g. age is not under 0 and and must be a number
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

    #checks if user input correct admin status, e.g. only accapts 0 for False and 1 for True
    def admin_check(self, admin):
        done = False
        while not done:
            if admin == 0:
                return False
            elif admin == 1:
                return True
            try:
                admin = int(input("Please input 1 if admin permision is true and 0 for false: "))
            except:
                print("Wrong input.")

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password
    
    def get_name(self):
        return self.__name
    
    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_admin_status(self):
        return self.__admin