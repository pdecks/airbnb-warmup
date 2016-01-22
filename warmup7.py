"""You are given a 2D array with M rows and N volumns. You are initally
positioned at (0,0), the top-left cell in the array. You are allowed to move
either right or downwards. The array is filled with 1's and 0's. A 1 indicates
that you can move through that cell, a 0 indicates that you cannot move through
the cell.

Given a function numberOfPaths which takes in the above 2D array, return the
number of paths from the top-left cell to the bottom-right cell (M-1, N-1).

Since the answer can be large, return the number % 1,000,000,007.

1 <= N, M <= 1,000.

For an unblocked matrix, the total number of ways in which one can travel from top-left to bottom-right in (M+1)x(N+1) matrix is equivalent to arrangement of M DOWN arrows and N RIGHT arrows. The formula for which is (M+N)!/M!N!.
"""

from math import factorial as fac

FREE = 0
BLOCKED = 1

# def numberOfPaths(matrix):
#     M = len(matrix)
#     N = len(matrix[0])

# Total paths
def free_path(start, end):
    """Given start and end coords, calculate the total number of paths, assuming
    all entries are unblocked --> (m + n)! / (m! * n!)
    where m = num rows, n = num cols
    and start and end are tuples of the form (row pos, col pos)"""
    # num rows
    m = end[0] - start[0]
    # num cols
    n = end[1] - start[1]
    return fac(m + n) / (fac(m) * fac(n))


# unblocked paths
def available_path(start, end, matrix):
    """Considering blockages, find the total number of paths"""
    total = free_path(start, end)

    # if origin is blocked, no possible paths
    if matrix[start[0]][start[1]] == BLOCKED:
        return 0
    
    # placeholder for current coordinates
    temp = [0, 0]

    for row in range(start[0], end[0] + 1):
        for col in range(start[1], end[1] + 1):
            temp[0] = row
            temp[1] = col
            total -= free_path(start, temp) * available_path(temp, end, matrix)
            # !!! Hitting max recursive depth because temp always resets to 0,0
    return total


def initialize_matrix(m, n):
    """Initialize mxn matrix with all FREE cells."""
    matrix = []
    for i in range(m):
        curr_row = []
        for j in range(n):
            curr_row.append(0)
        matrix.append(curr_row)

    return matrix


def block_entry(r, c, matrix):
    """Block a specific entry."""
    matrix[r][c] = BLOCKED

    return matrix


def main():
    m = 2
    n = 2

    # create an MxN matrix
    matrix = initialize_matrix(m, n)   
    
    # define start and end coordinates
    start = [0, 0]
    end = [m - 1, n - 1]
    
    # block a set of entries
    # matrix = block_entry(1, 1, matrix)
    # matrix = block_entry(2, 1, matrix)

    print available_path(start, end, matrix)
    
    return

main()