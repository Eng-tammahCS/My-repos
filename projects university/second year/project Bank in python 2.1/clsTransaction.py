from PrintScreen import printScreen
import Customers
import sqlite3
class Transactions(printScreen):

    @staticmethod
    def check_Balance():
        account=int(input("Enter account number: "))
        db = sqlite3.connect('customers.db')
        cr = db.cursor()
        try:

            custom =cr.execute("SELECT * FROM customers WHERE ID = ?", (account,))
            datacustomer=custom.fetchone()
            db.commit()
            db.close()


            print(f"\n Your Balance IS {datacustomer[8]}$")

        except:
            print("Invalid Account Number")



    # #cr.execute("select * from customers")
    @staticmethod
    def Is_Found(ID):
            se=Transactions.search(ID)
            if se !="Notfound" and len(se)>0:
                return True
            else:
                return False

    @staticmethod
    def search(ID):

        try:
            db = sqlite3.connect('customers.db')
            cr = db.cursor()
            custom =cr.execute("SELECT * FROM customers WHERE ID = ?", (ID,))
            datacustomer=custom.fetchone()
            db.close()
            return list(datacustomer)
        except:
            return "Notfound"


    @staticmethod
    def TurnBetweenClients():

           S_acount_number=int(input("Enter a sender's acount  number: "))

           while not Transactions.Is_Found(S_acount_number):# find acount sender number:
               S_acount_number =int( input("Sorry!,not found acount number"))

           Password=input("Enter your password: ")

           Sepass1=Transactions.search(ID=S_acount_number)

           while (Password != Sepass1[4]):
                print("Passwords do not match <> ")
                Password=input("Enter your password: ")




           R_acount_number=int(input("Enter a receiver's acount  number : "))
           while not Transactions.Is_Found(R_acount_number):# find acount receiver number:
               R_acount_number =int( input("Sorry!,not found acount number :"))

           Sepass2=Transactions.search(ID=R_acount_number)

           print(f"\n Your Amount IS {Sepass1[8]}$")
           Amount = int(input("Enter Amount : "))


           istrue=True
           while  istrue:
                istrue = (Amount > Sepass1[8] or (Sepass1[8] == 0 or Amount <= 0))
                if ( istrue) : # customers.balance:
                    print("Sorry!,amount greater than or equal your balance <> ")
                    Amount = int(input("Enter Amount That you want to transfer: "))



           y=input("Are you Sure To do this Transaction? (y/n) ")
           if y.upper()=="Y":
                newBalance1=Transactions.withdrowBalance(Sepass1[8],Amount)
                newBalance2=Transactions.depositeBalance(Sepass2[8],Amount)

                if Transactions.IsUpdateBalance(Sepass1[0],newBalance1) and Transactions.IsUpdateBalance(Sepass2[0],newBalance2):
                        print("Your Balance has been transferred ")
                        print(f"Your new Balance is {newBalance1}")
                        print(f"Your friend Balance is {newBalance2}")

           else:
              print("Your Balance has been NOT transferred")


    # @staticmethod
    # def Receive_amount():
    #     R_acount_number = input("Enter a receiver's acount  number: ")
    #     while R_acount_number !=  # find acount receiver number:
    #         R_acount_number = input("Sorry!,not found acount number")
    #     Amount = int(input("Enter Amount:"))
    #     #balance+=amount

    @staticmethod
    def deposite():
        Acount_number=int(input("Enter a Account  Number: "))

        while not  Transactions.Is_Found(Acount_number):
            Acount_number = input("Sorry!,not found acount number")


        Password=input("Enter your password: ")

        Sepass=Transactions.search(ID=Acount_number)

        while (Password != Sepass[4]):
            print("Passwords do not match <> ")
            Password=input("Enter your password: ")

        Amount = int(input("Enter Amount That you want to deposite: "))

        # istrue = False
        # while not istrue:
        #     if Amount > Sepass[8] or (Sepass[8]==0 or Amount <= 0) : # customers.balance:
        #         print("Sorry!,amount greater than or equal your balance <> ")
        #         Amount = int(input("Enter Amount That you want to deposite: "))


        y=input("Are you Sure To do this Transaction? (y/n) ")
        if y.upper()=="Y":
            newBalance=Transactions.depositeBalance(Sepass[8],Amount)
            if Transactions.IsUpdateBalance(Sepass[0],newBalance):
                print("Your Balance has been transferred ")
                print(f"Your new Balance is {newBalance}")

        else:
            print("Your Balance has been NOT transferred")

    @staticmethod
    def withdrow():
        Acount_number=int(input("Enter a Account  Number: "))

        while not  Transactions.Is_Found(Acount_number):
            Acount_number = input("Sorry!,not found acount number")

        Password=input("Enter your password: ")

        Sepass=Transactions.search(ID=Acount_number)

        while (Password != Sepass[4]):
            print("Passwords do not match <> ")
            Password=input("Enter your password: ")


        Amount = int(input(f"Your Balance is -> [{Sepass[8]}] \nEnter  Amount That you want to transfer : "))
        # istrue = False
        # while not istrue:
        #     if Amount > Sepass[8] or (Sepass[8]==0 or Amount <= 0) : # customers.balance:
        #         print("Sorry!,amount greater than or equal your balance <> ")
        #         Amount = int(input("Enter Amount That you want to transfer: "))
        #
        #     istrue=True

        istrue = True
        while istrue:
            istrue = (Amount > Sepass[8] or (Sepass[8]==0 or Amount <= 0))
            if (istrue):  # customers.balance:
                print("Sorry!,amount greater than or equal your balance <> ")
                Amount = int(input("Enter Amount That you want to transfer: "))

        y=input("Are you Sure To do this Transaction? (y/n) ")
        if y.upper()=="Y":
            newBalance=Transactions.withdrowBalance(Sepass[8],Amount)
            if Transactions.IsUpdateBalance(Sepass[0],newBalance):
                print("Your Balance has been transferred ")
                print(f"Your new Balance is {newBalance}")

        else:
            print("Your Balance has been NOT transferred")

    @staticmethod
    def withdrowBalance(Balance,Amount):
        return Balance-Amount
    @staticmethod
    def depositeBalance(Balance,Amount):
        return Balance+Amount


            # istrue = Tr/ue
    @staticmethod
    def IsUpdateBalance(ID,NewBalance):
        try:
            db = sqlite3.connect('customers.db')
            cr = db.cursor()
            cr.execute("update customers set balance=? WHERE ID =?", (NewBalance,ID))
            # datacustomer=custom.fetchone()

            db.commit()
            db.close()

            return True

        except:
            print("Not Upated ")



