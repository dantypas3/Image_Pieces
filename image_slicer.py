import random
import pygame
import numpy as np
import sys


def pieces(n_pieces, width, height, screen):
    points = []

    while not points:
        x_0, y_0, x1, y1 = [None]*4
        touching = 0
        lines = 0
        slices = 1
        while slices != n_pieces:
            x_0, y_0, x1, y1 = draw_line(width, height, screen,  x_0, y_0, x1, y1)
            lines += 1
            points.append([x_0, y_0, x1, y1])

            if lines > 2:
                for i in range(lines, 2):
                    x_0i, y_0i, x1i, y1i = points[i]
                    x_0i, x1i = sorted([x_0i, x1i])
                    y_0i, y1i = sorted([y_0i, y1i])
                    for j in range(lines - i):
                        x_0j, y_0j, x1j, y1j = points[j]
                        x_0j, x1j = sorted([x_0j, x1j])
                        y_0j, y1j = sorted([y_0j, y1j])

                        if x1i < x_0j or x_0i > x1j or y1i < y_0j or x_0i > y1j:
                            break
                        else:
                            if x_0i < (x_0j + x1j)/2 < x1i and y_0i < (y_0j + y1j)/2 < y1i:
                                pass



            slices = 1 + lines + touching

        if points:
            break
        else:
            points = []


    return points


def draw_line(width, height, screen, x_0=None, y_0=None, x1=None, y1=None):
    """Calculates the points of the next line that will cut the image. Returns the start and end point of that line.
    The line will start at the middle of the previous line and end at a random point on the edge of the image"""

    if x_0:

        # calculating the middle point of the previous line
        x_middle = abs((x1 + x_0))/2
        y_mean = abs((y1 + y_0))/2

        # choosing the edge randomly
        edge = random.choice([0, 1, 2, 3])

        # choosing the point randomly on the edge
        if edge == 0:
            x_end = random.randint(0, width - 1)
            y_end = 0
        elif edge == 1:
            x_end = width - 1
            y_end = random.randint(0, height - 1)
        elif edge == 2:
            y_end = height - 1
            x_end = random.randint(0, width - 1)
        else:
            x_end = 0
            y_end = random.randint(0, height - 1)

        pygame.draw.line(screen, (0, 0, 0), (x_middle, y_mean), (x_end, y_end), 2)

        return x_middle, y_mean, x_end, y_end

    else:
        x, y = random.randint(0, width - 1), random.randint(0, height - 1)
        pygame.draw.line(screen, (0, 0, 0), (x, 0), (0, y), 2)

        return x, 0, 0, y


def main(n_lines):

    # Size of the mask in pixels
    WIDTH = 600
    HEIGHT = 450
    WHITE = (255, 255, 255)

    grid = np.zeros((HEIGHT, WIDTH))

    # Initialize pygame and create the screen widget
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    screen.fill(WHITE)

    terminate = False

    x_0, y_0, x1, y1 = [None]*4

    drawn = False

    # main loop for the pygame
    while not terminate:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    screen.fill(WHITE)
                    drawn = False
                    x_0, y_0, x1, y1 = [None]*4

        while not drawn:
            for i in range(n_lines):
                x_0, y_0, x1, y1 = draw_line(WIDTH, HEIGHT, screen,  x_0, y_0, x1, y1)
            drawn = True

        pygame.display.flip()


if __name__ == "__main__":
    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python image_slicer.py 5")

    if sys.argv[1].isnumeric():
        lines = int(sys.argv[1])
        if lines >= 0:
            main(lines)
        else:
            raise ValueError("Enter positive number of lines")
    else:
        raise ValueError("Enter correct number of lines")
