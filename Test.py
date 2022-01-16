import unittest

import Player
from Player import *


class Test(unittest.TestCase):

    def test_inicial(self):  # primero defino al jugador y puesto a 0 el marcador
        player = Player()
    def test_0_0(self):
        player = Player()
        self.assertEquals("0-0",player.calcularPuntuacion())
