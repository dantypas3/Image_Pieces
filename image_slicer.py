import random
import pygame
import numpy as np

# Size of the mask in pixels
WIDTH = 600
HEIGHT = 427

grid = np.zeros((HEIGHT, WIDTH))

# Initialize pygame and create the screen widget
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill((255, 255, 255))


def draw_first_line():
    """ Creates the first line that will cut the image. Returns the start and end point of that line.
    The points of the line are on the perimeter of the image and are chosen randomly.
    """
    x, y = random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1)
    pygame.draw.line(screen, (0, 0, 0), (x, 0), (0, y), 2)

    return x, 0, 0, y


def draw_line(x_0, y_0, x1, y1,):
    """Calculates the points of the next line that will cut the image. Returns the start and end point of that line.
    The line will start at the middle of the previous line and end at a random point on the edge of the image"""

    # calculating the middle point of the previous line
    x_middle = abs((x1 + x_0))/2
    y_mean = abs((y1 + y_0))/2
    print(x_middle, y_mean)

    # choosing the edge randomly
    edge = random.choice([0, 1, 2, 3])

    # choosing the point randomly on the edge
    if edge == 0:
        x_end = random.randint(0, WIDTH - 1)
        y_end = 0
    elif edge == 1:
        x_end = WIDTH - 1
        y_end = random.randint(0, HEIGHT - 1)
    elif edge == 2:
        y_end = HEIGHT - 1
        x_end = random.randint(0, WIDTH - 1)
    else:
        x_end = 0
        y_end = random.randint(0, HEIGHT - 1)

    pygame.draw.line(screen, (0, 0, 0), (x_middle, y_mean), (x_end, y_end), 2)

    return x_middle, y_mean, x_end, y_end


terminate = False
first_line = True

x_0, y_0, x1, y1 = 0, 0, 0, 0

# main loop for the pygame
while not terminate:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate = True

        if event.type == pygame.KEYDOWN:
            # Whenever the space is pressed a new line is calculated and drawn on the screen
            if event.key == pygame.K_SPACE:
                if first_line:
                    x_0, y_0, x1, y1 = draw_first_line()
                    first_line = False
                else:
                    x_0, y_0, x1, y1 = draw_line(x_0, y_0, x1, y1)

    pygame.display.flip()
