
def  doesCircleExist( commands):
    """Robot computer simulation where robot moves on an infinite plane,
    starting from position (0, 0). Its movements are described by:

    G: go forward one step
    L: rotate left
    R: rotate right

    The movements in the input string *are repeated for an infinite time*.
    Find if there exists a circle, whose radius is some positive real number
    such that the bot never leaves it.
    """

    # 1. it seems like the bot has to return to its original position
    # therefore this can be broken down into keeping track of which way the
    # bot is facing and whether or not the pattern returns the bot to (0, 0)
    # 2. there is also the case where the bot follows a mirrored path
    # e.g., 'GRGRG'. the below code does not address this.
    num_commands = len(commands)

    # starting direction
    direction = 'N'

    # starting coordinates
    position = [0, 0]

    # execute the commands
    i = 0
    while i < num_commands:
        if commands[i] == 'G':
            position = moveBot(position, direction)
        else: # command == 'R' or 'L'
            direction = rotateBot(direction, commands[i])
        i += 1

    if position[0] == 0 and position[1] == 0:
        return 'YES'
    else:
        return 'NO'


def moveBot(curr_coor, curr_dir):
    """For the 'G' command, move the bot in the correct direction.
    Return the new positional coordinates.
    """
    x = curr_coor[0]
    y = curr_coor[1]

    if curr_dir == 'N':
        y += 1
    elif curr_dir == 'E':
        x += 1
    elif curr_dir == 'S':
        y -= 1
    else: #curr_dir == 'west'
        x -= 1

    return [x, y]


def rotateBot(curr_dir, command):
    if command == 'R':
        if curr_dir == 'N':
            return 'E'
        elif curr_dir == 'E':
            return 'S'
        elif curr_dir == 'S':
            return 'W'
        else: #curr_dir == 'west'
            return 'N'
    elif command == 'L':
        if curr_dir == 'N':
            return 'W'
        elif curr_dir == 'E':
            return 'N'
        elif curr_dir == 'S':
            return 'E'
        else: #curr_dir == 'west'
            return 'S'
    else: # command == 'G'
        return curr_dir


doesCircleExist('GRGL')
