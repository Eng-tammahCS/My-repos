#pragma once
#include<iostream>
#include<iomanip>
#include "clsScreen.h"
#include "clsPerson.h"
#include "clsUser.h"
#include "clsBankClient.h"
#include "C:\Users\a new life\Desktop\clsInputValidate.h"
using namespace std;
class clsTransferScreen:public clsScreen
{
	static string _ReadAccountNumber()
	{
		string AccountNumber;
		AccountNumber = clsInputValidate::ReadString();
		while (!clsBankClient::IsClientExist(AccountNumber))
		{
			cout << "\nAccount number is not found, choose another one: ";
			AccountNumber = clsInputValidate::ReadString();
		}
		return AccountNumber;
	}

	static void _PrintShortCard(clsBankClient& Client) {
		cout << "\t\t Card\n";
		cout << "\t--------------------------\n";
		cout << "\t Full name  : "<<Client.FullName()<<endl;
		cout << "\t acc.number : "<<Client.AccountNumber()<<endl;
		cout << "\t Balance    : "<<Client.AccountBalance<<endl;
		cout << "\t--------------------------\n";

	}
	static void _TransferMoney() {
		_DrawScreenHeader("Transfer screen!");
		string Account;
		cout << "Enter Account number to Transfer from?> ";
		Account = _ReadAccountNumber();
		clsBankClient FromClient = clsBankClient::Find(Account);
		cout << endl;
		_PrintShortCard(FromClient);
		
		cout << "Enter Account number to Transfer To?> ";
		Account = _ReadAccountNumber();
		clsBankClient ToClient = clsBankClient::Find(Account);
		_PrintShortCard(ToClient);
		cout << "__________________________________________\n";
		cout << "Enter transfer amount>>";
		double value = clsInputValidate::ReadDblNumber();
		char choice = 'y';
		cout << "Do you sure of this operatoins[y/n]>";
		cin >> choice;
		if (toupper(choice) == 'Y')
		{
			while (!FromClient.Transfer(value, ToClient))
			{
				cout << "sorry,Enter amount less than balance>>";
				value = clsInputValidate::ReadDblNumber();
			}
		}
		else
			cout << "Done,this transfer is cancelled!\n";


		cout << "Successfuly tha transfer!\n";
		_PrintShortCard(FromClient);
		_PrintShortCard(ToClient);
	

}
public:
	static void Transfer() {
		_TransferMoney();
	}




};

