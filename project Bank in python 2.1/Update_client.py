from PrintScreen  import printScreen
from Customers import  customers
from Add_Customer import  add_Customer
import sqlite3

class updateClient:
    db=sqlite3.connect("customers.db")
    cursor=db.cursor()
    # client=cursor.execute("SELECT * FROM customers where ID like 500")
    @staticmethod
    def _get_and_checkID():
        isFound = False
        while not isFound:
            ID=int(input("Enter ID that you want to Update:>"))
            client=updateClient.cursor.execute("SELECT * FROM customers where ID like "+str(ID)).fetchone()
            # print(client)
            if client:
                updateClient.db.commit()
                updateClient.db.close()
                isFound=True
                return client
            print("ID not found")


    @staticmethod
    def _update_client( ):
        db = sqlite3.connect("customers.db")
        cursor = db.cursor()
        old_client=updateClient._get_and_checkID()
        ID=old_client[0]
        new_client=add_Customer._add_customer("update client")
        cursor.execute("UPDATE customers SET "
                                    "f_name=?, l_name=?, date_of_bihrth=?, password=?, "
                                    "phone=?, email=?, gender=?  WHERE ID =?",(*new_client,ID))
        # print(*new_client)
        # print(*old_client)
        db.commit()
        db.close()
        print("Client Updated Successfully")

# updateClient._update_client()









