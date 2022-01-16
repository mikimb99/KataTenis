import unittest

import Player
from Player import *


class Test(unittest.TestCase):

    def test_inicial(self):  # primero defino al jugador y puesto a 0 el marcador
        player = Player()
    def test_0_0(self):
        player = Player()
        self.assertEquals('0-0',player.calcularPuntuacion())
    def test_15_0(self):
        player = Player()
        player.autoincrementarJug1()
        self.assertEquals('15-0',player.calcularPuntuacion())
    def test_30_0(self):
        player = Player()
        player.autoincrementarJug1()
        player.autoincrementarJug1()
        self.assertEquals('30-0', player.calcularPuntuacion())
    def test_40_0(self):
        player = Player()
        player.autoincrementarJug1()
        player.autoincrementarJug1()
        player.autoincrementarJug1()
        self.assertEquals('40-0', player.calcularPuntuacion())
    def test_0_15(self):
        player = Player()
        player.autoincrementarJug2()
        self.assertEquals('0-15', player.calcularPuntuacion())
    def test_0_30(self):
        player = Player()
        player.autoincrementarJug2()
        player.autoincrementarJug2()
        self.assertEquals('0-30', player.calcularPuntuacion())
    def test_0_40(self):
        player = Player()
        player.autoincrementarJug2()
        player.autoincrementarJug2()
        player.autoincrementarJug2()
        self.assertEquals('0-40', player.calcularPuntuacion())