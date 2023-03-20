# income:
    # - rental income = 2000/month
    # total income = 2000/month

# purchase price 200,000

# expenses:
    # - taxes = 150/month
    # - insurance = 100/month
    # - utilities = 0/month
        # - elec
        # - water
        # - sewer
        # - gas
    # - hoa = 0/month
    # - lawn/snow = 0/month
    # - vacancy = 100/month
    # - repairs = 100/month
    # - capex = 100/month
    # - property mangement = 200/month
    # - mortgage = 860/month

    # total = 1610/month

# cashflow = 390/month

# cash on cash roi
    # - downpayment = 40,000
    # - closing costs = 3000
    # - rehab budget = 7000
    # - misc = 0
    # total investment = 50,000

# anual cash flow = 4680

# cash on cash roi = 9.36%

class CashOnCash():
    """
        the purpose of this class is to provide information about cash on cash ROI 
        for a rental property
    """
    def __init__(self, income):
        self.income = income

    def expenses(
            self, taxes, insurance, vacancy, repairs, capex, property_management, 
            mortgage, utilities = 0, hoa = 0, ls = 0):
        self.taxes = taxes
        self.insurance = insurance
        self.vacancy = vacancy
        self.repairs = repairs
        self.capex = capex
        self.property_management = property_management
        self.mortgage = mortgage
        self.utilities = utilities
        self.hoa = hoa
        self.ls = ls

        self.total = self.taxes + self.insurance + self.vacancy + self.repairs + self.capex 
        self.total += self.property_management + self.mortgage + self.hoa + self.utilities + self.ls

        return self.total
    
    def cashflow(self):
        return self.income - self.total
    
    def invested(self):
        self.down = int(input("What was the down payment?  "))
        self.closing = int(input("What were the closing costs?  "))
        self.rehab = int(input("What was the rehab budget?  "))
        self.misc = int(input("What were the misc costs?  "))

        return self.down + self.closing + self.rehab + self.misc
    
    def anual_cashflow(self):
        return CashOnCash.cashflow(self) * 12
    
    def roi(self):
        self.roi = CashOnCash.anual_cashflow(self) / CashOnCash.invested(self)
        self.roi *= 100
        print(f"\nThe cash on cash ROI for this property is {self.roi}%")
    
income = 2000
taxes = 150
insurance = 100
utilities = 0
hoa = 0
lawn_snow = 0
vacancy = 100
repairs = 100
capex = 100
property_management = 200
mortgage = 860

downpayment = 40000
closing_costs = 3000
rehab_budget = 7000
misc = 0

rental_property = CashOnCash(income)

rental_property.expenses(taxes, insurance, vacancy, repairs, capex, property_management, mortgage)
rental_property.cashflow()
rental_property.anual_cashflow()
rental_property.roi()

