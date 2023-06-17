import pygame
import sys
from settings import speed
from Box import create_box_wall

from settings import WIDTH, HEIGHT, FPS, LIGHT_PISTACHIO, BLACK
from Player import Player

from Wall import updateWalls
from Apple import updateApples

from utils import SCREEN
from sprite_actions import player_boxes_collision, player_walls_collision, player_apples_collision



def main_game_loop():
    # Inicjalizacja Pygameee
    pygame.init()

    font = pygame.font.Font(None, 36)

    boxes = create_box_wall()  # Add each individual box sprite to the group
    walls = pygame.sprite.Group()
    apples = pygame.sprite.Group()

    # Inicjalizacja gracza
    player = Player()

    # Grupa sprite'ów
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    running = True
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
        walls.update()
        walls = updateWalls(boxes, walls, apples)
        apples.update()
        apples = updateApples(boxes, walls, apples)
        player_boxes_collision(player, boxes)
        player_walls_collision(player, walls)
        player_apples_collision(player, apples)

        if len(boxes) == 0:
            boxes = create_box_wall()

        # Rysowanie
        SCREEN.fill(LIGHT_PISTACHIO)
        # Rysowanie ścian
        walls.draw(SCREEN)
        boxes.draw(SCREEN)
        apples.draw(SCREEN)

        all_sprites.draw(SCREEN)

        # rydowanie metryki
        text_surface = font.render("Score: " + str(player.score), True, BLACK)
        SCREEN.blit(text_surface, (WIDTH - text_surface.get_width() - 20, 0))
        text_surface = font.render("Speed: " + str(speed), True, BLACK)
        SCREEN.blit(text_surface, (WIDTH - text_surface.get_width() - 20, text_surface.get_height() + 10))

        # Wyświetlanie zmian
        pygame.display.flip()

    # Zamknięcie programu
    pygame.quit()
    sys.exit()

if __name__ == "__main__":

    main_game_loop()
