import pygame
import sys
from utils import speed, score
from Player import Player
from Box import boxes

from utils import WIDTH, HEIGHT, FPS, LIGHT_PISTACHIO, BLACK
from Player import Player

from Wall import walls, updateWalls
from Apple import Apple


# Inicjalizacja Pygameee
pygame.init()

font = pygame.font.Font(None, 36)

# Utworzenie okna gry
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gra w labirynt")




# Inicjalizacja gracza
player = Player()

# Grupa sprite'ów
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Główna pętla gry
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
    walls = updateWalls(walls)



    # Rysowanie
    screen.fill(LIGHT_PISTACHIO)
    # Rysowanie ścian
    walls.draw(screen)
    boxes.draw(screen)
    all_sprites.draw(screen)

    # rydowanie metryki
    text_surface = font.render("Score: " + str(score), True, BLACK)
    screen.blit(text_surface, (WIDTH - text_surface.get_width() - 20, 0))
    text_surface = font.render("Speed: " + str(speed), True, BLACK)
    screen.blit(text_surface, (WIDTH - text_surface.get_width() - 20, text_surface.get_height() + 10))


    # Wyświetlanie zmian
    pygame.display.flip()

# Zamknięcie programu
pygame.quit()
sys.exit()
