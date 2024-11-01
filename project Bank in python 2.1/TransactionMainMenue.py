from typing import TYPE_CHECKING
from PrintScreen import printScreen
import subprocess
from clsTransaction import Transactions
from AbcExcute import abcexcute

# if TYPE_CHECKING:

import os
class transacion_mainMenue(printScreen,abcexcute):
    isBack=True
    options=[
        'Check balance',
        'Withdraw balance',
        'Deposit balance',
        'Turn between client',
        'Back to main menu'
    ]
    @staticmethod
    def _UserINput():
        inp =0
        istrue=False
        while not istrue:
            inp=int(input("Enter the item that you want> "))
            if  not len(transacion_mainMenue.options)>=inp > 0:
                print(f"Enter number between {1} and {len(transacion_mainMenue.options)}")
            istrue = len(transacion_mainMenue.options)>=inp > 0
        return (inp)





    @staticmethod
    def printMainMenue():
        transacion_mainMenue.PrintScreenMenue("Transaction Main Menue",)


    @staticmethod
    def __checkBalance():
        Transactions.check_Balance()
        # print("here Wll be the all clients")


    @staticmethod
    def __withdrawBalance():
        Transactions.withdrow()

    @staticmethod
    def __depositBalance():
        Transactions.deposite()
    @staticmethod
    def __turnBetweenClients():
        Transactions.TurnBetweenClients()
        # print("here Wll be the edit client")

    @staticmethod
    def GotoMainMenu():
        from MainMenue import mainMenue

        print("Enter the number you want to come back")
        os.system('cls')
        # mainMenue.PerformMainMenue()
    @staticmethod
    def perform():

        transacion_mainMenue.printMainMenue()
        transacion_mainMenue._MakeListContent(transacion_mainMenue.options)
        printScreen._footer()
        inputs=transacion_mainMenue._UserINput()
        if inputs==1:
            subprocess.call('cls', shell=True)

            printScreen.PrintScreenMenue("Checking Balance")
            transacion_mainMenue.__checkBalance()

        elif inputs==2:
            subprocess.call('cls', shell=True)

            printScreen.PrintScreenMenue("Withdraw Memue")

            transacion_mainMenue.__withdrawBalance()

        elif inputs==3:
            subprocess.call('cls', shell=True)

            printScreen.PrintScreenMenue("Deposite Menue ")
            transacion_mainMenue.__depositBalance()

        elif inputs==4:
            subprocess.call('cls', shell=True)

            printScreen.PrintScreenMenue("Turn Between clients Menue ")

            transacion_mainMenue.__turnBetweenClients()

        elif inputs==5:
            # printScreen.PrintScreenMenue("Go to Main Menue ")
            transacion_mainMenue.isBack=False
            # transacion_mainMenue.GotoMainMenu()









    @staticmethod
    def excute(e=""):

        while transacion_mainMenue.isBack:
            # os.system("cls")
            subprocess.call('cls', shell=True)
            transacion_mainMenue.perform()
            if transacion_mainMenue.isBack:
                subprocess.call('pause', shell=True)

        transacion_mainMenue.isBack=True




# transacion_mainMenue.perform_transaction()
