#pragma once
#include <iostream>
#include <iomanip>
#include "C:\Users\a new life\Desktop\clsInputValidate.h"
#include "clsScreen.h"
#include "clsClientListScreen.h"
#include "clsAddNewClientScreen.h"
#include "clsDeleteClientScreen.h"
#include "clsUpdateClientScreen.h"
#include "clsFindClientScreen.h"
#include "clsTransactionScreen.h"
#include "clsManageUsersScreen.h"
#include "clsLoginRegisterScreen.h"
#include "clsMainCurrencyScreen.h"
#include "Global.h"


using namespace std;
class clsMainScreen :protected clsScreen
{
private:
	enum enMainMenueOptions {
		eListClients = 1, eAddNewClient = 2, eDeleteClient = 3,
		eUpdateClient = 4, eFindClient = 5, eShowTransactionsMenue = 6,
		eManageUsers = 7 ,enShowLogins,enShowCurrencyMenu, eExit 
	};
	static short _ReadMainMenueOption()
	{
		cout << setw(37) << left << "" << "Choose what do you want to do? [1 to 10]? ";
		short Choice = clsInputValidate::ReadShortNumberBetween(1, 10, "Enter Number between 1 to 8? ");
		return Choice;
	}
	static void _GoBackToMainMenue()
	{
		cout << setw(37) << left << "" << "\n\tPress any key to go back to Main Menue...\n";
		system("pause>0");
		ShowMainMenue();
	}
	static void _ShowAllClientsScreen()
	{
		//cout << "\nClient List Screen Will be here...\n";
		clsClientListScreen::ShowClientsList();

	}
	static void _ShowAddNewClientsScreen()
	{
		clsAddNewClientScreen::ShowAddNewClientScreen();
		//cout << "\nAdd New Client Screen Will be here...\n";
	}
	static void _ShowDeleteClientScreen()
	{

		clsDeleteClientScreen::ShowDeleteClientScreen();

		//cout << "\nDelete Client Screen Will be here...\n";

	}
	static void _ShowUpdateClientScreen()
	{
		clsUpdateClientScreen::ShowUpdateClientScreen();
		//cout << "\nUpdate Client Screen Will be here...\n";
	}
	static void _ShowFindClientScreen()
	{
		clsFindClientScreen::ShowFindClientScreen;
		//cout << "\nFind Client Screen Will be here...\n";
	}
	static void _ShowTransactionsMenue()
	{
		clsTransactionsScreen::ShowTransactionsMenue();
//cout << "\nTransactions Menue Will be here...\n";
	}
	static void _ShowManageUsersMenue()
	{
		clsManageUsersScreen::ShowManageUsersMenue();
		//cout << "\nUsers Menue Will be here...\n";
	}
	static void _ShowLogins()
	{
		clsLoginRegisterScreen::ShowLoginRegisterScreen();
		//cout << "\nUsers Menue Will be here...\n";
	}
	static void _ShowCurrencyMenu()
	{
		clsMainCurrencyScreen::ShowCurrencyMenuOptions();
		//cout << "\nUsers Menue Will be here...\n";
	}

	static void _LogOut()
	{
		CurrentUser = clsUser::Find("", "");
	}
	static void _PerfromMainMenueOption(enMainMenueOptions MainMenueOption)
	{
		switch (MainMenueOption)
		{
		case enMainMenueOptions::eListClients:
		{
			system("cls");
			_ShowAllClientsScreen();
			_GoBackToMainMenue();
			break;
		}
		case enMainMenueOptions::eAddNewClient:
			system("cls");
			_ShowAddNewClientsScreen();
			_GoBackToMainMenue();
			break;
		case enMainMenueOptions::eDeleteClient:
			system("cls");
			_ShowDeleteClientScreen();
			_GoBackToMainMenue();
			break;
		case enMainMenueOptions::eUpdateClient:
			system("cls");
			_ShowUpdateClientScreen();
			_GoBackToMainMenue();
			break;
		case enMainMenueOptions::eFindClient:
			system("cls");
			_ShowFindClientScreen();
			_GoBackToMainMenue();
			break;
		case enMainMenueOptions::eShowTransactionsMenue:
			system("cls");
			_ShowTransactionsMenue();
			_GoBackToMainMenue();
			break;
		case enMainMenueOptions::eManageUsers:
			system("cls");
			_ShowManageUsersMenue();
			_GoBackToMainMenue();
			break;
		case enMainMenueOptions::enShowLogins:
			system("cls");
			_ShowLogins();
			_GoBackToMainMenue();
			break;
		case enMainMenueOptions::enShowCurrencyMenu:
			system("cls");
			_ShowCurrencyMenu();
			_GoBackToMainMenue();
			break;
		case enMainMenueOptions::eExit:
			system("cls");
			_LogOut();
			//Login();
			break;
		}
	}
public:
	static void ShowMainMenue()
	{
		system("cls");
		_DrawScreenHeader("\t\tMain Screen", "");

		cout << setw(37) << left << "" << "===========================================\n";
		cout << setw(37) << left << "" << "\t\t\tMain Menue\n";
		cout << setw(37) << left << "" << "===========================================\n";
		cout << setw(37) << left << "" << "\t[1] Show Client List.\n";
		cout << setw(37) << left << "" << "\t[2] Add New Client.\n";
		cout << setw(37) << left << "" << "\t[3] Delete Client.\n";
		cout << setw(37) << left << "" << "\t[4] Update Client Info.\n";
		cout << setw(37) << left << "" << "\t[5] Find Client.\n";
		cout << setw(37) << left << "" << "\t[6] Transactions.\n";
		cout << setw(37) << left << "" << "\t[7] Manage Users.\n";
		cout << setw(37) << left << "" << "\t[8] Show login register Users.\n";
		cout << setw(37) << left << "" << "\t[9] Currency exchange.\n";
		cout << setw(37) << left << "" << "\t[10] Logout.\n";
		cout << setw(37) << left << "" << "===========================================\n";
		_PerfromMainMenueOption((enMainMenueOptions)_ReadMainMenueOption());
	}
};