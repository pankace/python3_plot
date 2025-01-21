import pygame
import logging

logging.basicConfig(level=logging.INFO)

logger = logging.getLogger()
logger.info("Program started")

def f(x):
    return x  # Function to plot y = x

# Initialize pygame
pygame.init()

# Set up the display
w = 600
h = 600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("Graph of y = x")

running = True

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the axes
    pygame.draw.line(screen, (255, 255, 255), (0, h // 2), (w, h // 2))  # X-axis
    pygame.draw.line(screen, (255, 255, 255), (w // 2, 0), (w // 2, h))  # Y-axis

    # Plot the function y = x
    for x in range(-w // 2, w // 2):
        y = f(x)
        # Scale and translate points to the middle of the screen
        screen_x = x + w // 2
        screen_y = h // 2 - y
        # Draw the point if it is within the screen boundaries
        if 0 <= screen_x < w and 0 <= screen_y < h:
            screen.set_at((screen_x, screen_y), (0, 255, 0))

    # Update the display
    pygame.display.flip()

pygame.quit()
logger.info("Program terminated")
