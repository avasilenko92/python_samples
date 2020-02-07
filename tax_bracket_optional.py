import pandas as pd
import os
os.chdir('C:\\Users\\Samuel\\PycharmProjects\\tax_bracket')
file = "tax_bracket.xlsx"
bracket = pd.read_excel(file, header=0)
bracket.income_cap = pd.to_numeric(bracket['income_cap'], errors='coerce')
bracket['liability'] = [0,0,0,0]

#for index, row in bracket.iterrows():
#    bracket.at[index, 'liability'] = row['marginal_tax_rate']*2

income_cap = bracket['income_cap']
marginal_tax_rate = bracket['marginal_tax_rate']

income = 20000

income_holder = income
liability = 0

if income >= income_cap[0]:
    liability = income * marginal_tax_rate[0]
    income_holder = income - income_cap[0]
print(liability)
print(income_holder)

if income >= income_cap[1]:
    liability = liability + (income_holder * marginal_tax_rate[1])
print(liability)
print(income_holder)
