# This script is designed to search a sorted array and use the binary search method to locate a number
# Expected Input: Hardcoded array of integers and a number to locate
# Expected Output: The list getting halved as it searches for the number, if the number is not found, then the
# closest guess
import math


def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 7, 9, 10]
    number = 11
    midpoint = math.floor(len(arr) / 2)
    guess = arr[midpoint]
    print("First Guess: " + str(guess) + " First Index: " + str(midpoint))
    while guess != number and midpoint > 0:
        if guess > number:
            arr = arr[0:midpoint]
        else:
            arr = arr[midpoint:len(arr)]
        midpoint = math.floor(len(arr) / 2)
        guess = arr[midpoint]
        print("Arr: " + str(arr) + " Guess: " + str(guess) + " Midpoint: " + str(midpoint))
    print("Guess ended at: " + str(guess))


if __name__ == '__main__':
    main()
