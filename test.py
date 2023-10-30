from mortgage import Mortgage

def __main__():
    mortgage = Mortgage(500000, 100000, 0.05, 25, False)

    mortgage.print_fixed_rate_monthly_payment_details()

    print(mortgage.print_mortgage_details())
    if mortgage.is_variable_rate:
        print("Your monthly repayments are: ", mortgage.calculate_variable_rate_monthly_repayment()[0])
    else:
        print("Your monthly repayments are: ", mortgage.calculate_fixed_rate_monthly_repayment())
    print("Your total interest paid is: ", mortgage.calculate_total_interest_paid())
    print("Your total amount repaid is: ", mortgage.calculate_total_amount_repaid())


if __name__ == "__main__":
    __main__()