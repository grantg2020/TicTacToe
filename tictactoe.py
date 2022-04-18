import tkinter as tk
from model import *
from tkinter import messagebox
from typing import List

import model

# Main window
main = None

#Visual constants
SIZE_OF_SQUARE = 250

# Padding
PADDING = SIZE_OF_SQUARE / 5

game = model.TicTacToe()


class Window(tk.Frame):
    def restartGame(self):
        game.resetBoard()
        for elem in self.msgBox:
            self.canvas.delete(elem)
        self.replayButton.destroy()

        for elem in self.hoverElements:
            self.canvas.delete(elem)

        for elem in self.boardPieces:
            self.canvas.delete(elem)

        self.winner = EMPTY

    def positionToSquares(self, x, y) -> List[int]:
        # Determine which square was clicked
        x /= SIZE_OF_SQUARE
        y /= SIZE_OF_SQUARE

        if x > 2: x = 2
        if y > 2: y = 2

        return [int(x), int(y)]

    def motionEvent(self, event):
        # If someone won, don't do anything
        if self.winner != EMPTY: return

        pos = self.positionToSquares(event.x, event.y)
        x = pos[0]
        y = pos[1]

        # erase what was on old position IF IT CHANGED
        try:
            if self.hoverElements != None:
                for elem in self.hoverElements:
                    self.canvas.delete(elem)
        except:
            pass

        if game.getBoardPosition(x, y) == EMPTY:
            # draw when on that position
            if game.getCurrentPlayer() == CIRCLE:
                self.hoverElements = self.drawCircle(x, y, "#d9d9d9")
            else:
                self.hoverElements = self.drawCross(x, y, "#d9d9d9")

    def clickEvent(self, event):
        # If someone won, don't do anything
        if self.winner != EMPTY: return

        pos = self.positionToSquares(event.x, event.y)
        x = pos[0]
        y = pos[1]

        currentPlayer = game.getCurrentPlayer()

        # Draw and set board position if it isn't filled
        if game.getBoardPosition(x, y) == EMPTY:
            game.setBoardPosition(x, y, currentPlayer)
            self.drawMove(x, y, currentPlayer)

            # Flip current player
            game.flipCurrentPlayer()

            winner = game.getWinner()
            self.winner = winner
            if winner != EMPTY:
                title = 'Winner!'
                body = ''
                if winner == TIE:
                    title = 'Tie!'
                    body = 'You tied!'
                elif winner == CROSS:
                    body = 'Cross wins!'
                else:
                    body = 'Circle wins!'

                self.displayMessage(title, body)

    def drawMove(self, row, column, value):
        # Error handling
        if value < 0 or value > 2:
            raise ("Invalid value")
        if row < 0 or row > 2:
            raise ("Invalid value")
        if column < 0 or column > 2:
            raise ("Invalid value")

        if value == CIRCLE:
            self.boardPieces.append(self.drawCircle(row, column))
        elif value == CROSS:
            for elem in self.drawCross(row, column):
                self.boardPieces.append(elem)

    def drawCircle(self, row, column, color="#000000"):
        # Draw circle
        return [
            self.canvas.create_oval(
                row * SIZE_OF_SQUARE + PADDING,
                column * SIZE_OF_SQUARE + PADDING,
                row * SIZE_OF_SQUARE + SIZE_OF_SQUARE - PADDING,
                column * SIZE_OF_SQUARE + SIZE_OF_SQUARE - PADDING,
                outline=color)
        ]

    def drawCross(self, row, column, color="#000000"):
        elems = []
        # Draw crosses
        elems.append(
            self.canvas.create_line(
                row * SIZE_OF_SQUARE + PADDING,
                column * SIZE_OF_SQUARE + PADDING,
                row * SIZE_OF_SQUARE + SIZE_OF_SQUARE - PADDING,
                column * SIZE_OF_SQUARE + SIZE_OF_SQUARE - PADDING,
                fill=color))
        elems.append(
            self.canvas.create_line(
                row * SIZE_OF_SQUARE + PADDING,
                column * SIZE_OF_SQUARE + SIZE_OF_SQUARE - PADDING,
                row * SIZE_OF_SQUARE + SIZE_OF_SQUARE - PADDING,
                column * SIZE_OF_SQUARE + PADDING,
                fill=color))

        return elems

    # Displays end of game message with play again button
    def displayMessage(self, title, body):
        center_x = SIZE_OF_SQUARE * 3 / 2
        center_y = SIZE_OF_SQUARE * 3 / 2
        box_width = 200
        box_height = 150

        elems = []
        # Draw a rectangle filled and with a border
        elems.append(
            self.canvas.create_rectangle(center_x - (box_width / 2),
                                         center_y - (box_height / 2),
                                         center_x + (box_width / 2),
                                         center_y + (box_height / 2),
                                         fill="#FFF"))
        # Write centered text for the title and body
        elems.append(
            self.canvas.create_text(center_x,
                                    center_y - (box_height / 2) + PADDING / 2,
                                    text=title))
        elems.append(self.canvas.create_text(center_x, center_y, text=body))
        # Draw a button that says Play Again
        #Create a button
        btn = tk.Button(
            self,
            text='Play again',
            # image=tk.PhotoImage(width=1, height=1),
            # compound="c",
            width=8,
            height=2,
            padx=0,
            pady=0,
            command=self.restartGame)

        # Add it 'to the canvas'
        btn.place(x=center_x - 37,
                  y=center_y + (box_height / 2) - PADDING / 2 - 30)

        self.replayButton = btn
        # Save a graphics object (to use for clearing later)
        self.msgBox = elems

    def on_resize(self, event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width) / self.width
        hscale = float(event.height) / self.height
        self.width = event.width
        self.height = event.height
        # resize the canvas
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all", 0, 0, wscale, hscale)

    def __init__(self, parent):
        super(Window, self).__init__(parent)

        # Draw the lines
        self.canvas = tk.Canvas(self,
                                width=SIZE_OF_SQUARE * 3,
                                height=SIZE_OF_SQUARE * 3)
        # horizontal
        self.canvas.create_line(0, SIZE_OF_SQUARE, SIZE_OF_SQUARE * 3,
                                SIZE_OF_SQUARE)
        self.canvas.create_line(0, SIZE_OF_SQUARE * 2, SIZE_OF_SQUARE * 3,
                                SIZE_OF_SQUARE * 2)
        # vertical
        self.canvas.create_line(SIZE_OF_SQUARE, 0, SIZE_OF_SQUARE,
                                SIZE_OF_SQUARE * 3)
        self.canvas.create_line(SIZE_OF_SQUARE * 2, 0, SIZE_OF_SQUARE * 2,
                                SIZE_OF_SQUARE * 3)

        # Bind to left click and mouse moving
        self.canvas.bind("<Button-1>", self.clickEvent)
        self.canvas.bind('<Motion>', self.motionEvent)

        self.canvas.pack(fill=tk.BOTH, expand=1)

        self.winner = EMPTY

        self.boardPieces = []

        self.msgBox = []


if __name__ == "__main__":
    # Create an instance of tkinter
    root = tk.Tk()

    # Create the main window
    main = Window(root)

    # Fill the window with content
    main.pack(fill="both", expand=True)

    #Makes it so you can't resize it
    root.resizable(False, False)

    # Set window title
    root.title("TicTacToe")

    # Display the window
    root.mainloop()