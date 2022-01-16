import unittest

class Player(unittest.TestCase):

    score=["0","15","30","40"] #definidos los puntos

    def __init__(self): #definimos el marcador inicial
        self.score = "0"

    def ganarPunto(self): #definimos el 15
        self.score= self.score+1
    def getScore(self):
        return self.score[self.score]

