import pygame
from settings import PINK, WIDTH, HEIGHT, BLACK, STEP, SPEED
# from Gra import boxes, walls, apples
from utils import game_over

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((50, 50))
        # self.image.fill(PINK)
        self.original_image = pygame.image.load("pics/snail.png")
        self.image = pygame.transform.scale(self.original_image, (40, 80))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.score = 100

    def update(self):
        self.prev_rect = self.rect.copy()
        self.move()
        self.check_screen_collisions()

    def move(self):
        # Poruszanie gracza
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= STEP*SPEED +2
        if keys[pygame.K_RIGHT]:
            self.rect.x += STEP*SPEED*+2
        if keys[pygame.K_UP]:
            self.rect.y -= STEP*SPEED*+2
        if keys[pygame.K_DOWN]:
            self.rect.y += STEP*SPEED*+2
            print(SPEED)

    def check_screen_collisions(self):
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT



        # # Sprawdzenie kolizji z ścianami
        # collision_walls = pygame.sprite.spritecollideany(self, walls)
        # if collision_walls:
        #     self.rect = self.prev_rect
        #     self.rect.y += 5
        #     # Sprawdzenie kierunku kolizji
        #     # if keys[pygame.K_LEFT] and collision_walls.rect.right >= self.rect.left:
        #     #     self.rect.left = collision_walls.rect.left
        #     # if keys[pygame.K_RIGHT] and collision_walls.rect.left <= self.rect.right:
        #     #     self.rect.right = collision_walls.rect.right
        #     # if keys[pygame.K_UP] and collision_walls.rect.bottom >= self.rect.top:
        #     #     self.rect.top = collision_walls.rect.bottom
        #     #     self.rect.y += 5
        #     # if keys[pygame.K_DOWN] and collision_walls.rect.top <= self.rect.bottom:
        #     #     self.rect.bottom = collision_walls.rect.top
        #
        #
        #
        # collided_boxes = pygame.sprite.spritecollide(self, boxes, False)
        # if collided_boxes:
        #     for box in collided_boxes:
        #         box.decrease_value(1)
        #         self.rect = self.prev_rect
        #         self.rect.y+=5