from const import*
class GlobalInfo():
    def __init__(self):
        self.running = True
        self.play = play
        self.maxScore = 0
        self.userText = userText
        self.textPlay = font1.render('PLAY', True, (180, 20, 0))
        self.playPos = playPos
        self.boxNamePos = boxNamePos


        self.countAsteroid = countAsteroid
        self.timeBeforePlay = timeBeforePlay
