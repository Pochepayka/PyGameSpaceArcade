import pygame
import random
import sys
import os


# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (200, 200, 200)
YELLOW = (250, 250, 0)
ORANGE = (250, 100, 0)

# Экран
WIDTH = 1400
HEIGHT = 800
FPS = 60
screen = pygame.display.set_mode((WIDTH, HEIGHT))#,pygame.FULLSCREEN)

# Экран с кнопкой Play
textWinLosePos = (560, 375)
boxNamePos = (WIDTH/2-200,305)
playPos = [610,375]
play = False
stopPlay = False
surfBlock = pygame.Surface((WIDTH,HEIGHT))
nameInit = True#False
mainName = ""
active = False
userText = ''
mainPath ="media/image/main1.bmp"
lobbyPath = "media/image/lobby1.bmp"

# Ракета игрока
xRocket = 650
yRocket = 630
widthRocket = 150
heightRocket = 150
speed = 15
playerHp = 3
moveRight = False
moveLeft = False
moveUp = False
moveDown = False
#surfRocket = pygame.Surface((widthRocket,heightRocket), pygame.SRCALPHA, 32)
#surfRocket = surfRocket.convert_alpha()#прозрачность фона
rocketPath = "./media/image/rocket.png"

# Пули
speedBullet = 20
maxCountBull = 5
countBullets = 0
fire = False

# Мобы
widthMob = 90
heightMob = 85
mobXp = 5
countAsteroid = 15
countKilledMobs=0
surfMob = pygame.Surface((widthMob,heightMob))
mobExist = [False] * countAsteroid
countForWin = 5
speedAsteroid = 10
asteroidPath = "./media/image/asteroid.png"

# звездаd
starPath = "./media/image/star.png"
speedStar = speedAsteroid
widthStar = 50
heightStar = 50

# Табло инфы
widthInfo = 200
heightInfo = 75
surfInfo = pygame.Surface((widthInfo,heightInfo))#, pygame.SRCALPHA, 32)
#surfInfo = surfInfo.convert_alpha()#прозрачность фона

# Время
timeBeforePlay = 0
timeSincePlay = 0
timeSinceInit = 0

#-------------вспомогательные элементы

pygame.font.init()
baseFont = pygame.font.Font(None,36)
font1 = pygame.font.Font(None,100)
font2 = pygame.font.Font(None,25)
font3 = pygame.font.Font(None,40)
inputRect = pygame.Rect(WIDTH/2+20, 300, 140, 32)

BASE = 'C:/Users/vovap/PycharmProjects/GameForBauman/'
