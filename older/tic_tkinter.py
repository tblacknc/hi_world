
import tkinter as tk
from tkinter.messagebox import showinfo

class PlotApp(object):

    b = [55,55,55,125,125,125,190,190,190]
    a = [55, 140, 205, 55, 140,205,55, 140, 205]
    lines = ['0,1,2','3,4,5','6,7,8','0,4,8','2,4,6','0,3,6','1,4,7','2,5,8']
    graph = ["", "", "", "", "", "", "", "", ""]
    tie = 0
    won = 0
    lost = 0

    def __init__(self, root):
        self._root = root
        
        self.createCanvas()

    def createCanvas(self):
        global canvas

        for x in range(9):
            PlotApp.graph[x] = ""
            
        canvas = tk.Canvas(self._root, bg='white', height='250', width='275')
        
        canvas.create_line(100, 25, 100, 225)
        canvas.create_line(25, 85, 250, 85)
        canvas.create_line(180, 25, 180, 225)
        x = canvas.create_line(25, 155, 250, 155)
        txt = "won", PlotApp.won, "lost", PlotApp.lost, "tie", PlotApp.tie
        canvas.create_text(200, 230,text=txt)
        canvas.grid(column=2, row=2, sticky='nwes')
        canvas.bind("<Button-1>", self.clicked)
            
    def clicked(self, event):
        x, y = event.x, event.y

        if x <= 100 and y <100:
            box = 0
        if x > 100 and x < 180 and y < 100:
            box = 1
        if x > 180  and y < 100:
            box = 2
        if y > 100 and y < 160 and x < 100:
            box = 3
        if y > 100 and y < 160 and x > 100 and x < 180:   
            box = 4
        if y > 100 and y < 160 and x > 180: 
            box = 5           
        if y > 160 and x < 100:
            box = 6
        if y > 160 and x > 100 and x < 180:   
            box = 7         
        if y > 160 and x > 180: 
            box = 8
        again = 0
        if PlotApp.graph[box] == '':
            canvas.create_text(PlotApp.a[box],PlotApp.b[box],text="X",font=25)
            PlotApp.graph[box] = "X";
        else:
            again = 1
            showinfo("canvas", "place taken go again")
  
        if PlotApp.checkWin(self) == 0 and again == 0:
            PlotApp.youPick(self)
            print("PlotApp.graph =", PlotApp.graph, PlotApp.won, PlotApp.lost, PlotApp.tie)
            PlotApp.checkWin(self)

    def checkTie(self):

        for x in PlotApp.graph:
            if x == "":
                return 0
        return 1

    def checkWin(self):
        
        line = [0,0]
        count = 0
        temp = 0
        if PlotApp.checkTie(self)== 1:
            PlotApp.tie += 1
            txt = "Game Over Tie!"
            showinfo("canvas", txt)
            print("PlotApp.graph =", PlotApp.graph, PlotApp.won, PlotApp.lost, PlotApp.tie)

            app = PlotApp(root)
            return 1
        
        for x in PlotApp.lines:
            cells = x.split(',')
            line[0] = 0
            line[1] = 0
            for cell in cells:
                cell = int(cell)
                entries = ['X','O']
                for entry in entries:
                    if count == 1:
                        count = 0
                    else:
                        count += 1
                    if PlotApp.graph[cell] == entry:
                        temp = temp + 1
                        line[count] += 1
                        if line[count] == 3:
                            if entry == "X":
                                PlotApp.won += 1
                            else:
                                PlotApp.lost += 1
                                
                            txt = "Game Over "+ entry + " wins!"
                            #canvas.create_text(200, 230,text=txt)
                            showinfo("canvas", txt)
                            print("PlotApp.graph =", PlotApp.graph, PlotApp.won, PlotApp.lost, PlotApp.tie)

                            print("PlotApp.graph =", PlotApp.graph)
                            app = PlotApp(root)
                            if entry == "O":
                                PlotApp.youPick(self)
                            #root.mainloop()
                            return 1
        return 0
     
    def youPick(self):
        corners = [0,2,6,8]
        sides = [1,3,5,7]

        two = PlotApp.checkTwo(self, "O")
        if two:
            return 1                            
       
        two = PlotApp.checkTwo(self, "X")
        if two:
            return 1
        if two == 0:
            for corner in corners:
                corner = int(corner)
                if PlotApp.graph[corner] == "":
                    PlotApp.graph[corner] = "O"
                    canvas.create_text(PlotApp.a[corner],PlotApp.b[corner],text="O",font=40)
                    return 1
            if PlotApp.graph[4] == "":
                PlotApp.graph[4] = "O"
                canvas.create_text(PlotApp.a[4],PlotApp.b[4],text="O",font=40)
                return 1
            for side in sides:
                side = int(side)
                if PlotApp.graph[side] == "":
                    PlotApp.graph[side] = "O"
                    canvas.create_text(PlotApp.a[side],PlotApp.b[side],text="O",font=40)
                    return 1

    def checkTwo(self,inpt):
        line = 0
        for x in PlotApp.lines:
            cells = x.split(',')
            line = 0
            for cell in cells:
                cell = int(cell)
                
                if PlotApp.graph[cell] == inpt:
                    line = line + 1
                    #print("PlotApp.graph =", PlotApp.graph[cell], inpt, line)
                    if line == 2:
                        for cell in cells:
                            cell = int(cell)
                            if PlotApp.graph[cell] == '':
                                PlotApp.graph[cell] = 'O'
                                canvas.create_text(PlotApp.a[cell],PlotApp.b[cell],text="O",font=40)
                                return 1
        return 0

def main():
    global root
    root = tk.Tk()
    app = PlotApp(root)
    root.mainloop()
    
    
if  __name__ == '__main__':
    main()
