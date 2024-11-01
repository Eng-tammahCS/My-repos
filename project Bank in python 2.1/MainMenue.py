import os

import subprocess
import Remove
from PrintScreen import printScreen
from Show_clients import showClients
from Add_Customer import add_Customer
from Update_client import updateClient
from Remove import remove
from FindCLients import find
from AbcExcute import abcexcute

from typing import TYPE_CHECKING
# if TYPE_CHECKING:


class mainMenue(printScreen,abcexcute):

    lists=[
        'Show clients',
        'Add client',
        'remove client',
        'Edit client',
        'Find client',
        'Transactions',
        'Exit'
    ]
    @staticmethod
    def _UserINput():
        inp =0
        istrue=False
        while not istrue:
            inp=int(input("Enter the item that you want> "))
            if  not len(mainMenue.lists)>=inp > 0:
                print(f"Enter number between {1} and {len(mainMenue.lists)}")
            istrue = len(mainMenue.lists)>=inp > 0
        return (inp)





    @staticmethod
    def printMainMenue():
        mainMenue.PrintScreenMenue("Main Menue",)


    @staticmethod
    def __showAllClient():
        showClients.showAllClients_withOrder()

        # print("here Wll be the all clients")


    @staticmethod
    def __addClient():
        add_Customer.Add_Customer()

    @staticmethod
    def __removeClient():
        remove.remove()
        # print("here Wll be the remove client")

    @staticmethod
    def __editClient():
        updateClient._update_client()

        print("here Wll be the edit client")

    @staticmethod
    def __findClient():
        find._printClient()
        # print("here Wll be the find client")

    @staticmethod
    def __transactions():
        from TransactionMainMenue import transacion_mainMenue
        transacion_mainMenue.excute()
    @staticmethod
    def perform(inputs):

        mainMenue.printMainMenue()
        mainMenue._MakeListContent(mainMenue.lists)
        printScreen._footer()


        # inputs=mainMenue._UserINput()
        if inputs==1:
            mainMenue.__showAllClient()
        elif inputs==2:
            mainMenue.__addClient()

        elif inputs==3:
            mainMenue.__removeClient()

        elif inputs==4:
            mainMenue.__editClient()

        elif inputs==5:
            mainMenue.__findClient()

        elif inputs==6:
            mainMenue.__transactions()
        elif inputs==7:
            subprocess.call("exit", shell=True)





    @staticmethod
    def GotoMainMenu():
        # os.system("pause")
        # print("Enter the number you want to come back")
        # os.system('cls')
        # mainMenue.PerformMainMenue()
        pass


    @staticmethod
    def excute(inputs=""):

        # while True:
            os.system("cls")
            subprocess.call('cls', shell=True)
            mainMenue.perform(inputs)
            subprocess.call('pause', shell=True)







