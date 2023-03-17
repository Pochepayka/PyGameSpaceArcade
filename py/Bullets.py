from const import *
class Ist():
    def __init__(self, color, speedBull):
        self.x = xRocket + widthRocket/2
        self.y = yRocket
        self.X = [xRocket + widthRocket/2]*maxCountBull
        self.Y = [HEIGHT]*maxCountBull
        self.c = color
        self.sc = screen
        self.sp = speedBull
        self.spRocket = speed
        self.count = countBullets
        self.yRocket = yRocket
        self.maxCountBull = maxCountBull
    def Draw(self):
        for i in range (0, min(self.count,maxCountBull)):
            pygame.draw.circle(self.sc, self.c,
                           (self.X[i], self.y + speedBullet * (i+1)), 5, 5)

    def Right(self):
        self.x+=speed
        for i in range(0,maxCountBull):
            if self.y + self.sp * (i+1) > self.yRocket-speedBullet:
                self.X[i] += speed

    def Left(self):
        self.x-=speed
        for i in range(0,maxCountBull):
            if self.y+ self.sp * i > self.yRocket-speedBullet:
                self.X[i] -= speed

    def Upp(self):
        self.y-=speed
        for i in range(0,maxCountBull):
            if self.y + self.sp * i > self.yRocket - speedBullet:
                self.Y[i] -= speed

    def Down(self):
        self.y+=speed
        for i in range(0,maxCountBull):
            if self.y + self.sp * i > self.yRocket - speedBullet:
                self.Y[i] += speed

    def Count(self):
        self.count +=1
        self.count = min(self.count,maxCountBull)

    def Null(self):
        self.count = 0
        self.X = [self.x] * maxCountBull
        for i in range(0, maxCountBull):
            self.Y[i] = self.y + speedBullet * i

    def Up(self):
        self.y-=speedBullet
        for i in range(0, maxCountBull):
            self.Y[i] = self.y + speedBullet * i

    def __del__(self):
        print("Объект ist удален")