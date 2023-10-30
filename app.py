# --------------------
# Author: Daniel Hardej
# Date created: 2023-07-29
# Date modified: 2023-07-29
# Description: Main file for the mortgage calculator application
# --------------------
# Notes:
# So far, this is just a placeholder file for the mortgage calculator application. I just whipped it up to test the mortgage class and 
# the mortgage functions in mortgage.py. I will be adding more to this file as I develop the application.
# It probably won't run properly at the moment, but it'll get updeted soon...
# --------------------

from mortgage import Mortgage
import math
# import pandas as pd

def __main__():
    mortgage_details = Mortgage()
    print(mortgage_details.is_variable_rate)
    mortgage_details.print_variable_rate_monthly_payment_details()
    mortgage_details.print_mortgage_details()
    

if __name__ == "__main__":
    __main__()

