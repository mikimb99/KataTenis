import unittest
from Player import Player


class Test(unittest.TestCase):

     def test_inicial(self): #primero defino al jugador
         player= Player()
         self.assertEquals("0", player.getScore())

