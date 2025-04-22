# utils/finance_tools.py

import numpy as np

def present_value(future_value, interest_rate, time_periods):
    """Calculates the present value of an investment."""
    return future_value / (1 + interest_rate) ** time_periods

def future_value(present_value, interest_rate, time_periods):
    """Calculates the future value of an investment."""
    return present_value * (1 + interest_rate) ** time_periods

def compound_interest(principal, rate, time):
    """Calculates compound interest."""
    return principal * (1 + rate) ** time

print("File changed")
