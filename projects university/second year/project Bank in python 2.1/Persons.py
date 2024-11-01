class persons:

    def __init__(self, f_name,l_name,date_of_birth,phone,email,gender):
        self.f_name = f_name
        self.l_name = l_name
        self.date_of_birth = date_of_birth
        self.phone = phone
        self.email = email
        self.gender = gender




    @property
    def f_name(self):
        return self.__f_name

    @f_name.setter
    def f_name(self,f_name):

        self.__f_name = f_name


    @property
    def l_name(self):
        return self.__l_name

    @l_name.setter
    def l_name(self,l_name):
        # while not self.f_name.isalpha():
            # print("Please enter a valid name")
        self.__l_name = l_name


    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self,date_of_birth):
        self.__date_of_birth = date_of_birth

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self,phone):
        self.__phone = phone

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self,email):
        self.__email = email

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self,gender):
        self.__gender = gender


    def print_client(self):

            s=(f"Name : {self.f_name} {self.l_name} \n"
               f"Phone : {self.phone} \n"
               f"Date of Birth : {self.date_of_birth} \n"
               f"Email : {self.email} \n"
               f"Gender : {self.gender}")
            print(s)


