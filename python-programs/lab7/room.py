# Simple Maze Class
# Mark Boady
# Drexel University
# CS 172

class Room:
    # Constructor sets the description
    # And all four doors should be initially set to None
    def __init__(self, descr):
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.descr = descr
        pass

    # Accessors
    # Return the correct values
    def __str__(self):
        return self.descr

    def getNorth(self):
        return self.north

    def getSouth(self):
        return self.south

    def getEast(self):
        return self.east

    def getWest(self):
        return self.west

    # Mutators
    # Update the values
    def setDescription(self, d):
        self.descr = d
        return

    def setNorth(self, n):
        self.north = n
        return

    def setSouth(self, s):
        self.south = s
        return

    def setEast(self, e):
        self.east = e
        return

    def setWest(self, w):
        self.west = w
        return
