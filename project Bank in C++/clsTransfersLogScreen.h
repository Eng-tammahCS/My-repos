#pragma once
#include <iostream>
#include "clsScreen.h"
#include <iomanip>
#include <fstream>
#include "clsUser.h"
#include "clsBankClient.h"
class clsTransfersLogScreen :protected clsScreen
{
private:
	static void PrintTransferLogRegisterRecordLine(clsBankClient::stTransferLog &TransferListerRecord)
	{
		cout << setw(8) << left << "" << "| " << setw(20) << left << TransferListerRecord.Time;
		cout << "| " << setw(8) << left << TransferListerRecord.AcountFrom;
		cout << "| " << setw(8) << left << TransferListerRecord.AccountTo;
		cout << "| " << setw(10) << left << TransferListerRecord.AmountTransfer;
		cout << "| " << setw(15) << left << TransferListerRecord.BalanceAfter1;
		cout << "| " << setw(15) << left << TransferListerRecord.BalanceAfter2;
		cout << "| " << setw(20) << left << TransferListerRecord.UserNmae;
	}
public:
	static void ShowLoginRegisterScreen()
	{
		vector <clsBankClient::stTransferLog> TransferRegisterRecord = clsBankClient::GetTransfersLogRegisterList();
	
		string Title = "\tTransfer log Register List Screen";
		string SubTitle = "\t\t(" + to_string(TransferRegisterRecord.size()) + ") Record(s).";
		_DrawScreenHeader(Title, SubTitle);
		cout << setw(8) << left << "" << "\n\t_______________________________________________________";
		cout << "_____________________________________________\n" << endl;
		cout << setw(8) << left << "" << "| " << left << setw(20) << "Date/Time";
		cout << "| " << left << setw(8) << "s.Acount";
		cout << "| " << left << setw(8) << "d.Account";
		cout << "| " << left << setw(10) << "Amount";
		cout << "| " << left << setw(15) << "s.Balance after";
		cout << "| " << left << setw(15) << "d.Balance after";
		cout << "| " << left << setw(20) << "User Name";

		cout << setw(8) << left << "" << "\n\t_______________________________________________________";
		cout << "_____________________________________________\n" << endl;
		if (TransferRegisterRecord.size() == 0)
			cout << "\t\t\t\tNo Logins Available In the System!";
		else
			for (clsBankClient::stTransferLog Record : TransferRegisterRecord)
			{
				PrintTransferLogRegisterRecordLine(Record);
				cout << endl;
			}
		cout << setw(8) << left << "" << "\n\t___________________________________________________________";
		cout << "_________________________________________\n" << endl;
	}
};