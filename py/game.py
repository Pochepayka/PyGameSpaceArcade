import pygame
from const import *
from enemys import mob
#from Bullets import Ist
from screen import Screen
from player import Player
from Info import Info
from stars import Star
from GlobalInfo import GlobalInfo

#-----------------цикл игры-------------------
class Game():
    def __init__(self):
        self.GlobalInfo = GlobalInfo()
        self.sc = Screen()
        self.clock = pygame.time.Clock()
        self.text_surface =""
        self.moveUp = moveUp
        self.moveDown = moveDown
        self.moveLeft = moveLeft
        self.moveRight = moveRight
        self.fire = fire
        self.mob1=[]



    def FPS(self):
    # Держим цикл на правильной скорости
        self.clock.tick(FPS)



    def Down(self):
        for i in range (0,self.GlobalInfo.countAsteroid):
            self.mob1[i].y += self.mob1[i].speed
        self.star.y += self.star.speed



    def ConectColider(self,boom,bonus):

        def reflect_circle_on_line(lp0, lp1,obj):
            pt = (obj.x+obj.w/2, obj.y+obj.h/2)
            l_dir = (lp1 - lp0).normalize()  # direction vector of the line
            nv = pygame.math.Vector2(-l_dir[1], l_dir[0])  # normal vector to the line
            d = (lp0 - pt).dot(nv)  # distance to line
            return(abs(d)<obj.h/2-5\
                and obj.y+obj.h >= self.player.y \
                and obj.y <= self.player.y +self.player.h \
                and obj.x + obj.w >= self.player.x \
                and obj.x <= self.player.x + self.player.w)


        line_list = []
        t = self.player.collide
        for p0, p1 in zip(t, t[1:] + t[:1]):
            line_list.append((pygame.math.Vector2(p0), pygame.math.Vector2(p1)))

            for line in line_list:
                try:
                    conect = reflect_circle_on_line(*line, self.star)
                    if conect:

                        self.Info.winPoint+=1
                        bonus.play(0)
                        del self.star
                    if self.star.y>self.sc.heigth:
                        del self.star
                except:
                    error = True
                for i in range(0, self.GlobalInfo.countAsteroid):
                    try:
                        conect = reflect_circle_on_line(*line, self.mob1[i])
                        if conect:
                            del self.mob1[i]
                            self.player.hp -=1
                            boom.play(0)
                    except:
                        error = True



    def Event(self):
    # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.GlobalInfo.running = False
            # if stopPlay==False:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and event.pos[0] < 800 and event.pos[0] > 600 \
                        and event.pos[1] < 450 and event.pos[1] > 350 and len(self.GlobalInfo.userText) > 2 and self.GlobalInfo.play== False:
                    self.GlobalInfo.play= True
                    self.GlobalInfo.timeBeforePlay = pygame.time.get_ticks()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and len(self.GlobalInfo.userText) > 2 and self.GlobalInfo.play== False:
                    self.GlobalInfo.play= True
                    self.GlobalInfo.timeBeforePlay = pygame.time.get_ticks()
                elif event.key == pygame.K_LEFT:
                    self.moveLeft = True
                elif event.key == pygame.K_RIGHT:
                    self.moveRight = True
                elif event.key == pygame.K_UP:
                    self.moveUp = True
                elif event.key == pygame.K_DOWN:
                    self.moveDown = True
                    """elif self.GlobalInfo.play == True:
                        if event.key == pygame.K_SPACE and self.ist.Y[self.ist.count - 1] <= 0:
                            self.fire = True
                            self.ist.y = self.player.y
                            self.ist.Null()"""
                elif event.key == pygame.K_BACKSPACE:
                    self.GlobalInfo.userText = self.GlobalInfo.userText[:-1]
                else:
                    self.GlobalInfo.userText += event.unicode

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.moveLeft = False
                elif event.key == pygame.K_RIGHT:
                    self.moveRight = False
                if event.key == pygame.K_UP:
                    self.moveUp = False
                elif event.key == pygame.K_DOWN:
                    self.moveDown = False
                elif event.key == pygame.K_SPACE:
                    self.fire = False



    def Init(self):
        for i in range (0, self.GlobalInfo.countAsteroid):
            try:
                self.mob1[i].num
            except:
                self.mob1.append(mob(i))
                print(i, "mob create")

        try:
            self.Info.winPoint
        except:
            self.Info = Info()
            print("Info create")


        try:
            self.star.obj
        except:
            self.star = Star()
            print("star create")

        #try:
        #    self.ist.count
        #except:
        #    self.ist = Ist(RED,speedBullet)
        #    print("ist create")

        try:
            self.player.obj
        except:
            self.player = Player()
            print("player create")



    def UpdateObjects(self):
        self.player.nickname = self.GlobalInfo.userText
        self.Info.timeBeforePlay = self.GlobalInfo.timeBeforePlay
        self.sc.updateBackground(mainPath, "Game")

        self.player.UpdateCollide()
        pygame.draw.polygon(screen, RED, self.player.collide)

        self.sc.updateObject(self.player.obj, self.player.x, self.player.y)

        try:
            self.sc.updateObject(self.star.obj, self.star.x, self.star.y)
        except:
            error=True

        for i in range (0, self.GlobalInfo.countAsteroid):
            try:
                self.sc.updateObject(self.mob1[i].obj, self.mob1[i].x, self.mob1[i].y)

                if self.mob1[i].xp <= 0 or self.mob1[i].y>self.sc.heigth:
                    self.Info.countKilledMobs += 1
                    del self.mob1[i]
            except:
                error=True



    def DrawInfo(self):
        # поле с информацией
        strLivesCount = "Count of lives:" + str(self.player.hp)
        # strInfoBullets = "Count of bullets:" + str(self.ist.maxCountBull - self.ist.count) + "/" + str(self.ist.maxCountBull)
        strInfoTime = "Time game:" + str(self.Info.timeSincePlay // 100)
        textCountKills = font2.render(strLivesCount, True, YELLOW)
        textCountBull = font2.render(str("Stars:"+str(self.Info.winPoint)), True, YELLOW)
        textCountTime = font2.render(strInfoTime, True, YELLOW)

        surfInfo.fill(GREY)
        surfInfo.blit(textCountKills, (0, 0))
        surfInfo.blit(textCountBull, (0, 25))
        surfInfo.blit(textCountTime, (0, 50))
        surfInfo.set_alpha(255)
        screen.blit(surfInfo, (self.sc.width - self.Info.widthInfo, 0))



    def EventToDo(self):
        if self.Info.stopPlay == False:
            self.Info.timeSinceInit = pygame.time.get_ticks()
            self.Info.timeSincePlay = self.Info.timeSinceInit - self.Info.timeBeforePlay

        #self.ist.yRocket = self.player.y
        if self.moveLeft and self.player.x > 0:
            self.player.x -= self.player.speed
            #self.ist.Left()

        if self.moveRight and self.player.x + self.player.w < self.sc.width:
            self.player.x += self.player.speed
            #self.ist.Right()

        if self.moveUp and self.player.y > 0:
            self.player.y -= self.player.speed
            #self.ist.Upp()

        if self.moveDown and self.player.y + self.player.h < self.sc.heigth:
            self.player.y += self.player.speed
            #self.ist.Down()

        #if self.fire:
            #r=1
            #self.ist.Count()

        #if self.ist.Y[self.ist.count - 1] <= 0:
        #    self.ist.count = 0



    def notPlay(self,table):
        self.sc.updateBackground(lobbyPath, "Lobby")
        self.sc.updateObject(self.GlobalInfo.textPlay, self.GlobalInfo.playPos[0], self.GlobalInfo.playPos[1])
        self.text_surface = baseFont.render(self.GlobalInfo.userText, True, YELLOW)
        self.sc.updateObject(font3.render("Top players", True, YELLOW), 0, 0)
        self.sc.updateObject(self.text_surface, inputRect.x, inputRect.y + 5)
        inputRect.w = max(100, self.text_surface.get_width() + 10)
        textPlsInputName = baseFont.render("Plese input name: ", True, YELLOW)
        self.sc.updateObject(textPlsInputName, self.GlobalInfo.boxNamePos[0], self.GlobalInfo.boxNamePos[1])
        topScore = table.selectTopFive()
        i=40
        for record in topScore:
            self.sc.updateObject(
                font2.render(record[0].__str__() + ":" + record[1].__str__(), True, YELLOW), 0, i)
            if record[0] == self.GlobalInfo.userText:
                self.GlobalInfo.maxScore = record[1]
            i += 30


    def CheckEndGame(self,table):
        table.saveResult({"nickname": self.player.nickname, "score": max(self.Info.winPoint,self.GlobalInfo.maxScore)})

        if self.player.hp <=0:
            self.GlobalInfo.play = False
            del self.player
            del self.Info
            #try:
            #    del self.star
            #except:
            #    error = True
            #del self.ist
            for i in range (0, self.GlobalInfo.countAsteroid):
                try:
                    del self.mob1[i]
                except:
                    error=True
            """
            self.Info.stopPlay = True
            if self.Info.countForWin == 0:
                self.sc.updateObject(self.Info.textLose, self.Info.textWinLosePos[0],self.Info.textWinLosePos[1])
            else:
                self.sc.updateObject(self.Info.textWin, self.Info.textWinLosePos[0],self.Info.textWinLosePos[1])
"""
    """def Bullet(self):

        self.ist.Draw()
        self.ist.Up()
        for j in range(0, self.ist.maxCountBull):
            for i in range(0, self.GlobalInfo.countAsteroid):
                try:
                    if self.ist.Y[j] < 10 + self.mob1[i].h and self.ist.Y[j] > self.mob1[i].h - self.ist.sp and \
                        self.ist.X[i] > self.mob1[i].x and self.ist.X[j] < self.mob1[i].x + self.mob1[i].w:
                        self.mob1[i].xp -= 1
                except:
                    error=True"""


