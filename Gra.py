import pygame
import sys
from assets.Box import create_box_wall

from settings import WIDTH, HEIGHT, FPS, LIGHT_PISTACHIO, BLACK
from Player import Player
from assets.Button import Button
from assets.Wall import generateWalls
from assets.Apple import generateApples

from utils import SCREEN
from sprite_actions import player_boxes_collision, player_walls_collision, player_apples_collision


def handle_events():
    for event in pygame.event.get():
        return not event.type == pygame.QUIT


def start_screen_loop():
    font = pygame.font.Font(None, 36)

    start_button = Button(WIDTH // 2, HEIGHT // 2, 200, 50, "Start", font)

    while True:
        pygame.time.Clock().tick(FPS)

        SCREEN.fill(LIGHT_PISTACHIO)
        start_button.update()
        start_button.draw(SCREEN)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if start_button.is_clicked(pos):
                    main_game_loop()
            else:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()



def game_over_screen_loop(player):
    font = pygame.font.Font(None, 36)

    retry_button = Button(WIDTH // 2, HEIGHT // 2, 200, 50, "Retry", font)


    while True:
        pygame.time.Clock().tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if retry_button.is_clicked(pos):
                    main_game_loop()

        SCREEN.fill(LIGHT_PISTACHIO)
        retry_button.update()
        retry_button.draw(SCREEN)

        score_text = font.render("Score: " + str(player.score), True, BLACK)
        SCREEN.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - 100))
        pygame.display.flip()
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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        update_sprites(player, boxes, walls, apples)

        draw_screen(all_sprites, walls, boxes, apples, player, font)
        if len(boxes) == 0:
            boxes = create_box_wall()

        if player.rect.bottom >= HEIGHT:
            game_over_screen_loop(player)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    start_screen_loop()

