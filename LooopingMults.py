
#This script is designed to do integer multiplication using only addition and looping
#Expected Input: Two integers provided by user via prompt
#Expected Output: The value of the two integers multiplied together printed to the console
def main():
    x = int(input("Numba1: "))
    y = int(input("Numba2: "))
    print(str(x) + " * " + str(y) + " = " + str(addLoop(x,y)))

def addLoop(x,y):
    value = 0
    if y < 0:
        y = abs(y)
        x = -x
    for i in range(y):
        value = value + x
    return value


if __name__ == '__main__':
    main()