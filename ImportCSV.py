
#This script is designed to open a specific csv file of sock data, output the color of a sock,
# output all the details about that sock, and then output the sock details to an enumerated file.
#Expected Input: 4 column csv file in specified location, columns are length, color, toe color, & thickness respectively
#Expected Output: x number of csv files containing a single sock, x is the number of socks in the input file
def main():
    file = open("C:\\Users\\avasilenko\\Downloads\\Socks.csv")
    f1 = file.readlines()
    for i, x in enumerate(f1):
        x = x.rstrip("\n")
        sock = x.split(",")
        print("Row#" + str(i + 1) + ": " + x)
        print("Sock Color: " + sock[1])
        file2 = open("Sock" + str(i + 1) + ".txt", "w+")
        file2.write(x)
    file.close()

    #This block demonstrates grabbing a single color of a specific sock without using a loop
    file = open("C:\\Users\\avasilenko\\Downloads\\Socks.csv")
    sockFile = file.read()
    sock = sockFile.split("\n")
    sockItem = sock[1].split(",")
    print("\nThe color of the 2nd sock is: " + sockItem[1])
    file.close()

if __name__ == '__main__':
    main()
