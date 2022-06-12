from maze import Maze
from room import Room


def play(my_maze):
    # Play a game
    while not my_maze.atExit():
        print(my_maze.getCurrent())

        # TODO: Get direction from user
        try:
            direction = input(
                "Enter direction to move north west east south restart")
            # TODO: Based on choice do what was asked.
            if direction == 'north':
                my_maze.moveNorth()
            elif direction == 'south':
                my_maze.moveSouth()
            elif direction == 'east':
                my_maze.moveEast()
            elif direction == 'west':
                my_maze.moveWest()
            # elif direction == 'q':
            #     return
            elif direction == 'restart':
                my_maze.reset()
            elif direction == '':
                return
            else:
                raise Exception
        except Exception as e:
            print("Invalid Entry")

    print("You found the exit!")
    return


# **SIMPLE_MAZE** :  This maze should be solved when the movements east and north  are applied in that order. This means you arrive at the exit when you go east room and then the north room. The description of each room doesn't matter since the correctness will be graded. The ORDER matters.
# TODO: Create the SIMPLE_MAZE
rooms1 = []
rooms1.append(Room("This room is the entrance"))
rooms1.append(Room("This room has a table. Maybe a dining room?"))
rooms1.append(Room("This room is the exit. Good Job."))
rooms1[0].setEast(rooms1[1])
rooms1[1].setWest(rooms1[0])

rooms1[1].setNorth(rooms1[2])
rooms1[2].setSouth(rooms1[1])
SIMPLE_MAZE = Maze(rooms1[0], rooms1[2])


# **INTERMEDIATE_MAZE** :  This maze should be solved when the movements are west, west, west, north, east. This means you arrive at the exit when you go west room, then west room again, then west room again, then take north and then finally the final east room. At the end of the movements, atExit should be true when it is called. The description of each room doesn't matter since the correctness will be graded.
# TODO: Create the INTERMEDIATE_MAZE
room1 = Room("Room1")
room2 = Room("Room2")
room3 = Room("Room3")
room4 = Room("Room4")
room5 = Room("Room5")
room6 = Room("Room6")

room1.setWest(room2)
room2.setEast(room1)

room2.setWest(room3)
room3.setEast(room2)

room3.setWest(room4)
room4.setEast(room3)

room4.setNorth(room5)
room5.setSouth(room4)

room5.setEast(room6)
room6.setWest(room5)


INTERMEDIATE_MAZE = Maze(room1, room6)


if __name__ == "__main__":
    play(INTERMEDIATE_MAZE)
    # TODO: Define this play function above and run on your INTERMEDIATE_MAZE
