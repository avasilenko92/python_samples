import math
import constants

#TESTING CHANGE

#TODO Reverse List
def tax(income):
    bracket = constants.brackets
    first = list(bracket.keys())[0]
    reversed = False
    if first != "maximum":
        reversed = True
    keys = bracket.keys()
    tax = 0
    for i,key in enumerate(keys):
        if i + 1 < len(keys):
            cutoff = list(bracket.keys())[i + 1]
        else:
            cutoff = 0
        taxed = income - cutoff
        if taxed > 0:
            tax += taxed * bracket[key]/100
            income = cutoff
    return math.floor(tax)

def main():
    incomes = [0,10000,10009,10010,12000,56789,1234567]
    for income in incomes:
        print("Tax on " + str(income) + " is " + str(tax(income)))

if __name__ == '__main__':
    main()
