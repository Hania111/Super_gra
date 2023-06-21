import time

import pygame,random,threading

from settings import BOX_NUM,WIDTH,HEIGHT,PISTACHIO,BLACK, multiplier_for_speed, nr_pointls_for_level

#SCREEN
def init_screen():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("supi dupi game")
    return screen
def game_over():
    # Clear the SCREEN
    SCREEN.fill(PISTACHIO)  # Fill with black color

    # Add game over text
    font = pygame.font.Font(None, 64)
    text = font.render("Game Over", True, BLACK )  # White color
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    SCREEN.blit(text, text_rect)

    # Update the display
    pygame.display.flip()
    time.sleep(5)
    pygame.quit()  # Uninitialize Pygame


SCREEN = init_screen()

#helper methods
def draw_missing():
    return set(random.sample(range(BOX_NUM +1), k=2))




