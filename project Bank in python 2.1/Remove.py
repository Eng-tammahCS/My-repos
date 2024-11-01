from PrintScreen import printScreen
from clsTransaction import Transactions
import sqlite3
class remove(printScreen):

    @staticmethod
    def remove():

        istrue=False
        remo=int(input("Enter the number you want to remove: "))
        while not Transactions.Is_Found(remo):
                remo=int(input("Enter the number you want to remove: "))
            # istrue=True
        y=input("Are you Sure To do this Transaction? (y/n) ")
        if y.upper()=="Y":
            db = sqlite3.connect('customers.db')
            cr = db.cursor()
            cr.execute("delete from customers WHERE ID =?", (remo,))
            # datacustomer=custom.fetchone()
            db.commit()
            db.close()
            print("Successfully removed")
        else:
            print("Not Removed ")

