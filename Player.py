import pygame
from settings import PINK, WIDTH, HEIGHT,SPEED
from utils import game_over
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(PINK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.score =0

    def update(self):
        self.prev_rect = self.rect.copy()
        self.move()
        self.check_screen_collisions()


    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= int(SPEED * 1.25)
        if keys[pygame.K_RIGHT]:
            self.rect.x += int(SPEED * 1.25)
        if keys[pygame.K_UP]:
            self.rect.y -= int(SPEED * 1.25)
        if keys[pygame.K_DOWN]:
            self.rect.y += int(SPEED * 1.25)
        self.check_screen_collisions()


    def check_screen_collisions(self):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            game_over()