import pygame
from game import Game
from sqlTable import Endpoint
from const import *
#-------------oткрытие окна игры--------------
pygame.init()
pygame.mixer.init()
pygame.font.init()
pygame.display.set_caption("My Game")

pygame.init()
pygame.mixer.init()
pygame.font.init()
#-----------------цикл игры-------------------
Game = Game()

table = Endpoint()
table.tryCreateTable()

pygame.mixer.music.load(os.path.join(BASE, "media/music/main.mp3"))
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)

boom = pygame.mixer.Sound(os.path.join(BASE, "media/music/crush.ogg"))
boom.set_volume(0.2)
bonus = pygame.mixer.Sound(os.path.join(BASE, "media/music/bonus.mp3"))
bonus.set_volume(0.2)

running = True
while running:
    Game.FPS()
    Game.Event()
    running = Game.GlobalInfo.running
    if Game.GlobalInfo.play:
        Game.Init()
        Game.Down()
        Game.ConectColider(boom,bonus)
        Game.UpdateObjects()
        #Game.Bullet()
        Game.EventToDo()
        Game.DrawInfo()
        Game.CheckEndGame(table)
    else:
        Game.notPlay(table)
    pygame.display.flip()
#------------end running------------------
pygame.quit()
