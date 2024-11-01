#pragma once

#include <iostream>
#include "clsScreen.h"
#include "clsCurrency.h"
#include "clsUser.h"
#include "C:\Users\a new life\Desktop\clsInputValidate.h"
	class clsUpdateCurrencyScreen :protected clsScreen
	{
	private:
		static void _ReadCurrencyRate(clsCurrency& Currency)
		{
			cout << "\nEnter New Rate: ";
			float Rate= clsInputValidate::ReadFloatNumber();
				
			Currency.UpdateRate(Rate);
			
		}
		static void _PrintCurrencyData(clsCurrency &Currency)
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
		static void ShowUpdateCurrencyScreen()
		{
			_DrawScreenHeader("\tUpdate Currency Screen", "");
			string Currencycode = "";
			cout << "\nPlease Enter CurrencyCode: ";
			Currencycode = clsInputValidate::ReadString();
			while (!clsCurrency::IsCurrencyExist(Currencycode))
			{
				cout << "\nThis currency is not found, choose another one: ";
				Currencycode = clsInputValidate::ReadString();
			}
			clsCurrency Currency = clsCurrency::FindByCode(Currencycode);
			_PrintCurrencyData( Currency);
			cout << "\nAre you sure you want to update this Currency y/n? ";
			char Answer = 'n';
			cin >> Answer;
			if (Answer == 'y' || Answer == 'Y')
			{
				cout << "\n\nUpdate Currency Rate:";
				cout << "\n____________________\n";
				_ReadCurrencyRate(Currency);

				cout << "\Currecy Updated Successfully :-)\n";
				_PrintCurrencyData(Currency);
			}else 
				cout << "Updatein is canclled!\n";
		}
};

