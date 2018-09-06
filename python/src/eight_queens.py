import math
def eight_queens():
    def check(row, col, queens):
        for r, c in enumerate(queens):
            diff = math.fabs(c - col)
            if diff == 0 or diff == row - r:
                return False
        return True
    
    def place(row, queens):
        if len(queens) < 8:
            for col in range(0, 8):
                if check(row, col, queens):
                    place(row + 1, queens + [col])
        else:
            board = [ [ '_' for j in range(0,8) ] for i in range(0,8) ]
            for r, c in enumerate(queens):
                board[r][c] = 'Q'
            for row in board:
                print(row)

    place(0, [])

eight_queens()
