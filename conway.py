from random import randint, choice

import pygame

pygame.init()

# Configurable Values
WIDTH = 500  # Screen width
HEIGHT = 500  # Screen height
CELL_SIZE = 10  # Cell size


def index(L, idx):
    return L[idx % len(L)]


def create_grid(width, height):
    """Creates and returns a random grid."""

    result_grid = []
    result_colors = []

    for _ in range(height):
        row = []
        color_row = []
        for _ in range(width):
            row.append(randint(0, 1))
            color_row.append(choice(['Y', 'W', 'G']))
        result_grid.append(row)
        result_colors.append(color_row)

    return result_grid, result_colors


def render_grid(grid, colors):
    """Renders a grid."""

    x = 0
    y = 0
    for row, color_row in zip(grid, colors):
        for col, color_col in zip(row, color_row):
            if col == 1:
                pygame.draw.rect(screen, COLOR_DICT[color_col],
                                 [x, y, CELL_SIZE, CELL_SIZE])
            x += CELL_SIZE
        x = 0
        y += CELL_SIZE


def count_neighbors(grid, row, col):
    neighbors = 0

    # Horizantal and Vertical Neighbors
    neighbors += index(index(grid, row + 1), col)
    neighbors += index(index(grid, row - 1), col)
    neighbors += index(index(grid, row), col - 1)
    neighbors += index(index(grid, row), col + 1)

    # Diagonal Neighbors
    neighbors += index(index(grid, row + 1), col + 1)
    neighbors += index(index(grid, row - 1), col - 1)
    neighbors += index(index(grid, row - 1), col + 1)
    neighbors += index(index(grid, row + 1), col - 1)

    return neighbors


def update_grid(grid):
    """Updates the grid, following the rules of Conway's Game of Life.

    - If there are any ON cells with over 3 neighbors, they turn OFF.
    - If there are any ON cells with under 2 neighbors, they turn OFF.
    - If there are any ON cells with 2 or 3 neighbors, they stay ON.
    - If there are any OFF cells with EXACTLY 3 neihgbors, they turn ON.

    Also, to make the simulation interesting, I am adding these rules to decide color:

    - Color is decided when an OFF cell turns ON. Cells doesn't change color until they
    turn OFF.
    - When a cell is turning ON, the most common color among the neighbors are used.
    - If there's a tie on colors among the neighbors, pick random."""

    new_grid = []

    for row_idx, row in enumerate(grid):
        new_row = []
        for col_idx, col in enumerate(row):
            neighbors = count_neighbors(grid, row_idx, col_idx)
            if col == 1 and (neighbors > 3 or neighbors < 2):
                new_row.append(0)
            elif col == 0 and neighbors == 3:
                new_row.append(1)
            elif col == 0 or col == 1:
                new_row.append(col)
            else:
                raise ValueError("Invalid grid")
        new_grid.append(new_row)

    return new_grid


def main():
    """The game loop and game setup"""

    grid, colors = create_grid(WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE)

    done = False
    while not done:
        # Event handlers
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # Display graphics
        render_grid(grid, colors)

        pygame.display.update()

        grid = update_grid(grid)

        # Clear screen and tick
        screen.fill(BLACK)
        timer.tick(5)


# Setup

screen = pygame.display.set_mode([WIDTH, HEIGHT])

timer = pygame.time.Clock()

# Colors
YELLOW = (255, 255, 153)
WHITE = (250, 250, 250)
GREEN = (0, 250, 5)
BLACK = (0, 0, 0)

COLOR_DICT = {
    'Y': YELLOW,
    'G': GREEN,
    'W': WHITE
}

pygame.display.set_caption("Conway's Game of Life Color Edition")

if __name__ == '__main__':
    main()

pygame.quit()
