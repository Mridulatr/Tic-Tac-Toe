import timeit
from minimax import miniMaxAI, miniMaxWithCache
import tictactoe as engine


board = [[None, None, None], [None, None, None], [None, None, None]]
player = "X"


def run_with_caching():
    # cache.clear()  # Clear cache to ensure fresh start for each measurement
    return miniMaxWithCache(board, player, player)


def run_without_caching():
    # cache.clear()  # Ensure the cache does not impact this function
    return miniMaxAI(board, player)


# Measure the performance with caching
time_with_caching = timeit.timeit(run_with_caching, number=5)

# Measure the performance without caching
time_without_caching = timeit.timeit(run_without_caching, number=5)

print(f"Time with caching: {time_with_caching} seconds per execution")
print(f"Time without caching: {time_without_caching} seconds per execution")