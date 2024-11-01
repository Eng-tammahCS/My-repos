from MainMenue import mainMenue
import subprocess



def UserINput():
    inp = 0
    istrue = False
    while not istrue:
        inp = int(input("Enter the item that you want> "))
        if not len(mainMenue.lists) >= inp > 0:
            print(f"Enter number between {1} and {len(mainMenue.lists)}")
        istrue = len(mainMenue.lists) >= inp > 0
    return (inp)


def Clearconsole():
    subprocess.call("cls", shell=True)
while True:

    Clearconsole()
    mainMenue.printMainMenue()
    mainMenue._MakeListContent(mainMenue.lists)
    mainMenue.excute(UserINput())

