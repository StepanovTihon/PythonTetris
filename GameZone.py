import numpy as np

class GameZoneClass():
    def __init__(self):
        self.Zone = np.zeros((13, 22))
        self.ZoneColor = np.array([["Black" for i in range(22)] for i in range(13)])
    
    def CheckPaste(self, x, y,fig_in=np.array([[1,0,0,0],   
                                               [0,0,0,0],
                                               [0,0,0,0],
                                               [0,0,0,0]])):
        ZoneForCheckPaste = self.Zone.copy()
        for i in range(len(fig_in[0])):
            for j in range(len(fig_in)):
                if(x+i<13 and y+j<22 and x+i >-1 and y+j >-1):
                    ZoneForCheckPaste[x+i, y+j]+=fig_in[i, j]
                    if(ZoneForCheckPaste[x+i, y+j]==2): return False
                else:
                    if(fig_in[i,j]==1):
                        return False

        return True

    def CheckTurn(self, x, y,fig_in=np.array([[1,0,0,0],   
                                               [0,0,0,0],
                                               [0,0,0,0],
                                               [0,0,0,0]])):
        ZoneForCheckTurn = self.Zone.copy()
        for i in range(len(fig_in[0])):
            for j in range(len(fig_in)):
                if(x+j<13 and y+(3-i)-1<22 and x+j >-1 and y+(3-i)-1 >-1):
                    ZoneForCheckTurn[x+j, y+(3-i)-1]+=fig_in[ (3-i)-1,j]
                    if(ZoneForCheckTurn[x+j, y+(3-i)-1]==2): return False
                else:
                    
                    if(fig_in[ (3-i)-1,j]==1):
                        print("Hey")
                        return False

        return True

    def CheckString(self, y):
        return np.sum(self.Zone, axis=0)[y] == len(self.Zone)

    def DelString(self, y):
        print("DEL! ", y)
        for i in range(len(self.Zone)): 
            self.Zone[i,y]=0
            self.ZoneColor[i,y]="Black"
        for i in range(len(self.Zone)-1, -1, -1):
            for j in range(len(self.Zone[0])-1, -1, -1):
                if j<=y and j!=0:
                    self.Zone[i,j]=self.Zone[i,j-1]
                    self.ZoneColor[i,j]=self.ZoneColor[i,j-1]

    def Set(self, x, y,fig_in=np.array([[1,0,0,0],
                                        [0,0,0,0],
                                        [0,0,0,0],
                                        [0,0,0,0]]),direct=1,color="White"):
        for i in range(len(fig_in)):
            for j in range(len(fig_in[0])):
                if(x+i<13 and y+j<22 and fig_in[i, j]==1):
                    if(direct==1):
                        self.ZoneColor[x+i, y+j] = color
                        self.Zone[x+i, y+j] = fig_in[i, j]
                    else:
                        self.Zone[x+i, y+j] -= fig_in[i, j]
                        self.ZoneColor[x+i, y+j] = "Black"

    def __str__(self):
        out = ""
        for i in self.Zone:
            for j in i:
                out += str(j)+" "
            out+="\n"
        return out

    def GetGameZone(self):
        return self.Zone

    def GetZoneColor(self):
        return self.ZoneColor    
    
    def DelStrings(self):
      for j in range(22):
        if(self.CheckString(j)==True):
          self.DelString(j)

