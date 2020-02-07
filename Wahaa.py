
#This script will print Wahaa! x number of times when the function is called
#Expected Input: Hard coded x value used as function argument
#Expected Output: Wahaa! x number of times
def main():
    x = 15
    print("Printing Wahaa! " + str(x) + " times on the same line")
    wahaaSameLine(x)
    print()
    print("Printing Wahaa! " + str(x) + " times on different lines")
    wahaaSeperateLines(x)
    print()
    y = 3
    print("Printing Wahaa! " + str(y) + " times on the same line")
    wahaaSameLine(y)
    print()

def wahaaSameLine(x):
    print("Wahaa! " * x)

def wahaaSeperateLines(num):
    for i in range(num):
        print("Wahaa!")

if __name__ == '__main__':
    main()
