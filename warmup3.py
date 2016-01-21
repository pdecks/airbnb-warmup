"""Write a function to print out a matrix (n x m) in spiral order."""

def spiral_print(matrix):
    """Takes a matrix as a list of lists of size n x m, prints values in CW
    spiral order

    n = num rows, m = num cols
    direction: 0 first row, 1 last col, 2 last row, 3 first col
    """
    direction = 0
    while matrix:
        n = len(matrix)
        m = len(matrix[0])
        
        action = direction % 4
        
        if action == 0:
            # print first row
            for item in matrix[0]:
                print item
            # new matrix lops off first row
            matrix = matrix[1:]
        
        elif action == 1:
            # print last col
            for row in matrix:
                print row[-1]
            # new matrix lops off last col
            new_matrix = []
            for row in matrix:
                new_row = row[:-1]
                new_matrix.append(new_row)
            matrix = new_matrix

        elif action == 2:
            # print last row, in reverse order
            row = matrix[-1]
            for i in range(-1, -1 * len(row) - 1, -1)
                print row[i]
            # new matrix lops off last row
            matrix = matrix[:-1]
            
        else: # action == 3

        direction += 1
        
        # make new matrix

    # 0
# parse input
n, m = map(int,raw_input().strip().split(','))

matrix = []
for i in range(n):
    row = map(int,raw_input().strip().split(','))
    matrix.append(row)

