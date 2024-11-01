from PrintScreen import printScreen
from Customers import customers
import  sqlite3
class showClients:
    db = sqlite3.connect('customers.db')
    cursor = db.cursor()
    @staticmethod
    def __returnAllClients():
        showClients.cursor.execute("SELECT * FROM customers order by id")
        return showClients.cursor.fetchall()


    @staticmethod
    def __print_one_client_with_format(client):
        isOne=True
        for dara in client:
            if isOne:
                print(f""
                      f"| {str(dara):>6}",end="")
                isOne=False
            else:
                print(f"| {str(dara):>10}",end="")
        else:
            print("\n")




    @staticmethod
    def __Print_heeder():
        print("*"*120)
        items_header=[' ID',' F Name',
                      ' L Name',
                      ' Birthday',
                      ' passwprd',
                      ' phone',
                      ' Email',
                      ' Gender',' Balance','Account Type']
        isOne=True
        for item in items_header:
            if isOne:
                print(f"| {item:>6}",end="")

                isOne = False
            else:
                print(f"| {item:>10}",end="")
        print("\n","*"*120)
    @staticmethod
    def showAllClients_withOrder():
        clients = showClients.__returnAllClients()
        printScreen.PrintScreenMenue("Show Clients",f"clients: ({len(clients)})")
        showClients.__Print_heeder()

        for client in clients:
            showClients.__print_one_client_with_format(client)
        else:
            print("\n")
            printScreen._footer()



