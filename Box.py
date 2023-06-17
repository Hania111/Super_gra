import pygame,random
from settings import WHITE, HEIGHT,WIDTH,BLACK,SPEED


pygame.init()
class Box(pygame.sprite.Sprite):
    def __init__(self, x,y,  width, height, value):
        pygame.sprite.Sprite.__init__(self)
        self.value = value

        # Create a surface for the box with value displayed
        self.image = pygame.Surface((width, height))
        self.image.fill(WHITE)
        font = pygame.font.Font(None, 24)
        text = font.render(str(self.value), True, BLACK)
        text_rect = text.get_rect(center=(width // 2, height // 2))
        self.image.blit(text, text_rect)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y+=SPEED
        self.update_text()
        if self.rect.y>HEIGHT:
            self.kill()


    def update_text(self):
        font = pygame.font.Font(None, 24)
        text =font.render(str(self.value), True, BLACK)
        text_rect = text.get_rect(center=(self.rect.width // 2, self.rect.height // 2))
        self.image.fill(WHITE)
        self.image.blit(text, text_rect)

    def decrease_value(self, amount):
        self.value -= amount
        if self.value <= 0:
             self.kill()  # Remove the box from the group
        self.update_text()

