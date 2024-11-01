#include <iostream>
#include <iomanip>
#include "clsPerson.h"
#include "clsBankClient.h"
#include "clsMainScreen.h"
#include "clsLoginScreen.h"


int main()

{
    while (true)
    {
        if (!clsLoginScreen::Login())
        {
            break;
        }

    }

    system("pause>0");
    return 0;
}