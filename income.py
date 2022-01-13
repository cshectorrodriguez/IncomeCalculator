class NetIncome:
	def __init__(self, status, income):
		self.filing_status = status
		self.gross = income
		self.federal_deduction = 12550
		self.state_deduction = 4803

		self.traditional_401k = 0
		self.taxable_income = 0
		self.fedaral_taxes = 0
		self.state_taxes = 0
		self.fica_taxes = 0
		self.after_tax_income = 0

		self.roth_401k = 0
		self.roth_IRA = 0
		self.net_income = 0

		self.max_401k = 20500

	def getFilingStatus(self):
		return self.filing_status

	def getGross(self):
		return self.gross

	#fix function...you dont pay FICA above a certain amount
	def setFICATax(self):
		self.fica_taxes = self.gross * 0.0765

	def getFICATax(self):
		return self.fica_taxes

	def setTaxableIncome(self):
		self.taxable_income = self.gross - self.traditional_401k

	def getTaxableIncome(self):
		return self.taxable_income

	def setFederalDeduction(self, amount):
		self.federal_deduction = amount

	def getFederalDeduction(self):
		return self.federal_deduction

	def setStateDeduction(self, amount):
		self.state_deduction = amount

	def getStateDeduction(self):
		return self.state_deduction

	def setFederalTaxes(self):
		self.fedaral_taxes = self.federalBracket(self.taxable_income - self.federal_deduction)

	def getFederalTaxes(self):
		return self.fedaral_taxes

	def setStateTaxes(self):
		self.state_taxes = self.stateBracket(self.taxable_income - self.state_deduction)

	def getStateTaxes(self):
		return self.state_taxes

	def setAfterTaxIncome(self):
		self.after_tax_income = self.taxable_income - self.fedaral_taxes - self.state_taxes - self.fica_taxes

	def getAfterTaxIncome(self):
		return self.after_tax_income

	def setTraditional401k(self, amount):
		self.traditional_401k = amount

	def getTraditional401k(self):
		return self.traditional_401k

	def setRoth401k(self, amount):
		self.roth_401k = amount

	def getRoth401k(self):
		return self.roth_401k

	def setRothIRA(self, amount):
		self.roth_IRA = amount

	def getRothIRA(self):
		return self.roth_IRA

	def setNetIncome(self):
		self.net_income = self.after_tax_income - self.roth_401k - self.roth_IRA

	def getNetIncome(self):
		return self.net_income

	def federalBracket(self, income):
		if income <= 0:
			return 0 

		elif income > 523600:
			return 157804.25 + ((income - 523600) * 0.37)

		elif income > 209425:
			return 47843 + ((income - 209425) * 0.35)

		elif income > 164925:
			return 33603 + ((income - 164925) * 0.32)

		elif income > 86375:
			return 14751 + ((income - 86375) * 0.24)

		elif income > 40525:
			return 4664 + ((income - 40525) * 0.22)

		elif income > 9950:
			return 995 + ((income - 9950) * 0.12)

		else:
			return income * 0.10

	def stateBracket(self, income):
		if income <= 0:
			return 0 

		elif income > 625369:
			return 60789.92 + ((income - 625369) * 0.123)

		elif income > 375221:
			return 32523.20 + ((income - 375221) * 0.113)

		elif income > 312686:
			return 26082.09 + ((income - 312686) * 0.103)

		elif income > 61214:
			return 2695.19 + ((income - 61214) * 0.093)

		elif income > 48435:
			return 1672.87 + ((income - 48435) * 0.08)

		elif income > 34892:
			return 860.29 + ((income - 34892) * 0.06)

		elif income > 22107:
			return 348.89 + ((income - 22107) * 0.04)

		elif income > 9325:
			return 93.25 + ((income - 9325) * 0.02)

		else:
			return income * 0.01

	def getFederalDeductionMax(self):
		self.federal_deduction = min(self.federal_deduction, self.gross)
		return self.federal_deduction

	def getStateDeductionMax(self):
		self.state_deduction = min(self.state_deduction, self.gross)
		return self.state_deduction

	#implement age contribution limit...20,500 + 6,500? if age = 60+?
	def getTraditional401kMax(self):
		self.max_401k = min(self.gross, self.max_401k)
		return self.max_401k

	def getRoth401kMax(self):
		return self.max_401k - self.traditional_401k


	#implement age contribution limit...aka max amount is 7k for 50 y/o
	def getRothIRAMax(self):
		max_contribution = self.gross
		if max_contribution == 0 or max_contribution >= 144000:
			return 0

		elif max_contribution <= 129000:
			max_contribution = 6000

		elif max_contribution <= 130500:
			max_contribution = 5400

		elif max_contribution <= 132000:
			max_contribution = 4800

		elif max_contribution <= 133500:
			max_contribution = 4200

		elif max_contribution <= 135000:
			max_contribution = 3600

		elif max_contribution <= 136500:
			max_contribution = 3000

		elif max_contribution <= 138000:
			max_contribution = 2400

		elif max_contribution <= 139500:
			max_contribution = 1800

		elif max_contribution <= 141000:
			max_contribution = 1200

		else:
			max_contribution = 600

		return max_contribution