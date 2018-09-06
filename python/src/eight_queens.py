import math
def eight_queens():

    def check(row, col, queens):
        for points in queens:
            r, c = points
            if col == c or math.fabs(row - col) == math.fabs(r - c) or row + col == r + c:
                return False
        return True

    def place(row, col, queens):
        if len(queens) < 8:
            for i in range(row, 9):
                for j in range(0, 9):
                    if check(i,j, queens):
                        place(i + 1, j, queens + [(i,j)])
        else:
            board = [ [ '_' for j in range(0,9) ] for i in range(0,9) ]
            for point in queens:
                board[ point[0] ][ point[1] ] = 'Q'
            for row in board:
                print(row)

    place(0, 0, [])

eight_queens()
