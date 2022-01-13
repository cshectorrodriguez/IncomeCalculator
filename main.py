from income import NetIncome
from helper import *
import time


def main():
	loop = True
	while loop:
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
		time.sleep(60)

if __name__ == '__main__':
	main()