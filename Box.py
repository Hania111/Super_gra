import pygame,random
from settings import WHITE, HEIGHT, BOX_HEIGHT,BOX_WIDTH,BOX_SEP,WIDTH, BOX_NUM, PINK
from Player import Player


pygame.init()
class Box(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, value):
        pygame.sprite.Sprite.__init__(self)
        self.value = value

        # Create a surface for the box with value displayed
        self.image = pygame.Surface((width, height))
        self.image.fill(PINK)
        font = pygame.font.Font(None, 24)
        text = font.render(str(self.value), True, (0, 0, 0))
        text_rect = text.get_rect(center=(width // 2, height // 2))
        self.image.blit(text, text_rect)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, player: Player):
        self.rect.y+=player.step
        self.update_text()
        if self.rect.y>HEIGHT:
            self.kill()


    def update_text(self):
        text = pygame.font.Font(None, 24).render(str(self.value), True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.rect.width // 2, self.rect.height // 2))
        self.image.fill(PINK)
        self.image.blit(text, text_rect)

    def decrease_value(self, amount):
        self.value -= amount
        if self.value <= 0:
             self.value = 0
             self.kill()  # Remove the box from the group
        self.update_text()


def draw_missing():
    return set(random.sample(range(BOX_NUM +1), k=2))
def create_box_wall():
    missing = draw_missing()
    boxes = pygame.sprite.Group()
    width= (WIDTH - 10*BOX_NUM)/BOX_NUM
    for i in range(BOX_NUM):
        if i not  in missing:
            boxes.add(Box( 10+ i *(width +10),-width, width, width, random.randint(5, 50)))
    return boxes


