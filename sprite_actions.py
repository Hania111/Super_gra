from settings import SPEED,HEIGHT
from utils import game_over
import pygame
def player_boxes_collision(player, boxes):
    collided_boxes = pygame.sprite.spritecollide(player, boxes, False)
    if collided_boxes:
        for box in collided_boxes:
            if player.score == 0:
                game_over()
            player.rect=player.prev_rect
            player.rect.y+=SPEED
            player.score-=1
            box.decrease_value(1)

