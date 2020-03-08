import copy
import pygame

GREEN = (0, 255, 133)
GRAY = (123, 123, 123)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

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


def solve(grid, screen):
    empty = []

    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                empty.append([i, j])

    return helper(grid, empty, screen)

def helper(grid, empty, screen):

    if len(empty) == 0:
        return grid
    
    i, j = empty[0][0], empty[0][1]
    
    for val in range(1, 10):

        cell = createCell(val, BLACK)
        x = (70 - cell.get_rect().width) // 2
        y = (70 - cell.get_rect().height) // 2
        screen.blit(cell, (i * 71 + 1 + x, j * 71 + 3 + y))
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        
        if checkPos(grid, i, j, val) is True:

            cell = createCell(val, GREEN)
            x = (70 - cell.get_rect().width) // 2
            y = (70 - cell.get_rect().height) // 2
            screen.blit(cell, (i * 71 + 1 + x, j * 71 + 3 + y))
            pygame.display.update()

            tempGrid = copy.deepcopy(grid)
            tempGrid[i][j] = val
            
            result = helper(tempGrid, empty[1:], screen)

            if result is not False:
                return result
        
        cell = pygame.Rect(i * 71 + 1, j * 71 + 1, 70, 70)
        pygame.draw.rect(screen, GRAY, cell)

    return False

# debug printer
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

def gridInput(grid):
    for i in range(9):
        grid[i] = [int(n) for n in input().split()]

# like p5.map
def mapClick(n):
  return int((n / 640) * 9)

def createCell(number, color):
    font = pygame.font.Font(None, 65)
    numSurface = font.render(str(number), True, color)
    return numSurface


def main():
    pygame.init()

    width, height = 640, 640

    # main window setup
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Sudoku solver')
    icon = pygame.image.load('logo.png')
    pygame.display.set_icon(icon)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(WHITE)

    screen.blit(background, (0, 0))

    # drawing the grid
    for y in range(1, 640, 71):
        for x in range(1, 640, 71):
            cell = pygame.Rect(x, y, 70, 70)
            pygame.draw.rect(screen, GRAY, cell)

    # reading sudoku from file
    grid = [[0] * 9 for _ in range(9)]
    gridInput(grid)

    # drawing centered numbers
    color = (20, 20, 123)
    for row in range(9):
        for col in range(9):
            if grid[row][col] != 0:
                cell = createCell(grid[row][col], color)
                x = (70 - cell.get_rect().width) // 2
                y = (70 - cell.get_rect().height) // 2
                screen.blit(cell, (row * 71 + 1 + x, col * 71 + 3 + y))

    pygame.display.flip()

    solved = solve(grid, screen)


    # main loop
    running = True
    while running is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.update()

    # printing result
    if solved is not False:
        print("Sudoku solved successfully")
    else:
        print("Unable to solve")


if __name__ == '__main__': main()

