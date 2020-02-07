class Sock:

    def __init__(self, slength, scolor, stoeColor, sthickness):
        self.length = slength
        self.color = scolor
        self.toeColor = stoeColor
        self.thickness = sthickness


    def printSock(self):
        print("The sock is: " + str(self.length) + " " + str(self.color) + " " + str(self.toeColor) + " " + str(self.thickness))

    def changeColor(self, color):
        self.color = color

    def csvSockEntry(self):
        return self.length + "," + self.color + "," + self.toeColor + "," + self.thickness
