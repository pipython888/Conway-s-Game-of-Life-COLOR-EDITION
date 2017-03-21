from random import randint, choice

import pygame

pygame.init()

# CONFIGURABLE VALUES

WIDTH = 500  # Screen width
HEIGHT = 500  # Screen height
CELL_SIZE = 10  # Cell size

######################


def create_grid(width, height):
    """Creates and returns a random grid."""

    grid = []
    colors = []

    for _ in range(height):
        row = []
        color_row = []
        for _ in range(width):
            row.append(randint(0, 1))
            color_row.append(choice(['Y', 'W', 'G']))
        grid.append(row)
        colors.append(color_row)

    return grid, colors


def render_grid(grid, colors):
    """Renders a grid."""

    color_dict = {
        'Y': YELLOW,
        'G': GREEN,
        'W': WHITE
    }

    x = 0
    y = 0
    for row, color_row in zip(grid, colors):
        for col, color_col in zip(row, color_row):
            if col == 1:
                pygame.draw.rect(screen, color_dict[color_col],
                                 [x, y, CELL_SIZE, CELL_SIZE])
            x += CELL_SIZE
        x = 0
        y += CELL_SIZE


# Setup

screen = pygame.display.set_mode([WIDTH, HEIGHT])

timer = pygame.time.Clock()

# Colors
YELLOW = (255, 255, 153)
WHITE = (250, 250, 250)
GREEN = (0, 250, 5)
BLACK = (0, 0, 0)

# Game Setup

grid, colors = create_grid(WIDTH // CELL_SIZE, HEIGHT // CELL_SIZE)

# Game loop
done = False
while not done:
    # Event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Display graphics
    render_grid(grid, colors)

    pygame.display.update()

    # Clear screen and tick
    screen.fill(BLACK)
    timer.tick(60)

pygame.quit()
