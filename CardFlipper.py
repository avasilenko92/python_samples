
set1 = "0100110"
set2 = "01001100111"
set3 = "100001100101000"
#[11, 10, 6, 0, 1, 2, 3, 4, 5, 7, 8, 9, 12, 13, 14]
#0 1 2 3 4 6 5 7 8 11 10 9 12 13 14

gameSet = []
rawInput = set3

def flipCard(chosenIndex):
    global gameSet
    global rawInput
    try:
        chosenIndex = int(chosenIndex)
        if chosenIndex >= len(gameSet) or chosenIndex < 0:
            return False
    except:
        print("Not an index!")
        return False
    if gameSet[chosenIndex] == "1":
        gameSet[chosenIndex] = "-"
        if chosenIndex - 1 >= 0:
            if gameSet[chosenIndex - 1] == "1":
                gameSet[chosenIndex - 1] = "0"
            elif gameSet[chosenIndex - 1] == "0":
                gameSet[chosenIndex - 1] = "1"
        if chosenIndex + 1 < len(gameSet):
            if gameSet[chosenIndex + 1] == "1":
                gameSet[chosenIndex + 1] = "0"
            elif gameSet[chosenIndex + 1] == "0":
                gameSet[chosenIndex + 1] = "1"
        rawInput = ""
        for x in gameSet:
            rawInput += x
        return True
    else:
        return False


def solve():
    global gameSet
    #How to solve:
    #0. Check for odd number of 1s (winnable)
    ones = 0
    for i, x in enumerate(gameSet):
        if x == "1":
            ones += 1
    if ones % 2 != 1:
        print("Unsolvable, " + str(ones) + " ones found")
        exit(0)


    #1. Find yellow card
    #2. ???
    #3. Solved!
    print("Solved!")
    exit(0)


def main():
    global gameSet
    global rawInput
    index = ""
    quit = False
    for x in rawInput:
        gameSet.append(x)
    for i,x in enumerate(gameSet):
        index += str(i)
    while quit != True:
        print("Set:" + rawInput)
        print("Pos:" + index)
        value = input("Pick a card to flip (q to quit)(s to solve): ")
        if value == "q" or value == "Q":
            quit = True
        if value == "s" or value == "S":
            solve()
        else:
            flipped = flipCard(value)
            if not flipped:
                print("Card not flippable, please try again")

if __name__ == '__main__':
    main()