#pragma once
#include <iostream>
#include <iomanip>
#include "clsScreen.h"
#include "clsPerson.h"
#include "clsCurrency.h"
#include "C:\Users\a new life\Desktop\clsInputValidate.h"
using namespace std;

class clsListCurrenciesScreen:public clsScreen
{


private:
	static void PrintCurrencyRecordLine(clsCurrency CurrencyRecord)
	{
		cout << setw(8) << left << "" << "| " << setw(35) << left << CurrencyRecord.Country();
		cout << "| " << setw(6) << left << CurrencyRecord.CurrencyCode();
		cout << "| " << setw(40) << left << CurrencyRecord.CurrencyName();
		cout << "| " << setw(10) << left << CurrencyRecord.Rate();
	}
public:
	static void ShowCurrencyListScreen()
	{
		vector <clsCurrency> vCurrencyRecord = clsCurrency::GetCurrenciesList();
	/*	if (!checkaccessrights(clsuser::enpermissions::pregisterlogin))
		{
			return;
		}*/
		string Title = "\tCurrency exchange List Screen";
		string SubTitle = "\t\t(" + to_string(vCurrencyRecord.size()) + ") Record(s).";
		_DrawScreenHeader(Title, SubTitle);
		cout << setw(8) << left << "" << "\n\t_______________________________________________________";
		cout << "_________________________________________\n" << endl;
		cout << setw(8) << left << "" << "| " << left << setw(35) << "Country";
		cout << "| " << left << setw(6) << "Code";
		cout << "| " << left << setw(40) << "Name currency";
		cout << "| " << left << setw(10) << "Rate(1$)";
		cout << setw(8) << left << "" << "\n\t_______________________________________________________";
		cout << "_________________________________________\n" << endl;
		if (vCurrencyRecord.size() == 0)
			cout << "\t\t\t\tNo Currency Available In the System!";
		else
			for (clsCurrency Record : vCurrencyRecord)
			{
				PrintCurrencyRecordLine(Record);
				cout << endl;
			}
		cout << setw(8) << left << "" << "\n\t_______________________________________________________";
		cout << "_________________________________________\n" << endl;
	}
};

