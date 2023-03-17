from const import *
class Star():
    def __init__(self):
        self.x = random.randint(0, WIDTH-widthMob)
        self.y = random.randint(-2*HEIGHT,-1/2*HEIGHT)
        self.w = widthStar
        self.h = heightStar
        self.obj = pygame.image.load(os.path.join(BASE, starPath))
        self.speed = speedStar
    def __del__(self):
        print("Объект star удален")