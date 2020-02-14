
#This script was used to demonstrate the basic mathematical operations available to us
#Expected Input: Hard coded integers
#Expected Output: Console output results

def main():
    a = 5
    b = 7
    c = 10
    d = 3
    # addition
    additionResult = (a + b + c + d)
    output = str(a) + " + " + str(b) + " + " + str(c) + " + " + str(d) + " = " + str(additionResult)
    print(output)
    # subtraction
    subtractionResult = (b - a - c - d)
    output = str(b) + " - " + str(a) + " - " + str(c) + " - " + str(d) + " = " + str(subtractionResult)
    print(output)
    # multiplication
    multiplicationResult = (a * b * c * d)
    output = str(a) + " * " + str(b) + " * " + str(c) + " * " + str(d) + " = " + str(multiplicationResult)
    print(output)
    # division
    divisionResult = (multiplicationResult / subtractionResult)
    output = str(multiplicationResult) + " / " + str(subtractionResult) + " = " + str(divisionResult)
    print(output)


if __name__ == '__main__':
    main()