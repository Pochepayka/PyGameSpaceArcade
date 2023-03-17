from const import *
class Player():
    def __init__(self):
        self.x = xRocket
        self.y = yRocket
        self.obj = pygame.image.load(os.path.join(BASE, rocketPath))
        self.hp = playerHp
        self.h = heightRocket
        self.w = widthRocket
        self.speed = speed
        self.nickname = "player"
        self.collide = [(self.x + 25, self.y + self.h - 25),
                        (self.x + self.w / 2, self.y),
                        (self.x + self.w - 25, self.y + self.h - 25)]
        self.textWinLosePos = textWinLosePos

    def UpdateCollide(self):
        self.collide = [(self.x + 25, self.y + self.h - 25),
                        (self.x + self.w / 2, self.y),
                        (self.x + self.w - 25, self.y + self.h - 25)]

    def __del__(self):
        print("Объект player удален")














