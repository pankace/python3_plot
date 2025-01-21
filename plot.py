import pygame
import math
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()
logger.info("Program started")

def f(x):
    return math.sin(x)

pygame.init()

w = 600
h = 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Graph of y = sin(x)")

interval = (-6, 6) #x
scale_x = w / (interval[1] - interval[0])
scale_y = h / 2

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    pygame.draw.line(screen, (255, 255, 255), (0, h // 2), (w, h // 2))  # X
    pygame.draw.line(screen, (255, 255, 255), (w // 2, 0), (w // 2, h))  # Y

    for x_pixel in range(w):
        x = interval[0] + (x_pixel / scale_x)
        y = f(x)
        screen_x = x_pixel
        screen_y = h // 2 - int(y * scale_y)
        if 0 <= screen_x < w and 0 <= screen_y < h:
            screen.set_at((screen_x, screen_y), (0, 255, 0))

    pygame.display.flip()

pygame.quit()
logger.info("Program terminated")
