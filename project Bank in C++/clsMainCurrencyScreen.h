#pragma once
#include<iostream>
#include "clsScreen.h"
#include "C:\Users\a new life\Desktop\clsInputValidate.h"
#include <iomanip>
#include "clsListCurrenciesScreen.h"
#include "clsFindCurrencyScreen.h"
#include "clsUpdateCurrencyScreen.h"
#include "clsClaclatorCurrencyScreen.h"
using namespace std;
class clsMainCurrencyScreen:public clsScreen
{
	enum enCurrencyoptoins{eShowCurrencies=1,eFindCurrency,eUpdateCurrency,eCurrencyCalclator,eMainMenu};
	static short _ReadCurrencyMenueOption()
	{
		cout << setw(37) << left << "" << "Choose what do you want to do? [1 to 5]? ";
		short Choice = clsInputValidate::ReadShortNumberBetween(1, 5, "Enter Number between 1 to 6? ");
		return Choice;
	}
	static void _ShowlistCurrencyScreen() {

		clsListCurrenciesScreen::ShowCurrencyListScreen();
		//cout << " this command will be here!\n";
	}
	static void _ShowFindCurrencyScreen() {

		clsFindCurrencyScreen::ShowFindUserScreen();
		//cout << " this command will be here!\n";
	}
	static void _ShowUpdateCurrencyScreen() {

		clsUpdateCurrencyScreen::ShowUpdateCurrencyScreen();
		//cout << " this command will be here!\n";
	}
	static void _ShowCurrencyCalclatorScreen() {

		clsClaclatorCurrencyScreen::CalclateCurrency();
		//cout << " this command will be here!\n";
	}
	static void _GoToBackMainMenuScreen() {
		cout << "Enter any key to back main menue screen!";
		system("pause>0");
		ShowCurrencyMenuOptions();

	}
	static void _platformCurrencyMenuOptions(enCurrencyoptoins Choice) {
		

		switch (Choice)
		{
		case clsMainCurrencyScreen::eShowCurrencies:
			system("cls");
			_ShowlistCurrencyScreen();
			_GoToBackMainMenuScreen();
			break;
		case clsMainCurrencyScreen::eFindCurrency:
			system("cls");
			_ShowFindCurrencyScreen();
			_GoToBackMainMenuScreen();
			break;
		case clsMainCurrencyScreen::eUpdateCurrency:
			system("cls");
			_ShowUpdateCurrencyScreen();
			_GoToBackMainMenuScreen();
			break;
		case clsMainCurrencyScreen::eCurrencyCalclator:
			system("cls");
			_ShowCurrencyCalclatorScreen();
			_GoToBackMainMenuScreen();
			break;
		case clsMainCurrencyScreen::eMainMenu:

			break;
		
		}

	}


public:
	static void ShowCurrencyMenuOptions() {

		system("cls");

		_DrawScreenHeader("\t Currency Exchange Main screen", "");
		cout << setw(37) << left << "" << "===========================================\n";
		cout << setw(37) << left << "" << "\t\t Currency exchange Menue\n";
		cout << setw(37) << left << "" << "===========================================\n";
		cout << setw(37) << left << "" << "\t[1] List Currency.\n";
		cout << setw(37) << left << "" << "\t[2] Find Currency.\n";
		cout << setw(37) << left << "" << "\t[3] Update  Currency.\n";
		cout << setw(37) << left << "" << "\t[4] Currency Calclator.\n";
		cout << setw(37) << left << "" << "\t[5] Main Menue.\n";
		cout << setw(37) << left << "" << "===========================================\n";
		_platformCurrencyMenuOptions(enCurrencyoptoins(_ReadCurrencyMenueOption()));
	}
};

