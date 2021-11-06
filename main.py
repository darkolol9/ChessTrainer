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
        self.root.geometry('520x590')
        self.root.title('chess board')
        self.root.resizable(False, False)
        self.board = board

        self.turn = 'white'


        self.moveLbl = Label(self.root,text='Move:')
        self.moveLbl.place(relx=0.1,rely=0.9)

        self.moveBtn = Button(self.root,command=self.Move,text='GO!')
        self.moveBtn.place(relx=0.4,rely=0.9)

        self.moveEntry = Entry(self.root,width=10)
        self.moveEntry.place(relx=0.2,rely=0.9)

        self.label = Label(self.root,text = 'a        b       c      d       e       f        g       h',font=('Ariel',18))
        self.label.place(relx=0.05,rely=0.83)

        

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

    
    def notationToLocation(self,notation:str):

        from_ = notation[:2]

        if len(notation) == 2:
            return (8 - int(from_[1]),ord(from_[0])-ord('a')), None
            
        to_ = notation[3:]

        from_ = (8 - int(from_[1]),ord(from_[0])-ord('a'))
        to_ = (8 - int(to_[1]),ord(to_[0])-ord('a'))

        return (from_,to_)
    
    def Move(self):

        
        from_ , to_ = self.notationToLocation(self.moveEntry.get().strip())

        types = {
            1:pawn(self.turn),
            2:Knight(self.turn),
            6:King(self.turn)
        }

        piece = types[abs(self.board.array[from_[0]][from_[1]])]

        if len(self.moveEntry.get()) == 2:
            self.highLightMovesForPiece(piece.getPossibleMoves(self.board,from_),from_)
            return

        elif to_ in piece.getPossibleMoves(self.board,from_):
            self.board.array[to_[0]][to_[1]] = self.board.array[from_[0]][from_[1]]
            self.board.array[from_[0]][from_[1]] = 0
        

        self.drawBoard(self.board)

        self.board.prntBoard()

        self.turn = 'black' if self.turn == 'white' else 'white'


        

    def highLightMovesForPiece(self,moves,location):

        self.canvasBody.delete('all')
        self.drawBoard(self.board)

        self.canvasBody.create_rectangle(60*location[1],60*location[0],60*location[1]+60,60*location[0]+60,fill='green',stipple='gray50',outline='green')
        for move in moves:
            self.canvasBody.create_rectangle(60*move[1],60*move[0],60*move[1]+60,60*move[0]+60,fill='red',stipple='gray50',outline='red')


    def drawBoard(self,Board):
        self.canvasBody.delete('all')
        self.drawTiles()



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
        for i in range(0,8):
            for j in range(0,8):
                if j == 0:
                    self.canvasBody.create_text(5,i*60+20,text=str(8 -i))


    def run(self):
        game.drawBoard(self.board)
        self.root.mainloop()







board = Board()

game = App(board)


game.run()




