# This script will read in a csv file and count the number of matches
# Expected Input: A hardcoded csv file
# Expected Output: The number of matched and unmatched socks
import Sock


def main():
    file = open("SocksFrom1573786131.9717295.csv")
    f1 = file.readlines()
    matches = 0
    for i, x in enumerate(f1):
        if x == "":
            continue
        x = x.rstrip("\n")
        sockList = x.split(",")
        sock = Sock.Sock(sockList[0], sockList[1], sockList[2], sockList[3])
        if i < len(f1) - 1:
            f2 = f1[i + 1:]
            for j, y in enumerate(f2):
                y = y.rstrip("\n")
                if y == "":
                    continue
                sockList = y.split(",")
                if sock.matches(sockList[0], sockList[1], sockList[2], sockList[3]):
                    f1[i + j + 1] = ""
                    matches = matches + 1
                    sock.printSock();
                    break
    print("Found " + str(matches) + " matches, and " + str(len(f1) - (matches*2)) + " unmatched")
    file.close()

if __name__ == '__main__':
    main()
