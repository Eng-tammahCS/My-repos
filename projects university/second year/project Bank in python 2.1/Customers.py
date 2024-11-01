from Persons import persons
import sqlite3

class customers(persons):
    # self.__ID = persons.Number
    Number=0

    @classmethod
    def increase_id(cls):
        DB = sqlite3.connect('customers.db')
        cursor = DB.cursor()
        lastCustomer=cursor.execute("SELECT * FROM customers order by id desc ")
        cls.Number= lastCustomer.fetchone()[0]
        cls.Number+=1
        DB.close()
        return cls.Number



    status="ON"
    db = sqlite3.connect('customers.db')
    cr = db.cursor()
    cr.execute("create table if not exists customers"
               "(ID integer,f_name text"
               " ,l_name text,date_of_bihrth text,password text ,phone text"
               ",email text,gender text ,balance integer,Account_Type text)")

    db.commit()
    # cr.execute("")
    db.close()

    def __init__(self, f_name="",l_name="",date_of_birth="",passwprd="",phone="",email="",gender="",balance=0,id_Old_client=0):
        persons.__init__( f_name,l_name,date_of_birth,phone,email,gender)
        # customers.Number += 1
        if id_Old_client==0:
            self.account_ID=customers.increase_id()
        else:
            self.account_ID=id_Old_client

        self.balance = balance
        self.password=passwprd
        self.__account_type = customers.status


        db=sqlite3.connect('customers.db')
        cr = db.cursor()
        cr.execute('insert into customers(ID,f_name,l_name,date_of_bihrth,password,phone,email,gender,balance,Account_Type) '
                   'values(?,?,?,?,?,?,?,?,?,?)',(self.account_ID,f_name,self.l_name,self.date_of_birth,self.password,self.phone,self.email,self.gender,self.balance,self.account_type))
        db.commit()
        db.close()

# def _makeObject()



    @property
    def account_ID(self):
        return self.__account_ID

    @account_ID.setter
    def account_ID(self,account_ID):
        self.__account_ID = account_ID
    @property
    def account_type(self):
        return self.__account_type

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self,value):
        if value > 0:
            self.__balance = value
        else:
            raise ValueError("Balance must be positive")


    def print_client(self):
        super().print_client()
        s=(f"Balance :{self.balance}\n"
            f"Account Type: {self.account_type}")

        print(s)

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self,value):
        self.__password = value



    @staticmethod
    def add(f_name="",l_name="",date_of_birth="",passwprd="",phone="",email="",gender="",balance=0):
        adding=customers(f_name,l_name,date_of_birth,passwprd,phone,email,gender,balance)
        # print(adding.account_ID)
