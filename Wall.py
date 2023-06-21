import pygame
import random
from settings import HEIGHT, WIDTH, BOTTLE_GREEN, PROBABILITY_WALL, HEIGHT_OF_WALL
from Player import Player


class Wall(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image: pygame.Surface= pygame.Surface((width, height))
        self.image.fill(BOTTLE_GREEN)
        self.rect: pygame.Rect = self.image.get_rect()
        self.rect.x= x
        self.rect.y= y

    def update(self, player: Player) -> None:
        """
        Updates position of apple (every object is automaticly moving down)
        """
        self.rect.y+= player.step
        if self.rect.y>HEIGHT:
            self.kill()



def generateWalls(boxes: pygame.sprite.Group, walls: pygame.sprite.Group, apples: pygame.sprite.Group) -> pygame.sprite.Group:
    """
    Adds randomly generated walls to the sprite group "apples". Before adding them, I check for collisions with other objects to ensure there are none.
    :param boxes: pygame sprite group of boxes
    :param walls: pygame sprite group of walls
    :param apples: pygame sprite group of apples
    :return: pygame sprite group of walls
    """
    if random.randint(0,PROBABILITY_WALL) == 2:
        wall_height: int = HEIGHT_OF_WALL
        wall_length = random.randint(int(WIDTH/8), int(WIDTH / 2))
        x = random.randint(0,WIDTH)
        wall = Wall(x, 0, wall_length, wall_height)
        if not pygame.sprite.spritecollide(wall, walls, False) and \
            not pygame.sprite.spritecollide(wall, boxes, False) and \
                not pygame.sprite.spritecollide(wall, apples, False):
            walls.add(wall)
    return walls


