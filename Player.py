import unittest

class Player(unittest.TestCase):

    def __init__(self):
        self.puntuacionJug1=0
        self.map = {
            0: '0',
            1: '15',
            2: '30',
            3: '40'
        }

    def calcularPuntuacion(self):
        if 0 <= self.puntuacionJug1 <=3:
            return f'{self.map[self.puntuacionJug1]}-0'
    def autoincrementarJug1(self):
        self.puntuacionJug1 +=1