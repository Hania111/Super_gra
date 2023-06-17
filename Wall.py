import pygame
import random
from utils import WHITE, HEIGHT, WIDTH, step
from Box import boxes

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y+=step
        if self.rect.y>HEIGHT:
            self.kill()



def updateWalls(walls):
    if random.randint(0,100) == 2:
        wall_height = 10
        wall_length = random.randint(int(WIDTH/8), WIDTH / 2)
        x = random.randint(0,WIDTH)
        wall = Wall(x, 0, wall_length, wall_height)
        if not pygame.sprite.spritecollide(wall, walls, False) and \
            not pygame.sprite.spritecollide(wall, boxes, False):
            walls.add(wall)
    return walls

walls = pygame.sprite.Group()
