import unittest
from Partido import Partido


class Test(unittest.TestCase):

     def test_inicial(self): #primero defino al jugador
         player = Partido.Player()
         self.assertEquals("0", player.getScore)

