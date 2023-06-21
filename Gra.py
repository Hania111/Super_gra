import pygame
import sys
from Box import create_box_wall

from settings import WIDTH, HEIGHT, FPS, LIGHT_PISTACHIO, BLACK, background
from Player import Player

from Wall import generateWalls
from Apple import generateApples

from utils import SCREEN
from sprite_actions import player_boxes_collision, player_walls_collision, player_apples_collision


def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
    return True

def update_sprites(player, boxes, walls, apples):
    player.update()
    boxes.update(player)
    walls.update(player)
    walls = generateWalls(boxes, walls, apples)
    apples.update(player)
    apples = generateApples(boxes, walls, apples)
    player_boxes_collision(player, boxes)
    player_walls_collision(player, walls)
    player_apples_collision(player, apples)





def draw_screen(all_sprites, walls, boxes, apples, player, font):
    SCREEN.fill(LIGHT_PISTACHIO)
    walls.draw(SCREEN)
    boxes.draw(SCREEN)
    apples.draw(SCREEN)
    all_sprites.draw(SCREEN)

    text_surface = font.render("Score: " + str(player.score), True, BLACK)
    SCREEN.blit(text_surface, (WIDTH - text_surface.get_width() - 20, 0))
    text_surface = font.render("Level: " + str(player.level), True, BLACK)
    SCREEN.blit(text_surface, (WIDTH - text_surface.get_width() - 20, text_surface.get_height() + 10))

    pygame.display.flip()

def main_game_loop():
    pygame.init()

    font = pygame.font.Font(None, 36)

    boxes = create_box_wall()
    walls = pygame.sprite.Group()
    apples = pygame.sprite.Group()

    player = Player()

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    running = True
    while running:
        pygame.time.Clock().tick(FPS)

        running = handle_events()

        update_sprites(player, boxes, walls, apples)

        draw_screen(all_sprites, walls, boxes, apples, player, font)
        if len(boxes) == 0:
            boxes = create_box_wall()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main_game_loop()

