from mortgage import Mortgage
import matplotlib.pyplot as plt

'''
This module contains methods to graphically present the mortgage details and monthly payment schedule.
'''

class MortgageGraph(Mortgage):

    def __init__(self):
        super().__init__()
        self.mortgage = Mortgage()
        self.mortgage_details = self.mortgage.get_mortgage_details()
        self.monthly_payment_schedule = self.mortgage.get_monthly_payment_schedule()
        self.monthly_repayment = self.mortgage_details["monthly_repayment"]
        self.loan_term = self.mortgage_details["loan_term"]
        self.is_variable_rate = self.mortgage_details["is_variable_rate"]
        self.intro_rate_term = self.mortgage_details["intro_rate_term"]
        self.introductory_rate = self.mortgage_details["introductory_rate"]
        self.property_value = self.mortgage_details["property_value"]
        self.deposit_amount = self.mortgage_details["deposit_amount"]
        self.interest_rate = self.mortgage_details["interest_rate"]
        self.total_interest_paid = self.mortgage_details["total_interest_paid"]
        self.total_amount_repaid = self.mortgage_details["total_amount_repaid"]
    
    def plot_mortgage_balance(self):
        '''
        This method plots the mortgage balance over time.
        '''
        pass