#pylint: disable=too-many-function-args
#pylint: disable=no-member
""" Kacper Stysinski """
from copy import deepcopy
import pygame

GREEN = (0, 255, 133)
GRAY = (123, 123, 123)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def check_pos(grid, row, col, val):
    """ check whether a value can be inserted into given cell """
    for i in range(9):
        if grid[i][col] == val:
            return False

    for i in range(9):
        if grid[row][i] == val:
            return False

    start_col = col // 3
    start_row = row // 3

    for i in range(start_row * 3, start_row * 3 + 3):
        for j in range(start_col * 3, start_col * 3 + 3):
            if grid[i][j] == val:
                return False

    return True

def solve(grid, screen):
    """ main solver function """
    empty = []

    for j in range(9):
        for i in range(9):
            if grid[i][j] == 0:
                empty.append([i, j])

    return helper(grid, empty, screen)

def helper(grid, empty, screen):
    """ recursive solver """

    if not empty:
        return grid

    i, j = empty[0][0], empty[0][1]

    for val in range(1, 10):

        cell = create_cell(val, BLACK)
        cell_x = (70 - cell.get_rect().width) // 2
        cell_y = (70 - cell.get_rect().height) // 2
        screen.blit(cell, (i * 71 + 1 + cell_x, j * 71 + 3 + cell_y))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        if check_pos(grid, i, j, val) is True:

            cell = create_cell(val, GREEN)
            cell_x = (70 - cell.get_rect().width) // 2
            cell_y = (70 - cell.get_rect().height) // 2
            screen.blit(cell, (i * 71 + 1 + cell_x, j * 71 + 3 + cell_y))
            pygame.display.update()

            temp_grid = deepcopy(grid)
            temp_grid[i][j] = val

            result = helper(temp_grid, empty[1:], screen)

            if result is not False:
                return result

        cell = pygame.Rect(i * 71 + 1, j * 71 + 1, 70, 70)
        pygame.draw.rect(screen, GRAY, cell)

    return False

def print_grid(grid):
    """ debug printer """
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=' ')
            if j in (2, 5):
                print("|", end=' ')
        print()
        if i in (2, 5):
            for _ in range(21):
                print("-", end='')
            print()

def grid_input(grid):
    """ read known grid values """
    for i in range(9):
        grid[i] = [int(n) for n in input().split()]

def create_cell(number, color):
    """ create surface of a cell with a number  """
    font = pygame.font.Font(None, 65)
    num_surface = font.render(str(number), True, color)
    return num_surface

def main():
    """ main function """
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
    for j in range(1, 640, 71):
        for i in range(1, 640, 71):
            cell = pygame.Rect(i, j, 70, 70)
            pygame.draw.rect(screen, GRAY, cell)

    # reading sudoku from file
    grid = [[0] * 9 for _ in range(9)]
    grid_input(grid)

    # drawing centered numbers
    color = (20, 20, 123)
    for j in range(9):
        for i in range(9):
            if grid[j][i] != 0:
                cell = create_cell(grid[j][i], color)
                cell_x = (70 - cell.get_rect().width) // 2
                cell_y = (70 - cell.get_rect().height) // 2
                screen.blit(cell, (j * 71 + 1 + cell_x, i * 71 + 3 + cell_y))

    pygame.display.flip()

    # solving sudoku
    if solve(grid, screen) is not False:
        print("Sudoku solved successfully")
    else:
        print("Unable to solve")

    # main loop
    running = True
    while running is True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    # printing result


if __name__ == '__main__':
    main()
