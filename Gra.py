import pygame
import sys, threading
from utils import create_box_wall,SCREEN,game_over
from settings import WIDTH, HEIGHT, FPS, LIGHT_PISTACHIO, BLACK,SPEED
import Player
from sprite_actions import player_boxes_collision

pygame.init()

font = pygame.font.Font(None, 36)

player = Player.Player()
player.score = 100

# Create a group for all sprites
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Create the initial wall of boxes
boxes = create_box_wall()  # Add each individual box sprite to the group


running =True
while running:
    # Częstotliwość odświeżania ekranu
    pygame.time.Clock().tick(FPS)

    # Obsługa zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Aktualizacja
    all_sprites.update()
    boxes.update()
    #walls.update()
    player_boxes_collision(player, boxes)

    if len(boxes) ==0:
        boxes = create_box_wall()


    # Rysowanie
    SCREEN.fill(LIGHT_PISTACHIO)
    # Rysowanie ścian
    #walls.draw(SCREEN)
    boxes.draw(SCREEN)
    all_sprites.draw(SCREEN)



    # rydowanie metryki
    text_surface = font.render("Score: " + str(player.score), True, BLACK)
    SCREEN.blit(text_surface, (WIDTH - text_surface.get_width() - 20, 0))
    text_surface = font.render("Speed: " + str(SPEED), True, BLACK)
    SCREEN.blit(text_surface, (WIDTH - text_surface.get_width() - 20, text_surface.get_height() + 10))

    # Wyświetlanie zmian
    pygame.display.flip()

# Zamknięcie programu
pygame.quit()
sys.exit()



