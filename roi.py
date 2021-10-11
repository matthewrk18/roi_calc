class roiCalc:

    def __init__(self, cashInvest, income, expenses, cashFlow, cashROI):

        self.cashInvest = cashInvest
        self.income = income
        self.expenses = expenses
        self.cashFlow = cashFlow
        self.cashROI = cashROI



    def outPocket(self):

        ask = int(input("What is your total out of pocket investment? Please include Down Payment, Closing Costs, Rehab Budget, etc."))

        self.cashInvest = ask

    def cashIn(self):

        ask = int(input("What is your expected total monthly income from this property? Please include income from rent, laundry, storage, etc."))

        self.income = ask

    def cashOut(self):

        ask = int(input("What is your expected total monthly expenses for this property? Please include Mortgage, Insurance, Taxes, Vacancy, Repairs, CapEx, Property Management, etc. "))

        self.expenses = ask


    def yearlyFlow(self):

        self.cashFlow = (self.income - self.expenses)*12


    def totalROI(self):

        self.cashROI = float((self.cashFlow/self.cashInvest)*100)




def run():

    money = roiCalc(0,0,0,0,0)

    money.outPocket()
    money.cashIn()
    money.cashOut()
    money.yearlyFlow()
    money.totalROI()
    
    if money.cashROI >= 10:
        print(f"ROI: {money.cashROI:.2f}%  This is a good investment.")
    else:
        print(f"ROI: {money.cashROI:.2f}%  This is not a good investment.")

run()
