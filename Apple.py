import pygame,random
from utils import WHITE, HEIGHT,draw6,BOX_HEIGHT,BOX_WIDTH,BOX_SEP,WIDTH, RED


pygame.init()
class Apple(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, value):
        pygame.sprite.Sprite.__init__(self)
        self.value = value
        # Create a surface for the box with value displayed
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        font = pygame.font.Font(None, 24)
        text = font.render(str(self.value), True, (0, 0, 0))
        text_rect = text.get_rect(center=(width // 2, height // 2))
        self.image.blit(text, text_rect)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        # Metoda wywoływana w każdej iteracji pętli gry
        pass


