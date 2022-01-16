import unittest

class Player(unittest.TestCase):

    def __init__(self):
        self.puntuacionJug1=0
        self.puntuacionJug2=0
        self.map = {
            0: '0',
            1: '15',
            2: '30',
            3: '40',
            4: 'A',
            5: 'W'
        }
    def calcularPuntuacion(self):

        if self.mismo_score() and self.puntuacionJug1 >=3: #si es >=3 es deuce
                return "deuce"
        elif self.mismo_score()  and self.puntuacionJug1 ==0:
                return "0-0"
        elif self.mismo_score() and self.puntuacionJug1 ==1:
                return "15-15"
        elif self.mismo_score() and self.puntuacionJug1 ==2:
                return "30-30"

    def mismo_score(self):
        times = self.puntuacionJug1 == self.puntuacionJug2 # en los casos que sean iguales
        return times #devuelveme las veces para saber a que están iguales

    def lookup_score(self): #resultado
        return f'{self.lookup_score[self.puntuacionJug1]}-' \
               f'{self.lookup_score[self.puntuacionJug2]}'
    def autoincrementarJug1(self):
        self.puntuacionJug1 +=1

    def autoincrementarJug2(self):
        self.puntuacionJug2 +=1

