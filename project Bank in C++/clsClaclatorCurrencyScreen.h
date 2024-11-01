#pragma once
#include <iostream>
#include "clsScreen.h"
#include "clsBankClient.h"
#include "clsCurrency.h"
#include "C:\Users\a new life\Desktop\clsInputValidate.h"
using namespace std;
class clsClaclatorCurrencyScreen:protected clsScreen
{

	static float _ExchangeToDollar(clsCurrency & FromCurrency,float Amount ) {
		return Amount / FromCurrency.Rate();
	}
	static float _ExchangeFromDollar(clsCurrency & ToCurrency,float Amount ) {
		return Amount *ToCurrency.Rate();
	}
	static void _CalclateCurrency(clsCurrency& From, clsCurrency& To, float Amount) {
		cout << "convert from : \n\n";
		float Dollars = 0;
		_PrintCurrencyData(From);
			cout << endl;
			if (From.CurrencyCode()!="USD")
			{
				if (To.CurrencyCode() != "USD")
				{
					Dollars = _ExchangeToDollar(From,Amount);
					cout << " " << Amount << " " << From.CurrencyCode() + " = " << Dollars << " USD"<<endl << endl;
					cout << "Converting From USD To:\n\nTo:\n";
					_PrintCurrencyData(To);
					cout << endl;
					Dollars =_ExchangeFromDollar(To,Dollars );
					cout << " " << Amount << " " << From.CurrencyCode() + " = " << Dollars<< To.CurrencyCode() << endl << endl;

				}
				else {

					Dollars =_ExchangeToDollar(From,Amount );
					cout << " " << Amount << " " << From.CurrencyCode() + " = " << Dollars<< To.CurrencyCode() << endl << endl;

				}
			}
			else {
					Dollars =_ExchangeFromDollar(To,Amount );
					cout << " " << Amount << " " << From.CurrencyCode() + " = " << Dollars<< To.CurrencyCode() << endl << endl;

			}

	}

	static string _ReadCurrencyCode()
	{
		string Currencycode;
		Currencycode = clsInputValidate::ReadString();
		while (!clsCurrency::IsCurrencyExist(Currencycode))
		{
			cout << "\nThis currency is not found, choose another one: ";
			Currencycode = clsInputValidate::ReadString();
		}
		return Currencycode;
	}

	static void _PrintCurrencyData(clsCurrency& Currency)
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
	static void CalclateCurrency() {
		do
		{
			system("cls");
			_DrawScreenHeader("Claclate currency creen!");
			string Currencycode;
			float Amount = 0;
			cout << "Enter currency1 code from?> ";
			Currencycode = _ReadCurrencyCode();
			clsCurrency FromClient = clsCurrency::FindByCode(Currencycode);
			cout << "Enter currency2 code To?> ";

			Currencycode = _ReadCurrencyCode();
			clsCurrency ToCurrency = clsCurrency::FindByCode(Currencycode);
			cout << endl;
			cout << "Enter thee amount to exchange>>";
			Amount = clsInputValidate::ReadFloatNumber();
			_CalclateCurrency(FromClient, ToCurrency, Amount);
			cout << "Do you want to perform calclatoins[y/n]>[ ]\b\b";
		} while (tolower(clsInputValidate::ReadChar()) == 'y');
	}
	

};

