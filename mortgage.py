import math
# import pandas as pd

class Mortgage:

    '''
    This class defines the Mortgage object and provides methods to calculate the monthly repayment, total amount repaid and total interest paid.
    It also provides a set of getter functions that will calculate and return important features of the mortgage, inclduing:
        - monthly repayment
        - total amount repaid
        - total interest paid
        - monthly payment schedule
    
    The object can be initialised with the following parameters:
        - property_value
        - deposit_amount
        - interest_rate
        - loan_term
    
    And, optionally, the following parameters:
        - is_variable_rate
        - intro_rate_term
        - introductory_rate
    
    The initialization is done with all of the args set to None and the user is prompted to enter the values for each of the args.
    '''

    def __init__(self, property_value=None, deposit_amount=None, interest_rate=None, loan_term=None, is_variable_rate=None, intro_rate_term=None, introductory_rate=None):
        if property_value is None:
            property_value, deposit_amount, interest_rate, loan_term, is_variable_rate, intro_rate_term, introductory_rate = self.get_user_inputs()
        self.property_value = property_value
        self.deposit_amount = deposit_amount
        self.interest_rate = interest_rate
        self.loan_term = loan_term
        self.is_variable_rate = is_variable_rate
        if is_variable_rate:
            self.intro_rate_term = intro_rate_term
            self.introductory_rate = introductory_rate


    def get_user_inputs(self):

        while True:
            try:
                property_value = float(input("Enter the total property value: "))
                if property_value <= 0:
                    raise ValueError("Property value must be a positive number.")
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                deposit_amount = float(input("Enter the deposit amount: "))
                if deposit_amount < 0:
                    raise ValueError("Deposit amount cannot be negative.")
                if deposit_amount > property_value:
                    raise ValueError("Deposit amount cannot be greater than property value.")
                break
            except ValueError as e:
                print(e)

        while True:
            try:
                loan_term = int(input("Enter the loan term (in years): "))
                if loan_term <= 0:
                    raise ValueError("Loan term must be a positive integer.")
                break
            except ValueError as e:
                print(e)

        while True:
            is_variable_rate = input("Is the interest rate variable (Y/N)? ")
            if is_variable_rate.lower() == "y":
                is_variable_rate = True
                while True:
                    try:
                        intro_rate_term = int(input("Enter the introductory rate period (in years): "))
                        if intro_rate_term <= 0 or intro_rate_term > loan_term:
                            raise ValueError("introductory rate period must be a positive integer less than the loan term.")
                        break
                    except ValueError as e:
                        print(e)
                break
            elif is_variable_rate.lower() == "n":
                is_variable_rate = False
                intro_rate_term = 0
                break
            else:
                print("Please enter Y or N.")
        
        if is_variable_rate:
            while True:
                try:
                    introductory_rate = float(input("Enter the introductory interest rate (as a decimal): "))
                    if introductory_rate < 0 or introductory_rate > 1:
                        raise ValueError("Interest rate must be between 0 and 1.")
                    break
                except ValueError as e:
                    print(e)
            while True:
                try:
                    interest_rate = float(input("Enter the interest rate for the rest of the mortgage term (as a decimal): "))
                    if interest_rate < 0 or interest_rate > 1:
                        raise ValueError("Interest rate must be between 0 and 1.")
                    break
                except ValueError as e:
                    print(e)
       
        elif not is_variable_rate:
            while True:
                try:
                    interest_rate = float(input("Enter the interest rate (as a decimal): "))
                    if interest_rate < 0 or interest_rate > 1:
                        raise ValueError("Interest rate must be between 0 and 1.")
                    break
                except ValueError as e:
                    print(e)
            introductory_rate = interest_rate
        
        else:
            print("Error getting interest rate.")
      
        return property_value, deposit_amount, interest_rate, loan_term, is_variable_rate, intro_rate_term, introductory_rate


    def calculate_fixed_rate_monthly_repayment(self) -> float:
        try:
            if not self.is_variable_rate:
                loan_amount = self.property_value - self.deposit_amount
                monthly_interest_rate = self.interest_rate / 12
                num_payments = self.loan_term * 12
                monthly_repayment = (loan_amount * monthly_interest_rate) / (1 - math.pow(1 + monthly_interest_rate, - num_payments))
                return monthly_repayment
        except:
            print("Error calculating monthly repayment.")


    def calculate_variable_rate_monthly_repayment(self) -> list:
        loan_amount = self.property_value - self.deposit_amount
        num_payments = self.loan_term * 12
        monthly_repayments = []
        try:
            if self.is_variable_rate:
                for i in range(num_payments):
                    if i <= (self.intro_rate_term * 12):
                        monthly_interest_rate = self.introductory_rate / 12
                    else:
                        monthly_interest_rate = self.interest_rate / 12
                    remaining_payments = (self.loan_term - self.intro_rate_term) * 12
                    monthly_repayment = (loan_amount * monthly_interest_rate) / (1 - math.pow(1 + monthly_interest_rate, -remaining_payments))
                    monthly_repayments.append(monthly_repayment)
            return monthly_repayments
        except:
            print("Error calculating monthly repayment.")


    def calculate_total_amount_repaid(self) -> float:
        total_amount_repaid = 0
        if self.is_variable_rate:
            monthly_repayments = self.calculate_variable_rate_monthly_repayment()
            total_amount_repaid = sum(monthly_repayments)
        elif not self.is_variable_rate:
            total_amount_repaid = self.calculate_fixed_rate_monthly_repayment() * (self.loan_term * 12)
        else:
            print("Error calculating total amount repaid.")
        return round(total_amount_repaid, 2)


    def calculate_total_interest_paid(self) -> float:
        loan_amount = self.property_value - self.deposit_amount
        total_interest_paid = self.calculate_total_amount_repaid() - loan_amount
        return round(total_interest_paid, 2)
    
    # The getter functions...

    def print_mortgage_details(self):
        '''
        This method prints the mortgage details to the console.
        '''
        print("Mortgage details:")
        print("Property value: ", round(self.property_value, 2))
        print("Deposit amount: ", round(self.deposit_amount, 2))
        print("Interest rate: ", round(self.interest_rate, 2))
        print("Loan term: ", self.loan_term)
        print("Is variable rate: ", self.is_variable_rate)
        if self.is_variable_rate:
            print("Introductory rate term: ", self.intro_rate_term)
            print("Introductory rate: ", round(self.introductory_rate, 2))
            print("Monthly repayment: ", round(self.calculate_variable_rate_monthly_repayment()[0], 2))
        else:
            print("Monthly repayment: ", round(self.calculate_fixed_rate_monthly_repayment(), 2))
        print("Total interest paid: ", self.calculate_total_interest_paid())
        print("Total amount repaid: ", self.calculate_total_amount_repaid())


    def get_mortgage_details(self) -> dict:
        '''
        This method returns a dictionary containing the mortgage details.
        '''
        mortgage_details = {
            "property_value": self.property_value,
            "deposit_amount": self.deposit_amount,
            "interest_rate": self.interest_rate,
            "loan_term": self.loan_term,
            "is_variable_rate": self.is_variable_rate,
            "intro_rate_term": self.intro_rate_term,
            "introductory_rate": self.introductory_rate,
            "monthly_repayment": self.monthly_repayment,
            "total_interest_paid": self.calculate_total_interest_paid(),
            "total_amount_repaid": self.calculate_total_amount_repaid()
        }
        return mortgage_details
    

    def print_fixed_rate_monthly_payment_details(self):

        '''
        This method prints information for each monthly payment for a fixed rate mortgage
        to the console and will display the following details:
            - Payment number
            - Interest paid
            - Principle paid
            - Remaining balance
        '''

        if not self.is_variable_rate:
            num_payments = self.loan_term * 12
            loan_value = self.property_value - self.deposit_amount
            monthly_repayment = self.calculate_fixed_rate_monthly_repayment()
            balance = loan_value
            for i in range(num_payments):
                interest_paid = balance * (self.interest_rate / 12)
                principle_paid = monthly_repayment - interest_paid
                balance -= principle_paid
                print("Payment %2d  |  Interest: $%8.2f  |  Principle: $%8.2f  |  Remaining Balance: $%8.2f" % (i+1, interest_paid, principle_paid, balance))


    def get_fixed_rate_monthly_payment_details(self) -> dict:
        '''
        This method returns a dictionary containing the details for each monthly payment for a fixed rate mortgage.
        The structure of the dictionary is as follows:
            - keys = payment number, interest paid, principle paid, remaining balance
            - values = lists of the corresponding values for each payment
        '''
        if not self.is_variable_rate:
            num_payments = self.loan_term * 12
            loan_value = self.property_value - self.deposit_amount
            monthly_repayment = self.calculate_fixed_rate_monthly_repayment()
            balance = loan_value
            payment_number = []
            interest_paid = []
            principle_paid = []
            remaining_balance = []
            monthly_payment_details = {
                    "payment_number": payment_number,
                    "interest_paid": interest_paid,
                    "principle_paid": principle_paid,
                    "remaining_balance": remaining_balance
                }
            
            for i in range(num_payments):
                interest_paid = balance * (self.interest_rate / 12)
                principle_paid = monthly_repayment - interest_paid
                balance -= principle_paid
                monthly_payment_details["payment_number"].append(i+1)
                monthly_payment_details["interest_paid"].append(interest_paid)
                monthly_payment_details["principle_paid"].append(principle_paid)
                monthly_payment_details["remaining_balance"].append(balance)

            return monthly_payment_details



    def print_variable_rate_monthly_payment_details(self):
        '''
        This method prints information for each monthly payment for a variable rate mortgage
        to the console and will display the following details:
            - Payment number
            - Interest paid
            - Principle paid
            - Remaining balance
        '''
        loan_amount = self.property_value - self.deposit_amount
        num_payments = self.loan_term * 12
        payments = []

        balance = loan_amount
        for i in range(num_payments):
            if i < self.intro_rate_term * 12:
                monthly_interest_rate = self.introductory_rate / 12
            else:
                monthly_interest_rate = self.interest_rate / 12
            
            monthly_repayment = (monthly_interest_rate * balance) / (1 - math.pow(1 + monthly_interest_rate, -num_payments + i))
            
            interest_paid = balance * monthly_interest_rate
            principle_paid = monthly_repayment - interest_paid
            balance -= principle_paid
            
            payments.append((i+1, interest_paid, principle_paid, balance))

        for payment in payments:
            print("Payment %2d - Interest: $%8.2f, Principle: $%8.2f, Balance: $%10.2f" % payment)
    

    def get_monthly_payment_schedule(self) -> list:
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