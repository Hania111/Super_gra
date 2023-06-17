import random
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

# metryki
speed = 1
step_start = 5
step = step_start*speed
player_speed = 9