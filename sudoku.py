grid = [[0] * 9 for _ in range(9)]  # main sudoku grid

# grid[row][col]

def checkPos(grid, row, col, val):
    for i in range(9):
        if grid[i][col] == val:
            return False
    
    for i in range(9):
        if grid[row][i] == val:
            return False

    startCol = col // 3
    startRow = row // 3

    for i in range(startRow, startRow + 3):
        for j in range(startCol, startCol + 3):
            if grid[i][j] == val:
                return False

    return True


def solve(grid):
    pass



def printGrid(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end = ' ')
            if j == 2 or j == 5:
                print("|", end = ' ')
        print()
        if i == 2 or i == 5:
            for _ in range(21):
                print("-", end = '')
            print()

for i in range(9):
    grid[i] = [int(n) for n in input().split()]


printGrid(grid)