import pygame, threading
import time
import numpy as np

colors = {
    "Black": (0, 0, 0),
    "White": (	255, 222 ,173),
    "Yello": (231, 255, 1),
    "Green": (	154 ,205, 50),
    "Red": (139 ,26 ,26),
    "Orang": (205 ,102 ,0),
    "Blue": (	0, 0 ,205),
    "Pink": (255, 0, 185)
}

class GameScreenClass():
    def __init__(self, SizeCell=25, SizeMatrix=(13, 22)):
        pygame.init()
        self.gameScreen = pygame.display.set_mode((SizeCell*SizeMatrix[0], SizeCell*SizeMatrix[1]))
        self.gameScreen.fill((0,0,0))
        self.SizeCell = SizeCell
        self.SizeMatrix = SizeMatrix
        #self.StartDemon()
        self.demon()
        self.l=False
        self.r=False
        self.n=False
        self.rot=False
    def Update(self):
        pygame.display.flip()
            
    def DrawGrid(self):
        for i in range(-1, self.SizeCell*self.SizeMatrix[0]-1, self.SizeCell):
          pygame.draw.line(self.gameScreen, (255,255,255), [i, 0], [i, self.SizeCell*self.SizeMatrix[1]])
        for i in range(-1, self.SizeCell*self.SizeMatrix[1]-1, self.SizeCell):
          pygame.draw.line(self.gameScreen, (255,255,255), [0, i], [self.SizeCell*self.SizeMatrix[0], i])

    def demon(self):
        run = True
        self.l=False
        self.r=False
        #self.n=False
        self.rot=False        
        #while run:
        
        for event in pygame.event.get():
            #print("   a")
            if(event.type == pygame.QUIT): pass
            
            elif event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_LEFT:
                  self.l=True
                  print("1")
                if event.key == pygame.K_RIGHT:
                  self.r=True
                  print("2")
                if event.key == pygame.K_UP:
                  self.rot=True
                  print("3")
                if event.key == pygame.K_DOWN:
                  self.n=True
                  print("3")
            elif event.type == pygame.KEYUP:
                self.n=False
                                             
                
    
    def StartDemon(self): 
        demon = threading.Thread(target=self.demon)
        demon.daemon = True
        demon.start()
   
    def R(self):
        
        return self.r

    def Rot(self):
        
        return self.rot        
    def L(self):
        
        return self.l

    def N(self):
        
        return self.n    
        

    def Rect(self, x, y, color="White"):
        pygame.draw.rect(self.gameScreen, colors[color], (x*self.SizeCell+2, y*self.SizeCell+2, self.SizeCell-4, self.SizeCell-4))

    def Clear(self, color=(0, 0, 0)):
        self.gameScreen.fill(color)
        self.DrawGrid()

    def Write(self, matrix_in, mass):
        for i in range(len(matrix_in)):
            for j in range(len(matrix_in[0])):
                if(matrix_in[i,j]==1):
                    print(mass[i,j])
                    self.Rect(i, j, mass[i,j])

