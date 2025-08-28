def newBoard():
    board = [[None] * 3 for i in range(3)]
    return board


def render(board):
    print("  0", "1", "2")
    print("  -----")
    for r in range(len(board)):
        print(r, "|", end="")
        for c in range(len(board[r])):
            if board[r][c] is None:
                print(" ", end="")
            else:
                print(board[r][c], end="")
        print("|")

    print("  -----")


def getOpponent(player):
    if player == "X":
        return "O"
    elif player == "O":
        return "X"


def getLines():
    cols = []
    for x in range(3):
        col = []
        for y in range(3):
            col.append((x, y))
        cols.append(col)

    rows = []
    for y in range(3):
        row = []
        for x in range(3):
            row.append((x, y))
        rows.append(row)

    diagonals = [[(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]

    return rows + cols + diagonals

def legalMoves(board):
    legalCoords = []
    for x in range(3):
        for y in range(3):
            if not board[x][y]:
                legalCoords.append((x, y))
    return legalCoords