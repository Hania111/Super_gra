import random
# pakiet hydra
import pygame
# Ustawienia ekranu
WIDTH = 900
HEIGHT = 700
FPS = 30 #liczba kratek na sekundę

#box settings
BOX_WIDTH =130
BOX_HEIGHT =130
BOX_SEP =20
BOX_NUM =6

# Kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
PISTACHIO = (147,197,114)
LIGHT_PISTACHIO = (210, 240, 180)
PINK = (222,165,164)
PEACH = (255, 218, 185)
BOTTLE_GREEN = (0, 106, 78)



background = pygame.image.load("D:\Programowanie\Python\JezykiSkryptowe\super_gra\images\Get the We Heart It app!.jpeg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
apple_red_image = "D:\Programowanie\Python\JezykiSkryptowe\super_gra\images\clipart1288.png"
snail_image = "Untitled_Artwork-1.png"

# Apple settings
PROBABILITY_APPLES = 100
APPLE_POINTS = 20
# Wall settings
PROBABILITY_WALL = 45
HEIGHT_OF_WALL = 10

# levels settings
speed_level_1 = 4
speed_level_2 = 6
speed_level_3 = 8

level_2_treshold = 150
level_3_treshold = 250

player_speed = 7
start_points = 100





