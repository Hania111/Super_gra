import pygame,random
from settings import WHITE, HEIGHT, BOX_HEIGHT,BOX_WIDTH,BOX_SEP,WIDTH, BOX_NUM, PINK
from Player import Player
from typing import Set


pygame.init()
class Box(pygame.sprite.Sprite):
    def __init__(self, x: float, y:float, width: float, height: float, value: int)->None:
        pygame.sprite.Sprite.__init__(self)
        self.value: int = value

        # Create a surface for the box with value displayed
        self.image: pygame.Surface = pygame.Surface((width, height))
        self.image.fill(PINK)
        font = pygame.font.Font(None, 24)
        text = font.render(str(self.value), True, (0, 0, 0))
        text_rect = text.get_rect(center=(width // 2, height // 2))
        self.image.blit(text, text_rect)

        self.rect = self.image.get_rect()
        self.rect.x= int(x)
        self.rect.y= int(y)

    def update(self, player: Player)-> None:
        self.rect.y+=player.step
        self.update_text()
        if self.rect.y>HEIGHT:
            self.kill()


    def update_text(self)-> None:
        text: pygame.surface.Surface = pygame.font.Font(None, 24).render(str(self.value), True, (0, 0, 0))
        text_rect: pygame.Rect = text.get_rect(center=(self.rect.width // 2, self.rect.height // 2))
        self.image.fill(PINK)
        self.image.blit(text, text_rect)

    def decrease_value(self, amount: int)-> None:
        self.value -= amount
        if self.value <= 0:
             self.value = 0
             self.kill()  # Remove the box from the group
        self.update_text()


def draw_missing()-> Set[int]:
    return set(random.sample(range(BOX_NUM +1), k=2))
def create_box_wall()->pygame.sprite.Group:
    missing = draw_missing()
    boxes: pygame.sprite.Group = pygame.sprite.Group()
    width= (WIDTH - 10*BOX_NUM)/BOX_NUM
    for i in range(BOX_NUM):
        if i not  in missing:
            boxes.add(Box( 10+ i *(width +10),-width, width, width, random.randint(5, 50)))
    return boxes


