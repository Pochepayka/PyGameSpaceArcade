from screen import *
class mob():
    def __init__ (self,num):
        self.num = num
        self.xp = mobXp
        self.x = random.randint(0, WIDTH-widthMob)
        self.y = random.randint(-2*HEIGHT,-heightMob)
        self.h = heightMob
        self.w = widthMob

        self.obj = random.choice([pygame.transform.scale(pygame.image.load((os.path.join(BASE,"media/image/asteroid.png"))),(self.w,self.h)),pygame.transform.scale(pygame.image.load((os.path.join(BASE,"media/image/asteroid2.png"))),(self.w,self.h   ))])
            #pygame.image.load(os.path.join(BASE, asteroidPath))
        self.speed = speedAsteroid

    def __del__(self):
        print("Объект mob",self.num ,"удален")
