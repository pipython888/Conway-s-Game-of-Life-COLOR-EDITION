import pygame

pygame.init()

#### CONFIGUREABLE VALUES ####

WIDTH = 500  # Screen width
HEIGHT = 500  # Screen height
CELL_SIZE = 10  # Cell size

##############################

# Setup

screen = pygame.display.set_mode([WIDTH, HEIGHT])

timer = pygame.time.Clock()

# Colors
YELLOW = (255, 255, 153)
WHITE = (250, 250, 250)
GREEN = (0, 250, 5)
BLACK = (0, 0, 0)

# Game loop
done = False
while not done:
    # Event handlers
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # Display graphics
    pygame.display.update()

    # Clear screen and tick
    screen.fill(BLACK)
    timer.tick(60)

pygame.quit()
