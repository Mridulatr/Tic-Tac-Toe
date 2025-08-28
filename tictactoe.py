import random
import utils
import sys
import minimax
from copy import deepcopy
import timeit

def getMove(board, playerID, playerAlgo):
    if playerAlgo == "random_ai":
        return randomAI(board, playerID)
    elif playerAlgo == "finds_own_winning_move_ai":
        return findsOwnWinningMoveAI(board, playerID)
    elif playerAlgo == "finds_all_winning_moves_ai":
        return findsWinningAndLosingMovesAI(board, playerID)
    elif playerAlgo == "human_player":
        return  humanPlayer(board, playerID)
    elif playerAlgo == "minimax_ai":
        return minimax.miniMaxAI(board, playerID)
    else:
        raise Exception("Unknown algorithm, Try again!!!")


def makeMove(board, coords, player):
    x, y = coords
    updatedBoard = deepcopy(board)
    if updatedBoard[x][y] is not None:
        raise Exception(f"Illegal move ({x}, {y}) square already taken")
    updatedBoard[x][y] = player
    return updatedBoard

def getWinner(board):
    lineCoords = utils.getLines()
    for line in lineCoords:
        lineValues = [board[x][y] for (x, y) in line]
        if len(set(lineValues)) == 1 and lineValues[0]:
            return lineValues[0]
    return None


def checkDraw(board):
    for x in range(3):
        for y in range(3):
            # There is atleast one None value inside the board
            if not board[x][y]: 
                return False
    return True

def randomAI(board, player):
    legalCoords = []
    for x in range(3):
        for y in range(3):
            if not board[x][y]:
                legalCoords.append((x, y))
    return random.choice(legalCoords)

def findsWinningMoveAI(board, player): 
    # Returns the winning move if any else return None
    lineCoords = utils.getLines()
    for line in lineCoords:
        nPlayer = 0 # number of cells occupied by current player
        nEmpty = 0 # number of empty cells in the current line
        lastEmpty = None # last empty coordinate in the line
        for (x, y) in line:
            if board[x][y] == player:
                nPlayer += 1
            elif not board[x][y]:
                nEmpty += 1
                lastEmpty = (x, y)
        if nPlayer == 2 and nEmpty == 1:
            return lastEmpty
    return None


def findsOwnWinningMoveAI(board, player):
    # Returns the winning move if any else return random move
    wMove = findsWinningMoveAI(board, player)
    if wMove:
        return wMove
    return randomAI(board, player)


def findsWinningAndLosingMovesAI(board, player):
    wMove = findsWinningMoveAI(board, player)
    if wMove:
        return wMove
    oppWMove = findsWinningMoveAI(board, utils.getOpponent(player))
    if oppWMove:
        return oppWMove
    
    return randomAI(board, player)

def humanPlayer(board, player):
    x = int(input(f"{player}, What's your X-coordinate: "))
    y = int(input(f"{player}, What's your Y-coordinate: "))
    return (x, y)

def play(player1, player2):
    players = [("X", player1), ("O", player2)]
    playerMap = {"X": player1, "O" : player2}
    turn = 0
    board = utils.newBoard()
    while True:
        utils.render(board)
        ID, name = players[turn % 2]
        moveCoords = getMove(board, ID, name)
        board = makeMove(board, moveCoords, ID)
        if getWinner(board):
            utils.render(board)
            print(f"{name}-{ID}, wins!!!")
            # return 1 if ID == "X" else 2
            break
        if checkDraw(board):
            utils.render(board)
            print("Game ends in a draw")
            # return 0
            break
        turn += 1

# def repeatedBattle(player1, player2):
#     p1Wins, p2Wins, draws = 0, 0, 0
#     for i in range(1000):
#         n = play(player1, player2)
#         if n == 1:
#             p1Wins += 1
#         elif n == 2:
#             p2Wins += 1
#         else:
#             draws += 1
#     print(f"{player1} win percentage is {(p1Wins / 1000) * 100}%")
#     print(f"{player2} win percentage is {(p2Wins / 1000) * 100}%")
#     print(f"Number of draws = {draws}")


# repeatedBattle("random_ai", "random_ai")


if __name__ == "__main__":
    import sys

    if len(sys.argv) >= 3:
        player1 = sys.argv[1]
        player2 = sys.argv[2]
    else:
        print("No command-line arguments provided, entering interactive mode.")
        player1 = input("Enter Player 1 algorithm (random_ai, human_player, etc.): ")
        player2 = input("Enter Player 2 algorithm (random_ai, human_player, etc.): ")

    play(player1, player2)
