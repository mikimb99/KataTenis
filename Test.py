import unittest

import Player
from Player import Player


class Test(unittest.TestCase):

    def test_inicial(self):  # primero defino al jugador y puesto a 0 el marcador
        player = Player()
        self.assertEquals("0", player.getScore())
    def test_jugador15(self):
        player= Player()
        player.ganarPunto()
        self.assertEquals("15",player.getScore())
    def test_jugador30(self):
        player= Player()
        player.ganarPunto()
        player.ganarPunto()
        self.assertEquals("30", player.getScore())
