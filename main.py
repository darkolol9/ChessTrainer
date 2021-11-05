from tkinter import *
from typing import List, Tuple
from PIL import ImageTk,Image
from pieces import *

class Board:

    # negative number is black, else white
    # pawn 1
    # knight 2
    # bishop 3
    # rook 4
    # queen 5
    # king 6

    def __init__(self) -> None:
        self.array = [[0]* 8 for _ in range(8)]

        self.array[1] = [-1]*8
        self.array[6] = [1]*8

        self.array[0][0], self.array[0][7] = -4,-4
        self.array[7][0], self.array[7][7] = 4,4

        self.array[0][1] , self.array[0][6] = -2,-2
        self.array[7][1] , self.array[7][6] = 2,2

        self.array[0][2] , self.array[0][5] = -3,-3
        self.array[7][2] , self.array[7][5] = 3,3

        self.array[0][3] , self.array[0][4] = -5,-6
        self.array[7][3] , self.array[7][4] = 5,6

    def prntBoard(self):
        for row in self.array:
            print(row)


class App:
    def __init__(self,board) -> None:
        self.root = Tk()
        self.root.geometry('480x480')
        self.root.title('chess board')
        self.root.resizable(False, False)
        self.board = board

        self.Sprites = {
            1:'sprites/WPawn.png',
            2:'sprites/WKnight.png',
            3:'sprites/WBishop.png',
            4:'sprites/WRook.png',
            5:'sprites/WQueen.png',
            6:'sprites/WKing.png',
            -1:'sprites/BPawn.png',
            -2:'sprites/BKnight.png',
            -3:'sprites/BBishop.png',
            -4:'sprites/BRook.png',
            -5:'sprites/BQueen.png',
            -6:'sprites/BKing.png',
        }

        #canvas
        self.canvasBody = Canvas(self.root,bg='dark grey',width=480,height=480)
        self.canvasBody.pack()

    def highLightMovesForPiece(self,moves):

        self.canvasBody.delete('all')
        self.drawBoard(self.board)
        for move in moves:
            self.canvasBody.create_rectangle(60*move[1],60*move[0],60*move[1]+60,60*move[0]+60,fill='green',outline='green')


    def drawBoard(self,Board):
        self.canvasBody.delete('all')
        self.drawTiles()

        self.black = ImageTk.PhotoImage(Image.open('sprites/Bpawn.png'))
        self.white = ImageTk.PhotoImage(Image.open('sprites/Wpawn.png'))


        self.imgs = {}


        for i in range(-6,0):
            self.imgs[i] = ImageTk.PhotoImage(Image.open(self.Sprites[i]))
        for i in range(1,7):
            self.imgs[i] = ImageTk.PhotoImage(Image.open(self.Sprites[i]))


        logicArray = Board.array

        for i in range(8):
            for j in range(8):
                if logicArray[i][j] < 0:
                    self.canvasBody.create_image(60*j+30,60*i+30,image=self.imgs[logicArray[i][j]])
                if logicArray[i][j] > 0:
                    self.canvasBody.create_image(60*j+30,60*i+30,image=self.imgs[logicArray[i][j]])


    def drawTiles(self):
        # tile size 60x60
        for i in range(0,8):
            for j in range(0,8):
                if i % 2 == j % 2:
                    self.canvasBody.create_rectangle(60*i,60*j,60*i + 60,60*j + 60,fill='light gray',outline='light gray')


    def run(self):
        self.root.mainloop()







board = Board()

game = App(board)

board.array[3][3] = 2
game.drawBoard(board)
possibleMoves = Knight('white').getPossibleMoves(board,(3,3))
game.highLightMovesForPiece(possibleMoves)



game.run()




