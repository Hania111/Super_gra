from settings import speed, HEIGHT, step
from utils import game_over
import pygame
def player_boxes_collision(player, boxes):
    collided_boxes = pygame.sprite.spritecollide(player, boxes, False)
    if collided_boxes:
        for box in collided_boxes:
            if player.score == 0:
                game_over()
            player.rect=player.prev_rect
            player.rect.y+=step
            player.score -= 1
            box.decrease_value(1)


def player_walls_collision(player, walls):
    collision_walls = pygame.sprite.spritecollideany(player, walls)
    if collision_walls:
        player.rect = player.prev_rect
        player.rect.y += step

def player_apples_collision(player, apples):
    collision_apples = pygame.sprite.spritecollideany(player, apples)
    if collision_apples:
        player.score += 20
        collision_apples.kill()

