import utils
import tictactoe as engine

def miniMaxScore(board, playerToMove, playerToOptimise):
    winner = engine.getWinner(board)
    if winner:
        if winner == playerToOptimise:
            return 10
        else:
            return -10
    elif engine.checkDraw(board):
        return 0

    legalMoves = utils.legalMoves(board)
    scores = []

    for move in legalMoves:
        newBoard = engine.makeMove(board, move, playerToMove)
        opponent = utils.getOpponent(playerToMove)
        score = miniMaxScore(newBoard, opponent, playerToOptimise)
        scores.append(score)
    
    if playerToMove == playerToOptimise:
        return max(scores)

    else:
        return min(scores)


# Returns the best move for the miniMaxAI
def miniMaxAI(board, player):
    bestMove, bestScore = None, None
    legalMoves = utils.legalMoves(board)

    for move in legalMoves:
        newBoard = engine.makeMove(board, move, player)
        score = miniMaxWithCache(newBoard, utils.getOpponent(player), player)
        if bestScore is None or score > bestScore:
            bestScore = score
            bestMove = move
    return bestMove


cache = {}
def miniMaxWithCache(board, playerToMove, playerToOptimise):
    boardCacheKey = str(board)
    if boardCacheKey not in cache:
        score = miniMaxScore(board, playerToMove, playerToOptimise)
        cache[boardCacheKey] = score
    return cache[boardCacheKey]