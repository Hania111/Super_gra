from Player import Player
from settings import HEIGHT, APPLE_POINTS, nr_pointls_for_level, multiplier_for_speed
from utils import game_over
import pygame
def player_boxes_collision(player, boxes):
    collided_boxes = pygame.sprite.spritecollide(player, boxes, False)
    if collided_boxes:
        for box in collided_boxes:
            if player.score == 0:
                game_over()
            player.rect=player.prev_rect
            player.rect.y+=player.step
            player.score -= 1
            box.decrease_value(1)


def player_walls_collision(player: Player, walls: pygame.sprite.Group)-> None:
    """
    Function checking for collision with walls. If a collision occurs,
    the player cannot move further and will be pushed by it.
    :param player: Player
    :param walls: Sprite Group - list with walls
    """
    collision_walls = pygame.sprite.spritecollideany(player, walls)
    if collision_walls:
        player.rect = player.prev_rect
        player.rect.y += player.step

def player_apples_collision(player: Player, apples: pygame.sprite.Group)-> None:
    """
    Checks for collision between the player and apples. If a collision occurs,
    adds points to the player's score and removes the apple.
    :param player: Player
    :param apples: Sprite Group - list with apples
    """
    collision_apples = pygame.sprite.spritecollideany(player, apples)
    if collision_apples:
        player.score += APPLE_POINTS
        collision_apples.kill()


