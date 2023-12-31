import pygame
import numpy as np
import time

pygame.init()

width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Conway's Game of Life")

black = 0, 0, 0
white = 255, 255, 255

rows, cols = 60, 60
grid = np.random.choice([0, 1], size=(rows, cols))

cell_size = width // cols, height // rows

def update_grid(grid):
    new_grid = grid.copy()

    for i in range(rows):
        for j in range(cols):
     
            neighbors = (
                grid[i - 1 : i + 2, j - 1 : j + 2].sum() - grid[i, j]
            )

            if grid[i, j] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[i, j] = 0
            elif grid[i, j] == 0 and neighbors == 3:
                new_grid[i, j] = 1

    return new_grid

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    grid = update_grid(grid)

    screen.fill(black)
    for i in range(rows):
        for j in range(cols):
            color = white if grid[i, j] == 1 else black
            pygame.draw.rect(
                screen,
                color,
                (j * cell_size[0], i * cell_size[1], cell_size[0], cell_size[1]),
            )

    pygame.display.flip()

    time.sleep(0.1)

pygame.quit()
