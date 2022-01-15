from income import NetIncome
from helper import *
import time


def main():
	loop = True
	while loop:
		print("\n\nWELCOME TO THE TAX PREPARATION CALCULATOR!\n")
		print("---YOU MAY ENTER ANY OF THESE KEYWORDS AT ANY TIME---")
		print("INFO - TYPE THIS TO GET MORE INFORMATION ABOUT HOW TO ANSWER THE QUESTION")
		print("RESTART - TYPE THIS TO RESTART THE PROGRAM")
		print("QUIT - TYPE THIS TO QUIT THE PROGRAM\n\n")
		status = getUserFilingStatus()
		if status == "QUIT" : loop = False
		if status in ["QUIT", "RESTART"]: continue

		inquiry = getUserIncome()
		if inquiry == "QUIT" : loop = False
		if inquiry in ["QUIT", "RESTART"]: continue
		income = NetIncome(status, inquiry)


		inquiry = getUserAmount("TRADITIONAL 401K", "CONTRIBUTION", income.getTraditional401kMax())
		if inquiry == "QUIT" : loop = False
		if inquiry in ["QUIT", "RESTART"]: continue
		income.setTraditional401k(inquiry)



		income.setFICATax()
		income.setTaxableIncome()

		inquiry = getUserAmount("FEDERAL", "DEDUCTION", income.getFederalDeductionMax())
		if inquiry == "QUIT" : loop = False
		if inquiry in ["QUIT", "RESTART"]: continue
		income.setFederalDeduction(inquiry)



		inquiry = getUserAmount("STATE", "DEDUCTION", income.getStateDeductionMax())
		if inquiry == "QUIT" : loop = False
		if inquiry in ["QUIT", "RESTART"]: continue
		income.setStateDeduction(inquiry)


		income.setFederalTaxes()
		income.setStateTaxes()
		income.setAfterTaxIncome()



		inquiry = getUserAmount("ROTH 401K", "CONTRIBUTION", income.getRoth401kMax())
		if inquiry == "QUIT" : loop = False
		if inquiry in ["QUIT", "RESTART"]: continue
		income.setRoth401k(inquiry)



		inquiry = getUserAmount("ROTH IRA", "CONTRIBUTION", income.getRothIRAMax())
		if inquiry == "QUIT" : loop = False
		if inquiry in ["QUIT", "RESTART"]: continue
		income.setRothIRA(inquiry)



		income.setNetIncome()
		printStatistics(income)
		input("\nPRESS ENTER TO CONTINUE")
		# time.sleep(60)

if __name__ == '__main__':
	main()