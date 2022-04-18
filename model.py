# Possible values in each square
from random import randint

EMPTY = 0
CIRCLE = 1
CROSS = 2

# Tie constant
TIE = -1

# [
# [1, 2, 3], row 1
# [4, 5, 6], row 2
# [7, 8, 9], row 3
# ]

# board[1][2] = 6


class TicTacToe:
    def __init__(self):
        # Represents tic tac toe board
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.currentPlayer = randint(1, 2)

    def getCurrentPlayer(self):
        return self.currentPlayer

    # Returns winner as value 0, 1, or 2
    def getWinner(self):
        # All three columns in a row are the same
        for row in self.board:
            value = row[0]
            isSame = True
            for elem in row:
                if elem != value:
                    isSame = False

            if isSame and value != EMPTY:
                return value

        # All three rows in a column are the same
        for i in range(3):
            value = self.board[0][i]
            isSame = True
            for row in self.board:
                if row[i] != value:
                    isSame = False

            if isSame and value != EMPTY:
                return value

        # Diagonals are the same
        value = self.board[1][1]
        isSame = True
        for i in range(3):
            if self.board[i][i] != value:
                isSame = False

        if isSame and value != EMPTY:
            return value
        else:
            isSame = True
            for i in range(3):
                if self.board[i][2 - i] != value:
                    isSame = False
            if isSame and value != EMPTY:
                return value

        # Check for tie
        isTie = True
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == EMPTY:
                    isTie = False
        if isTie: return TIE

        return EMPTY

    def getBoardPosition(self, row, column) -> int:
        # Error handling
        if row < 0 or row > 2:
            raise ("Invalid value")
        if column < 0 or column > 2:
            raise ("Invalid value")

        return self.board[row][column]

    def setBoardPosition(self, row, column, value):
        # Error handling
        if value < 0 or value > 2:
            raise ("Invalid value")
        if row < 0 or row > 2:
            raise ("Invalid value")
        if column < 0 or column > 2:
            raise ("Invalid value")

        self.board[row][column] = value

    def flipCurrentPlayer(self):
        # if self.currentPlayer == CIRCLE:
        #     self.currentPlayer = CROSS
        # else:
        #     self.currentPlayer = CIRCLE

        self.currentPlayer = 3 - self.currentPlayer

    def resetBoard(self):
        for row in range(3):
            for col in range(3):
                self.setBoardPosition(row, col, EMPTY)