from mortgage import Mortgage
import math

# create a table class that inherits from the mortgage class
class MortgageDetails(Mortgage):

    '''
    This class inherits from the mortgage class and is used to create a table of monthly payments for a mortgage.
    It also provides different methods to display the table of monthly payemnts in different ways:
     - printed to the console
     - written to a csv file
     - displayed in a GUI
     - displayed in a web app
     - created and exported as a pandas dataframe
    '''

    def __init__(self, property_value=None, deposit_amount=None, interest_rate=None, loan_term=None, is_variable_rate=None, intro_rate_term=None, introductory_rate=None):
        super().__init__(property_value, deposit_amount, interest_rate, loan_term, is_variable_rate, intro_rate_term, introductory_rate)
        if self.is_variable_rate:
            self.monthly_repayment = Mortgage.calculate_variable_rate_monthly_repayment(self)
        elif not self.is_variable_rate:
            self.monthly_repayment = Mortgage.calculate_fixed_rate_monthly_repayment(self)

    def create_monthly_payment_schedule(self) -> list:
        '''
        This method creates a list of monthly payments for the mortgage.
        '''
        monthly_payment_schedule = []
        if not self.is_variable_rate:
            for i in range(self.loan_term * 12):
                monthly_payment_schedule.append(self.monthly_repayment)
        elif self.is_variable_rate:
            for i in range(self.loan_term * 12):
                monthly_payment_schedule.append(self.monthly_repayments[i])
        return monthly_payment_schedule

    def print_mortgage_details(self):
        '''
        This method prints the mortgage details to the console.
        '''
        print("Mortgage details:")
        print("Property value: ", self.property_value)
        print("Deposit amount: ", self.deposit_amount)
        print("Interest rate: ", self.interest_rate)
        print("Loan term: ", self.loan_term)
        print("Is variable rate: ", self.is_variable_rate)
        if self.is_variable_rate:
            print("Introductory rate term: ", self.intro_rate_term)
            print("Introductory rate: ", self.introductory_rate)
            print("Monthly repayment: ", self.monthly_repayment[0])
        else:
            print("Monthly repayment: ", self.monthly_repayment)
        print("Total interest paid: ", self.calculate_total_interest_paid())
        print("Total amount repaid: ", self.calculate_total_amount_repaid())

    def print_monthly_payment_schedule(self):
        '''
        This method prints the monthly payment schedule to the console.
        '''
        print("Mortgage payment schedule:")
        print("Monthly payment")
        for i in range(self.loan_term * 12):
            print(f"{i + 1}\t{self.monthly_payment_schedule[i]}")
    
    def print_fixed_rate_monthly_payment_details(self):
        if not self.is_variable_rate:
            num_payments = self.loan_term * 12
            loan_value = self.property_value - self.deposit_amount
            balance = loan_value
            for i in range(num_payments):
                interest_paid = balance * (self.interest_rate / 12)
                principle_paid = self.monthly_repayment - interest_paid
                balance -= principle_paid
                print("Payment %2d  |  Interest: $%8.2f  |  Principle: $%8.2f  |  Remaining Balance: $%8.2f" % (i+1, interest_paid, principle_paid, balance))


    def print_variable_rate_monthly_payment_details(self):

        # Calculate the loan amount
        loan_amount = self.property_value - self.deposit_amount

        # Calculate the number of monthly payments
        num_payments = self.loan_term * 12

        # Create an empty list to store the payment information
        payments = []
        total_interest_paid = 0

        # Calculate the monthly repayment
        balance = loan_amount
        for i in range(num_payments):
            # Calculate the monthly interest rate
            if i < self.intro_rate_term * 12:
                monthly_interest_rate = self.introductory_rate / 12
            else:
                monthly_interest_rate = self.interest_rate / 12
            
            # Calculate the monthly repayment
            monthly_repayment = (monthly_interest_rate * balance) / (1 - math.pow(1 + monthly_interest_rate, -num_payments + i))
            
            # Calculate the amount of each payment that goes towards interest and repaying the principle
            interest_paid = balance * monthly_interest_rate
            total_interest_paid += interest_paid
            principle_paid = monthly_repayment - interest_paid
            balance -= principle_paid
            
            # Add the payment information to the list
            payments.append((i+1, interest_paid, principle_paid, balance))

        # Print the payment information
        for payment in payments:
            print("Payment %2d - Interest: $%8.2f, Principle: $%8.2f, Balance: $%10.2f" % payment)
        
        