import sys
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS

def main():
    # Geeral setup 
    pygame.init()

    # Set up display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris")

    # Game loop
    running = True
    clock = pygame.time.Clock()
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
    
    pygame.quit()


if __name__ == "__main__":
    main()