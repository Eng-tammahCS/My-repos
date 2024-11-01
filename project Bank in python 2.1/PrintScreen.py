# from TransactionMainMenue import
class printScreen:

    # prompt='frf'
    @staticmethod
    def __header(prompt,subprompt):
        print(" "*40,"@"*50)
        print(f"{prompt:>70}\n{subprompt:>58}")
        print(" "*40,"@"*50)


    @staticmethod
    def PrintScreenMenue(prompt,subprompt=""):
        printScreen.__header(prompt,subprompt)
        # print(printScreen.MakeListContent(content))
    @staticmethod
    def _footer():
        print("@"*40)

    @staticmethod
    def _MakeListContent(lis):
        Lines=""
        for i,li in enumerate(lis):
            Lines+=(f"{i+1:>10}]- {li}\n")

        print( Lines)


    @staticmethod
    def printMainMenue():

        printScreen.PrintScreenMenue("WEllCOME")
        printScreen._footer()
