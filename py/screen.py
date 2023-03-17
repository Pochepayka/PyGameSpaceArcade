from const import *
class Screen():
    width = WIDTH
    heigth = HEIGHT
    screen = pygame.display.set_mode((width, heigth))
    yCoord = 0

    def __init__(self):
        self.fontInfo = pygame.font.SysFont('arial.ttf', 40)
        self.infoTextSurf = self.fontInfo.render('You can start enter your nickname|Press PLAY to continue|Press <-,->,↑,↓ for moving', True,YELLOW)

    def updateBackground(self,backgroundPath, kind):
        self.background = pygame.image.load(os.path.join(BASE,backgroundPath))
        self.current_background = self.background
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.current_background, (0, -self.heigth + self.yCoord))
        self.screen.blit(self.current_background, (0, self.yCoord))
        if kind == "Lobby":
            self.screen.blit(self.infoTextSurf, (90, 590))
            #self.screen.blit(self.infoTextSurf1, (590, 400))
        if (self.yCoord == self.heigth):
            self.screen.blit(self.current_background, (0, self.heigth - self.yCoord))
            self.yCoord = 0

        self.yCoord += 1

    def updateObject(self, object, x, y):
        self.screen.blit(object, (x, y))
