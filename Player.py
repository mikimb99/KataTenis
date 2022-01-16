import unittest

class Player(unittest.TestCase):

    #score=["0","15","30","40","A","W"] #definido el juego

    def __init__(self): #definimos el marcador inicial
        self.score = "0"

    def ganarPunto(self): #definimos el 15
        self.score ="15"
    def getScore(self):
        return self.score

