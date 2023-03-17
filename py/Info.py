from const import *

class Info():
    def __init__(self):
        self.timeSinceInit = timeSinceInit
        self.timeSincePlay = timeSincePlay
        self.timeBeforePlay = timeBeforePlay

        self.countKilledMobs = countKilledMobs
        self.countForWin = countForWin

        self.winPoint = 0
        self.textWinLosePos = textWinLosePos
        self.stopPlay = False
        self.widthInfo = widthInfo
        self.textLose = font1.render("YOU LOSE!", True, ORANGE)
        self.textWin = font1.render(str("YOU WIN! YOUR COUNT IS"+str(self.winPoint)) , True, YELLOW)
    def __del__(self):
        print("Объект info удален")


