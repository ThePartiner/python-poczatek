import math

def calculation_locat (capital, percentage, years):
    value = capital * (1 + (percentage/100)) ** years
    return value
