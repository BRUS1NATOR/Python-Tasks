from enum import Enum
from enum import IntEnum


class IsPathable(Enum):
    DeadEnd = 1,
    PossiblePath = 2,
    Exit = 3


class Move(IntEnum):
    Left = 0,
    Right = 1,
    Down = 2,
    Up = 3


class Position:
    x = 0
    y = 0
    path = IsPathable.PossiblePath

    def __init__(self, x, y):
        self.x = x
        self.y = y


maze = [
    "####B######################",
    "# #       #   #      #    #",
    "# # # ###### #### ####### #",
    "# # # #       #   #       #",
    "#   # # ######### # ##### #",
    "# # # #   #       #     # #",
    "### ### ### ############# #",
    "# #   #     # #           #",
    "# # #   ####### ###########",
    "# # # #       # #         C",
    "# # ##### ### # # ####### #",
    "# # #     ### # #       # #",
    "#   ##### ### # ######### #",
    "######### ### #           #",
    "# ####### ### #############",
    "A           #   ###   #   #",
    "# ############# ### # # # #",
    "# ###       # # ### # # # #",
    "# ######### # # ### # # # F",
    "#       ### # #     # # # #",
    "# ######### # ##### # # # #",
    "# #######   #       #   # #",
    "# ####### ######### #######",
    "#         #########       #",
    "#######E############D######"
]

moves_all = []


def create_move(position, move):
    global moves_all

    x = position.x
    y = position.y

    new_move = None

    # print('before:', move, 'x:', x, 'y:', y, sep=' ')
    if move == Move.Left:
        new_move = Position(x - 1, y)
    elif move == Move.Right:
        new_move = Position(x + 1, y)
    elif move == Move.Down:
        new_move = Position(x, y - 1)
    else:
        new_move = Position(x, y + 1)

    # print('after:', move, 'x:', new_move.x, 'y:', new_move.y, sep=' ')
    moves_all.append(new_move)
    return new_move


def check_position(labyrinth, x, y):
    global moves_all

    # x = столбец, y = строка
    if len(labyrinth) < y:
        return IsPathable.DeadEnd

    if len(labyrinth[y]) < x:
        return IsPathable.DeadEnd

    for move in moves_all:
        if move.x == x and move.y == y:
            return IsPathable.DeadEnd

    if labyrinth[y][x] == '#':
        return IsPathable.DeadEnd
    elif labyrinth[y][x] != ' ':
        return IsPathable.Exit
    else:
        return IsPathable.PossiblePath


def loop(labyrinth, exits, positions):
    moved = []
    for i in range(0, len(positions)):
        info = [check_position(labyrinth, positions[i].x - 1, positions[i].y),
                check_position(labyrinth, positions[i].x + 1, positions[i].y),
                check_position(labyrinth, positions[i].x, positions[i].y - 1),
                check_position(labyrinth, positions[i].x, positions[i].y + 1)]

        offset = 0
        for j in range(0, len(info)):
            if info[j] == IsPathable.PossiblePath:
                moved.append(create_move(positions[i], Move(j - offset)))
            elif info[j] == IsPathable.Exit:
                exits.append(create_move(positions[i], Move(j - offset)))
            if j % 3 == 0 and j > 0:
                offset += 3

    if len(moved) > 0:
        return loop(labyrinth, exits, moved)
    else:
        return


def calculate(labyrinth, x, y):
    result = []
    loop(labyrinth, result, [Position(x, y)])
    return result


def user_input():
    global maze

    try:
        xy = list(map(int, input('Введите x y игрока: ').split(' ')))

        if len(xy) != 2:
            raise ValueError

        x = xy[0]
        y = xy[1]

        if not 0 <= x <= len(maze[0]) or not 0 <= y <= len(maze):
            raise ValueError
        if maze[y][x] == '#':
            raise ValueError

        result = calculate(maze, x, y)

        output = []
        for i in result:
            output.append(maze[i.y][i.x])
        print(*output)

    except ValueError or TypeError:
        print('Не верные координаты')
        user_input()


if __name__ == '__main__':
    user_input()
