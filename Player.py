import pygame
from utils import PINK, WIDTH, HEIGHT, BLACK, step
from Wall import walls
from Box import boxes

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(PINK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)

    def update(self):
        old_rect = self.rect.copy()

        # Poruszanie gracza
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= step
        if keys[pygame.K_RIGHT]:
            self.rect.x += step
        if keys[pygame.K_UP]:
            self.rect.y -= step
        if keys[pygame.K_DOWN]:
            self.rect.y += step

        # Sprawdzenie kolizji z granicami ekranu
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT


        # Sprawdzenie kolizji z ścianami
        collision_walls = pygame.sprite.spritecollideany(self, walls)
        if collision_walls:
            self.rect = old_rect
            self.rect.y += 5
            # Sprawdzenie kierunku kolizji
            # if keys[pygame.K_LEFT] and collision_walls.rect.right >= self.rect.left:
            #     self.rect.left = collision_walls.rect.left
            # if keys[pygame.K_RIGHT] and collision_walls.rect.left <= self.rect.right:
            #     self.rect.right = collision_walls.rect.right
            # if keys[pygame.K_UP] and collision_walls.rect.bottom >= self.rect.top:
            #     self.rect.top = collision_walls.rect.bottom
            #     self.rect.y += 5
            # if keys[pygame.K_DOWN] and collision_walls.rect.top <= self.rect.bottom:
            #     self.rect.bottom = collision_walls.rect.top



        collided_boxes = pygame.sprite.spritecollide(self, boxes, False)
        if collided_boxes:
            for box in collided_boxes:
                box.decrease_value(1)
                self.rect = old_rect
                self.rect.y+=5