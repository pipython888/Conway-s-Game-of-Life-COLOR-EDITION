from random import randint, choice
from time import sleep

import pygame

pygame.init()

# Configurable Values
WIDTH = 1000  # Screen width
HEIGHT = 1000  # Screen height
CELL_SIZE = 20  # Cell size
COLOR_ON = True  # Toggle Color Edition
TIME_PER_FRAME = 0.1  # The amount of seconds you should wait between each frame
OUTLINE = 8  # If zero, all cells will be filled. If any other value, will draw outlined rectangle.


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
            color_row.append(choice(list(COLOR_DICT.keys())))
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
                color = COLOR_DICT[color_col] if COLOR_ON else GREEN
                pygame.draw.rect(screen, color, [x, y, CELL_SIZE - OUTLINE, CELL_SIZE - OUTLINE], OUTLINE)
            x += CELL_SIZE
        x = 0
        y += CELL_SIZE


def count_neighbors(grid, row, col):
    """Counts the amount of neighbors around a cell."""

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


def get_color(colors, row, col):
    """Gets the color a newcomer cell should be."""

    neighbor_colors = []

    # Horizantal and Vertical Neighbors
    neighbor_colors.append(index(index(colors, row + 1), col))
    neighbor_colors.append(index(index(colors, row - 1), col))
    neighbor_colors.append(index(index(colors, row), col - 1))
    neighbor_colors.append(index(index(colors, row), col + 1))

    # Diagonal Neighbors
    neighbor_colors.append(index(index(colors, row + 1), col + 1))
    neighbor_colors.append(index(index(colors, row - 1), col - 1))
    neighbor_colors.append(index(index(colors, row - 1), col + 1))
    neighbor_colors.append(index(index(colors, row + 1), col - 1))

    colors_with_quantities = {}

    for color in neighbor_colors:
        try:
            colors_with_quantities[color] += 1
        except KeyError:
            colors_with_quantities[color] = 1

    result = ""
    result_amount = 0
    for color, amount in colors_with_quantities.items():
        if amount > result_amount:
            result = color
            result_amount = amount
        if amount == result_amount:
            result = choice([result, color])
            result_amount = amount

    return result


def update_grid(grid, colors):
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
    new_colors = []

    for row_idx, row in enumerate(grid):
        new_row = []
        new_color_row = []
        for col_idx, col in enumerate(row):
            neighbors = count_neighbors(grid, row_idx, col_idx)
            if col == 1 and (neighbors > 3 or neighbors < 2):
                new_row.append(0)
                new_color_row.append(get_color(colors, row_idx, col_idx))
            elif col == 0 and neighbors == 3:
                new_row.append(1)
                new_color_row.append(colors[row_idx][col_idx])
            elif col == 0 or col == 1:
                new_row.append(col)
                new_color_row.append(colors[row_idx][col_idx])
            else:
                raise ValueError("Invalid grid")
        new_grid.append(new_row)
        new_colors.append(new_color_row)

    return new_grid, new_colors


def main():
    """The game loop and game setup"""

    global COLOR_ON

    grid, colors = create_grid(WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE)

    paused = False

    done = False
    while not done:
        # Event handlers
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    grid, colors = create_grid(WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE)

                if event.key == pygame.K_c:
                    COLOR_ON = not COLOR_ON

                if event.key == pygame.K_SPACE:
                    paused = not paused

                if event.key == pygame.K_RIGHT and paused:
                    grid, colors = update_grid(grid, colors)

        # Display graphics
        render_grid(grid, colors)

        pygame.display.update()

        if not paused:
            grid, colors = update_grid(grid, colors)

        # Clear screen and tick
        screen.fill(BLACK)
        timer.tick(20)
        sleep(TIME_PER_FRAME)


# Setup

screen = pygame.display.set_mode([WIDTH, HEIGHT])

timer = pygame.time.Clock()

# Colors
YELLOW = 255, 255, 153
WHITE = 250, 250, 250
GREEN = 0, 250, 5
BLUE = 100, 200, 255
RED = 255, 100, 50
DARK_BLUE = 40, 120, 180
DARK_GREEN = 70, 150, 40
BLACK = 0, 0, 0

COLOR_DICT = {
    'Y': YELLOW,
    'G': GREEN,
    'W': WHITE,
    'B': BLUE,
    'R': RED,
    'DB': DARK_BLUE,
    'DG': DARK_GREEN
}

pygame.display.set_caption("Conway's Game of Life Color Edition")

if __name__ == '__main__':
    main()

pygame.quit()
