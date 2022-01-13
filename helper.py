from information import *

def getUserFilingStatus():
	sentence = "--- FILING STATUS ---"
	sentence += "\n(HH) - HEAD OF HOUSEHOLD"
	sentence += "\n(MFS) - MARRIED FILING SEPARATELY"
	sentence += "\n(MFJ) - MARRIED FILING JOINTLY"
	sentence += "\n(QWW) - QUALIFIED WIDOW OR WIDOWED"
	sentence += "\n(S) - SINGLE"
	sentence += "\n\nENTER YOUR FILING STATUS: "
	while True:
		try:
			inquiry = input("{}".format(sentence))
			if inquiry.isnumeric(): raise
			elif inquiry.upper() in ["HH", "MFS", "MFJ", "QWW", "S", "QUIT", "RESTART"]:  
				return inquiry.upper()
			elif inquiry.upper() == "INFO":
				sentence = "\nENTER YOUR FILING STATUS: "
				print(informationForFilingStatus())
			else:
				raise			
		except:
			print("\nPLEASE ENTER ONE OF THESE FILING STATUSES (HH, MFS, MFJ, QWW, S)")

def getUserIncome():
	amount = -1
	while amount < 0:
		try:
			amount = input("ENTER YOUR YEARLY INCOME: ")
			if amount.isnumeric():
				if int(amount) > -1 : return int(amount)
				raise
			elif amount.upper() in ["QUIT", "RESTART"]: 
				return amount.upper()
			elif amount.upper() == "INFO":
				amount = -1
				print(informationForIncome())
			else:
				amount = -1
				raise			
		except:
			print("\nPLEASE ENTER AN AMOUNT GREATER THAN OR EQUAL TO 0 (EXCLUDE ANY $ AND COMMAS)")

def getUserAmount(account_type, contribution_deduction, max_amount):
	if max_amount == 0:
		return 0
	amount = -1
	while amount < 0:
		try:
			amount = input("\nENTER {} {} AMOUNT: ".format(account_type, contribution_deduction))
			if amount.isnumeric():
				if 0 <= int(amount) and int(amount) <= max_amount: return int(amount)
				raise
			elif amount.upper() == "MAX": # max standard deduction for federal/state
				return int(max_amount)
			elif amount.upper() in ["QUIT", "RESTART"]: 
				return amount.upper()
			elif amount.upper() == "INFO":
				amount = -1
				if account_type == "TRADITIONAL 401K":
					print(informationForTraditional401K())
				elif account_type == "ROTH 401K":	
					print(informationForRoth401K())
				elif account_type == "ROTH IRA":
					print(informationForRothIRA())
				elif account_type == "FEDERAL":
					print(informationForFederalDeductions())
				else:
					print(informationForStateDeductions())
			else:
				amount = -1
				raise			
		except:
			print("\nPLEASE ENTER AN AMOUNT BETWEEN $0 - ${:,.2f}".format(max_amount))

def printStatistics(income):
	print("\n\n\n")
	print("GROSS INCOME: ${:,.2f}".format(income.gross))
	print("ESTIMATED NET INCOME: ${:,.2f}".format(income.getNetIncome()))

	print("\n\nTAXABLE INCOME: ${:,.2f}".format(income.getTaxableIncome()))
	print(">>> FEDERAL STANDARD DEDUCTION: ${:,.2f}".format(income.getFederalDeduction()))
	print(">>> STATE STANDARD DEDUCTION: ${:,.2f}".format(income.getStateDeduction()))


	print("\n\nTOTAL TAXES PAID: ${:,.2f}".format(income.getFederalTaxes() + income.getStateTaxes() + income.getFICATax()))
	print(">>> FEDERAL INCOME TAXES: ${:,.2f}".format(income.getFederalTaxes()))
	print(">>> FICA INCOME TAXES: ${:,.2f}".format(income.getFICATax()))
	print(">>> STATE INCOME TAXES: ${:,.2f}".format(income.getStateTaxes()))


	print("\n\nTOTAL RETIREMENT CONTRIBUTIONS: ${:,.2f}".format(income.getTraditional401k() + income.getRoth401k() + income.getRothIRA()))
	print(">>> TRADITIONAL 401k CONTRIBUTION: ${:,.2f}".format(income.getTraditional401k()))
	print(">>> ROTH 401K CONTRIBUTION: ${:,.2f}".format(income.getRoth401k()))
	print(">>> ROTH IRA CONTRIBUTION: ${:,.2f}".format(income.getRothIRA()))