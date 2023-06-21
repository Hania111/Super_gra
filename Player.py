import pygame
from settings import PINK, WIDTH, HEIGHT, BLACK
from utils import game_over

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((50, 50))
        # self.image.fill(PINK)
        self.original_image = pygame.image.load("Untitled_Artwork-1.png")
        self.image = pygame.transform.scale(self.original_image, (40, 80))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        # metrics
        self.score = 100
        self.step = 5
        self.level = 1
        self.player_speed = self.step + 2

    def update(self):
        self.prev_rect = self.rect.copy()
        self.move()
        self.check_screen_collisions()
        self.update_metrics()

    def move(self):
        # Poruszanie gracza
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.player_speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.player_speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.player_speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.player_speed

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

    def update_metrics(self):
        level_speed_mapping = {1: 4, 2: 6, 3: 8}
        if self.score < 150:
            self.level = 1
        elif self.score < 200:
            self.level = 2
        else:
            self.level = 3
        self.step = level_speed_mapping.get(self.level, 4)
