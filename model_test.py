# Testing Package
import unittest

# File to be tested
from model import TicTacToe, CIRCLE, CROSS, EMPTY


# Class that holds the tests
class TestPrime(unittest.TestCase):
    def setUp(self):
        self.tictactoe = TicTacToe()

    # getBoard function test
    def test_getBoard(self):
        t = self.tictactoe

        # Make sure board is empty
        for row in range(3):
            for col in range(3):
                self.assertEqual(0, t.getBoardPosition(row, col))

    # getCurrentPlayer and flipCurrentPlayer function test
    def test_getCurrentPlayer(self):
        t = self.tictactoe
        p = t.getCurrentPlayer()
        t.flipCurrentPlayer()
        self.assertNotEqual(p, t.getCurrentPlayer())
        t.flipCurrentPlayer()
        self.assertEqual(p, t.getCurrentPlayer())

    # setBoardPosition function test
    def test_setBoardPosition(self):
        t = self.tictactoe

        t.setBoardPosition(2, 2, CROSS)
        self.assertEqual(CROSS, t.getBoardPosition(2, 2))

        t.setBoardPosition(1, 1, CIRCLE)
        self.assertEqual(CIRCLE, t.getBoardPosition(1, 1))

        # self.assertRaises(Error, )

    # getWinner function test
    def test_getWinner(self):
        t = self.tictactoe

        self.assertEqual(EMPTY, t.getWinner())

        for i in range(3):
            t.setBoardPosition(i, i, CROSS)

        self.assertEqual(CROSS, t.getWinner())

        for i in range(2):
            t.setBoardPosition(i, i, CIRCLE)
        t.setBoardPosition(2, 2, CROSS)

        self.assertEqual(EMPTY, t.getWinner())


if __name__ == '__main__':
    unittest.main()