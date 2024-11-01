#pragma once
#include <iostream>
#include "clsScreen.h"
#include "clsUser.h"
#include <iomanip>
#include "clsMainScreen.h"
#include "Global.h"

class clsLoginScreen:protected clsScreen
{
private:
	static bool _Login() {
		bool LoadFaild = false;
			string UserName, Password;
			short FaildLoginCount = 0;
		do
		{

	   	system("cls");
		_DrawScreenHeader("\t Login Screen", "");
			if (LoadFaild)
			{
				FaildLoginCount++;
				cout << "Invalid,UserName/Password>\n";
				cout << "you have " << 3-FaildLoginCount << " Trails to login!\n\n";
				
			}
			if (FaildLoginCount==3)
			{
				cout << "\nsorry,system are locked after 3 trails,try later:";
				return false;
			}
			cout << "Enter UserName>>";
			cin >> UserName;
			cout << "Enter Password>";
			cin >> Password;
			CurrentUser = clsUser::Find(UserName, Password);

			LoadFaild = CurrentUser.IsEmpty();
		} while (LoadFaild);
		clsUser::SaveLoginToFile(CurrentUser);
		clsMainScreen::ShowMainMenue();
		return true;
	}
public:
	static bool Login() {
		return _Login();
	}
};

