import pygame
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()
logger.info("Program started")

def f(x):
    return x**2  # Function to plot y = x^2

pygame.init()

w = 600
h = 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Graph of y = x^2")

interval = (-2, 2)
scale_x = w / (interval[1] - interval[0])
scale_y = h / 4
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    pygame.draw.line(screen, (255, 255, 255), (0, h // 2), (w, h // 2))  # X-axis
    pygame.draw.line(screen, (255, 255, 255), (w // 2, 0), (w // 2, h))  # Y-axis

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
