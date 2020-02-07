
#This script is designed to take in a number and print out the fibonacci sequence up to the nth item
#Expected Input: An integer received via user prompt
#Expected Output: The fibonacci sequence up to the nth value of the given number
def main():
    n = int(input("Please enter an integer: "))
    for i in range(n):
        print(str(i + 1) + ": " + str(fibonacciSequence(i + 1)))

def fibonacciSequence(num):
    if num == 0:
        return 0
    if num == 1 or num == 2:
        return 1
    return fibonacciSequence(num - 2) + fibonacciSequence(num - 1)

if __name__ == '__main__':
    main()