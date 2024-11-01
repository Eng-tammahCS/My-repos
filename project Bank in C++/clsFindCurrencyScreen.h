#pragma once
#include <iostream>
#include "clsScreen.h"
#include "clsCurrency.h"
#include "clsUser.h"
#include "C:\Users\a new life\Desktop\clsInputValidate.h"
class clsFindCurrencyScreen:protected clsScreen{
	private:
		enum enTypeFind { eFindByCode = 1, eFinfByCountry };

		static short _ReadTypeFind() {
			cout << "\tFind By:\n ____________\n [1] Code\n [2] Country\n>>>[ ]\b\b";
			short choice;
			choice = clsInputValidate::ReadShortNumberBetween(1, 2, "Invalid,enter Between[1-2]>");
				return choice;
		}

		static void _PrintCurrencyData(clsCurrency Currency)
		{
			cout << "\n___________________\n";
			cout << "\nCurrency Card:";
			cout << "\n___________________";
			cout << "\nCuntray   : " << Currency.Country();
			cout << "\nCode      : " << Currency.CurrencyCode();
			cout << "\nName      : " << Currency.CurrencyName();
			cout << "\nRate(1$) =: " << Currency.Rate();
	
			cout << "\n___________________\n";
		}
		
public:
	static void ShowFindUserScreen()
	{

		_DrawScreenHeader("\t Find User Screen", "");
		string CerrncyAndCountry;
		//enTypeFind Choice = enTypeFind(_ReadTypeFind());
		 clsCurrency Currency = clsCurrency::FindByCode("");
		switch (enTypeFind(_ReadTypeFind()))
		{
		case enTypeFind::eFindByCode :
			cout << "\nEnter Currencycode>>";
			CerrncyAndCountry = clsInputValidate::ReadString();
		  Currency = clsCurrency::FindByCode(CerrncyAndCountry);
		 break;
		case enTypeFind::eFinfByCountry :
			cout<< "\nEnter Countray>>";
			CerrncyAndCountry = clsInputValidate::ReadString();
		  Currency = clsCurrency::FindByCountry(CerrncyAndCountry);
		 break;
		
		}
		
		
		if (!Currency.IsEmpty())
		{
			cout << "\nUser Found :-)\n";
		}
		else
		{
			cout << "\nUser Was not Found :-(\n";
		}
		_PrintCurrencyData(Currency);
	}
	
};

