import pygame
from settings import PINK, WIDTH, HEIGHT, BLACK, level_2_treshold, level_3_treshold, speed_level_1,\
    speed_level_2, speed_level_3, start_points, player_speed, snail_image
from utils import game_over

class Player(pygame.sprite.Sprite):
    def __init__(self)-> None:
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((50, 50))
        # self.image.fill(PINK)
        self.original_image = pygame.image.load(snail_image)
        self.image = pygame.transform.scale(self.original_image, (40, 80))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        # metrics
        self.score: int = start_points
        self.step: int = speed_level_1
        self.level: int = 1
        self.player_speed: int = player_speed

    def update(self)-> None:
        self.prev_rect = self.rect.copy()
        self.move()
        self.check_screen_collisions()
        self.update_metrics()

    def move(self)-> None:
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

    def check_screen_collisions(self)-> None:
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT
            game_over()

    def update_metrics(self)-> None:
        level_speed_mapping = {1: speed_level_1, 2: speed_level_2, 3: speed_level_3}
        if self.score < level_2_treshold:
            self.level = 1
        elif self.score < level_3_treshold:
            self.level = 2
        else:
            self.level = 3
        self.step = level_speed_mapping.get(self.level, 4)
