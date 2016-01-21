"""Write a function to print out a matrix (n x m) in spiral order."""

def spiral_print(matrix):
    """Takes a matrix as a list of lists of size n x m, prints values in CW
    spiral order

    n = num rows, m = num cols
    direction: 0 first row, 1 last col, 2 last row, 3 first col
    """
    direction = 0
    result = ''
    while matrix:
        n = len(matrix)
        m = len(matrix[0])
        
        action = direction % 4
        
        if action == 0:
            # print first row
            for item in matrix[0]:
                # print item
                result = result + str(item) + ','
            # new matrix lops off first row
            matrix = matrix[1:]
        
        elif action == 1:
            # print last col
            for row in matrix:
                # print row[-1]
                result = result + str(row[-1]) + ','
            # new matrix lops off last col
            new_matrix = []
            for row in matrix:
                new_row = row[:-1]
                new_matrix.append(new_row)
            matrix = new_matrix

        elif action == 2:
            # print last row, in reverse order
            row = matrix[-1]
            for i in range(-1, -1 * len(row) - 1, -1):
                # print row[i]
                result = result + str(row[i]) + ','
            # new matrix lops off last row
            matrix = matrix[:-1]

        else: # action == 3
            # print first col, in reverser order
            for i in range(-1, -1 * len(matrix) - 1, -1):
                # print matrix[i][0]
                result = result + str(matrix[i][0]) + ','
            # new matrix lops off first col
            new_matrix = []
            for row in matrix:
                new_row = row[1:]
                new_matrix.append(new_row)
            matrix = new_matrix
                
        direction += 1
    
    # strip off final comma
    print result[:-1]
    return 

    # 0
# parse input
n, m = map(int,raw_input().strip().split(','))

matrix = []
for i in range(n):
    row = map(int,raw_input().strip().split(','))
    matrix.append(row)

spiral_print(matrix)

