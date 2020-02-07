import random
import time
import sys
import Sock

#This script is designed to generate x number of CSV files with 20,000 socks in each CSV
#Expected input: (Optional: number of csvs to generates, defaults to 1)
#Expected output: A csv denoted w/ an epoch timestamp that contains 20,000 socks
def generateEntry(attributes):
    return attributes[random.randrange(len(attributes))]

def main():
    random.seed(a=None, version=2)
    lengthArray = ["knee","ankle","low","thigh"]
    colorArray = ["purple","green","yellow","white","gray","blue","red"]
    thicknessArray = ["thin","thick","wooly"]
    if (len(sys.argv) >= 2 and int(sys.argv[1]) > 0):
        r = int(sys.argv[1])
    else:
        r = 1
    print("Range is" + str(r))
    for y in range(int(r)):
        sockCSV = open("SocksFrom" + str(time.time()) + ".csv", "w+")
        print("Writing to: " + sockCSV.name)
        for x in range(20000):
            s = Sock.Sock(generateEntry(lengthArray), generateEntry(colorArray), generateEntry(colorArray), generateEntry(thicknessArray))
            sockCSV.write(s.csvSockEntry() + "\n")
        sockCSV.close()

if __name__ == "__main__":
    main()