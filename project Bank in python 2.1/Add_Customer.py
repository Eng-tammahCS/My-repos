from Customers import customers
from PrintScreen import printScreen
import sqlite3

class add_Customer(printScreen):

    @staticmethod
    def _add_customer(prompt=""):

        add_Customer.PrintScreenMenue(prompt)
        print()
        print()
        f_name = input("Enter First Name: ")
        l_name = input("Enter Last Name: ")
        date_of_birth =input("Enter Date of Birth: ")
        password =input("Enter Password: ")
        phone =  input("Enter Phone Number: ")
        email =input("Enter Email Address: ")
        gender = input("Enter Gender: ")
        return f_name, l_name, date_of_birth, password, phone, email, gender
    @staticmethod
    def Add_Customer():
        C=customers.add(*add_Customer._add_customer("Add Customer"),balance=0)
        print("Added Successfully ")



    # def PrintCustomer(self):
    #     db=sqlite3.connect('customers.db')
    #     cr = db.cursor()
    #     # a=cr.execute("SELECT * FROM customers where ID=?",(self.customer[0]))
    #     row=cr.fetchall()
    #     if row:
    #         for row in row:
    #             print(row)
    #




