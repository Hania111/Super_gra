import pygame
import random
from settings import WHITE, HEIGHT, WIDTH, STEP,SPEED, PEACH, BOTTLE_GREEN, PROBABILITY_WALL


class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((width, height))
        self.image.fill(BOTTLE_GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y+=STEP*SPEED
        if self.rect.y>HEIGHT:
            self.kill()



def create_walls(boxes, walls, apples):
    if random.randint(0,PROBABILITY_WALL) == 2:
        wall_height = 10
        wall_length = random.randint(int(WIDTH/8), WIDTH / 2)
        x = random.randint(0,WIDTH)
        wall = Wall(x, 0, wall_length, wall_height)
        if not pygame.sprite.spritecollide(wall, walls, False) and \
            not pygame.sprite.spritecollide(wall, boxes, False) and \
                not pygame.sprite.spritecollide(wall, apples, False):
            walls.add(wall)
    return walls


