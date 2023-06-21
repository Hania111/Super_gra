import pygame,random
from settings import HEIGHT, WIDTH, RED, PROBABILITY_APPLES, apple_red_image
from Player import Player



class Apple(pygame.sprite.Sprite):
    def __init__(self, x: int, y :int)-> None:
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.Surface((30,30))
        # self.image.fill(RED)
        self.original_image = pygame.image.load(apple_red_image)
        self.image = pygame.transform.scale(self.original_image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, player: Player)->None:
        """
        Updates position of apple (every object is automaticly moving down)
        """
        self.rect.y+= player.step
        if self.rect.y>HEIGHT:
            self.kill()



def generateApples(boxes: pygame.sprite.Group, walls: pygame.sprite.Group, apples: pygame.sprite.Group) -> pygame.sprite.Group:
    """
    Adds randomly generated apples to the sprite group "apples". Before adding them, I check for collisions with other objects to ensure there are none.
    :param boxes: pygame sprite group of boxes
    :param walls: pygame sprite group of walls
    :param apples: pygame sprite group of apples
    :return: pygame sprite group of apples
    """
    if random.randint(0,PROBABILITY_APPLES) == 2:
        x: int = random.randint(0,WIDTH)
        apple: Apple = Apple(x, 0)
        if not pygame.sprite.spritecollide(apple, walls, False) and \
            not pygame.sprite.spritecollide(apple, boxes, False) and \
                not pygame.sprite.spritecollide(apple, apples, False) :
            apples.add(apple)
    return apples




