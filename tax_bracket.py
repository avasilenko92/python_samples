### The function takes a household income and determines the tax liability ###

def tax(x):
    if x <= 10000:
        return int(x * 0)
    elif x <= 30000:
        x1 = x - 10000
        return int(x1 * 0.1)
    elif x <= 100000:
        x1 = 20000 * 0.1
        x2 = x - 30000
        return int(x1 + (x2 * 0.25))
    else:
        x1 = 20000 * 0.1
        x2 = 70000 * 0.25
        x3 = x - 100000
        return int(x1 + x2 + (x3 * 0.40))

print(tax(0))
print(tax(10000))
print(tax(10009))
print(tax(10010))
print(tax(12000))
print(tax(56789))
print(tax(1234567))
