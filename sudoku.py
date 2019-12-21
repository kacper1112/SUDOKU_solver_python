import copy

grid = [[0] * 9 for _ in range(9)]  # main sudoku grid

# grid[row][col]
# grid[ i ][ j ]

def checkPos(grid, row, col, val):
    for i in range(9):
        if grid[i][col] == val:
            return False
    
    for i in range(9):
        if grid[row][i] == val:
            return False

    startCol = col // 3
    startRow = row // 3

    #print(startCol * 3, startCol * 3 + 3)
    #print(startRow * 3, startRow * 3 + 3)

    for i in range(startRow * 3, startRow * 3 + 3):
        for j in range(startCol * 3, startCol * 3 + 3):
            if grid[i][j] == val:
                return False

    return True


def solve(grid):
    empty = []

    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                empty.append([i, j])

    return helper(grid, empty)

def helper(grid, empty):

    if len(empty) == 0:
        return grid
    
    i, j = empty[0][0], empty[0][1]
    
    for val in range(1, 10):
        if checkPos(grid, i, j, val) is True:
            tempGrid = copy.deepcopy(grid)
            tempGrid[i][j] = val
            
            result = helper(tempGrid, empty[1:])

            if result is not False:
                return result

    return False

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

solved = solve(grid)

if solved is not False:
    printGrid(solved)
else:
    print("Unable to solve")
