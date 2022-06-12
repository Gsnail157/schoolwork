# Mark Boady
# CS 172 - Maze Game
# Drexel University 2018

class Maze:
    # Inputs: Pointer to start room and exit room
    # Sets current to be start room
    def __init__(self, st=None, ex=None):
        pass
        # TODO
        # Room the player starts in
        self.start = st
        # If the player finds this room they win
        self.end = ex

        # What room is the player currently in
        self.current = st

    # Return the room the player is in (current)
    def getCurrent(self):
        return self.current

    # The next four all have the same idea
    # See if there is a room in the direction
    # If the direction is None, then it is impossible to go that way
    # in this case return false
    # If the direction is not None, then it is possible to go this way
    # Update current to the new move (move the player)
    # then return true so the main program knows it worked.

    def moveNorth(self):

        if self.current.getNorth() == None:
            print("Direction invalid, try again.")
        else:
            self.current = self.current.getNorth()
            print("You went north")

    def moveSouth(self):
        if self.current.getSouth() == None:
            print("Direction invalid, try again.")
        else:
            self.current = self.current.getSouth()
            print("You went south")

    def moveEast(self):
        if self.current.getEast() == None:
            print("Direction invalid, try again.")
        else:
            self.current = self.current.getEast()
            print("You went east")

    def moveWest(self):
        if self.current.getWest() == None:
            print("Direction invalid, try again.")
        else:
            self.current = self.current.getWest()
            print("You went west")

    # If the current room is the exit,
    # then the player won! return true
    # otherwise return false

    def atExit(self):
        if self.current == self.end:
            return True
        else:
            return False

    # If you get stuck in the maze, you should be able to go
    # back to the start
    # This sets current to be the start_room
    def reset(self):
        self.current = self.start
        print("You went back to the start!")
        return
