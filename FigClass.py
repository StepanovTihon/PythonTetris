import numpy as np
import random



class FigClass():
    def __init__(self):
        colors = np.array(["White", "Yello", "Green", "Red", "Orang", "Blue", "Pink"])
        figures = np.array(
        [
            [[0, 1, 1, 0],
             [0, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 0, 0, 0]],

            [[0, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 1, 0, 0]],

            [[0, 1, 0, 0],
             [0, 1, 1, 0],
             [0, 1, 0, 0],
             [0, 0, 0, 0]],
         
            [[0, 1, 1, 0],
             [1, 1, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]],

            [[1, 1, 0, 0],
             [0, 1, 1, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]],        

            [[1, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 1, 0, 0],
             [0, 0, 0, 0]],        

            [[0, 0, 0, 0],
             [0, 1, 1, 0],
             [0, 1, 1, 0],
             [0, 0, 0, 0]]                       
        ])
        
        self.x=6
        self.y=0
        self.FigIndex=random.randint(0, len(figures))-1
        self.col=colors[self.FigIndex]
        self.figura = figures[self.FigIndex]

    def TurnFig(self):
        tmp_fig = self.figura.copy()
        for i in range(len(tmp_fig)):
            for j in range(len(tmp_fig[0])):
                self.figura[j, (3-i)-1] = tmp_fig[i, j]
                
    def FigColor(self):
        return self.col     

    def GetFig(self):
        return self.figura
    
    def Xpos(self,scale=0):
        self.x+=scale
        return self.x

    def Ypos(self,scale=0):
        self.y+=scale
        return self.y

    def __str__(self):
        out = ""
        for i in self.figura:
            for j in i:
                out += str(j)+" "
            out+="\n"
        return out

