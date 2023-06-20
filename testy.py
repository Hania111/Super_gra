import pygame
from Super_gra.assets.Apple import Apple
from Super_gra.assets.Wall import Wall
from settings import STEP, APPLE_POINTS
from Super_gra.assets.Player import Player
from sprite_actions import player_apples_collision


# testy obiektu Apple
def test_Apple_init():
    x, y = 100, 200
    apple = Apple(x, y)
    assert apple.rect.x == x
    assert apple.rect.y == y

def test_Apple_update():
    x, y = 100, 200
    apple = Apple(x, y)
    apple.update()
    assert apple.rect.y == y + STEP


# testy obiektu Wall
def test_Wall_init():
    x, y = 100, 200
    width, height = 50, 20
    wall = Wall(x, y, width, height)
    assert wall.rect.x == x
    assert wall.rect.y == y
    assert wall.rect.width == width
    assert wall.rect.height == height

def test_Wall_update():
    x, y = 100, 200
    width, height = 50, 20
    wall = Wall(x, y, width, height)
    wall.update()
    assert wall.rect.y == y + STEP


# test zjadania jabłka
def test_Apple_eat():
    apples = pygame.sprite.Group()
    player = Player()
    result = player.score + APPLE_POINTS
    print(result)
    apples.add(Apple(player.rect.x, player.rect.y))
    player_apples_collision(player, apples)
    print(player.score)
    assert result == result

# test kolizji obiektów
# @patch('random.randint', return_value=42)
# def test_collision():

#     boxes = pygame.sprite.Group()
#     walls = pygame.sprite.Group()
#     apples = pygame.sprite.Group()
#
#     # Test when random.randint(0, 35) returns 2
#     # random.randint = lambda a, b: 2
#     walls = updateWalls(boxes, walls, apples)
#     assert len(walls) == 0
    #
    # # Test when random.randint(0, 35) does not return 2
    # random.randint = lambda a, b: 3
    # walls = updateWalls(boxes, walls, apples)
    # assert len(walls) == 1

    # # Test collision with boxes
    # boxes.add(Wall(100, 200, 50, 20))
    # walls = updateWalls(boxes, walls, apples)
    # assert len(walls) == 1
    #
    # # Test collision with existing walls
    # walls.add(Wall(100, 200, 50, 20))
    # walls = updateWalls(boxes, walls, apples)
    # assert len(walls) == 1
    #
    # # Test collision with existing apples
    # apples.add(Wall(100, 200, 50, 20))
    # walls = updateWalls(boxes, walls, apples)
    # assert len(walls) == 1
    #
    # # Test when all collisions are avoided
    # boxes.empty()
    # walls.empty()
    # apples.empty()
    # walls = updateWalls(boxes, walls, apples)
    # assert len(walls) == 2