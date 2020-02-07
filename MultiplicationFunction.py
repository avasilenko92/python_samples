
#This script is designed to take two integers as user input, pass the numbers into a function that will return
# the multiplied value
#Expected Input: Two integers sent in via user prompt
#Expected Output: Value of the two integers multiplied together printed to the console
def main():
    print("Give me two numbers to multiply")
    x1=float(input("The first number is: "))
    y1=float(input("The second number is: "))
    value=multiply(x1,y1)
    print(str(x1) + " * " + str(y1) + " = " + str(value))
    #Alternatively...
    print(str(x1) + " * " + str(y1) + " = " + str(multiply(x1,y1)))

def multiply(x,y):
   return x * y

if __name__ == '__main__':
    main()