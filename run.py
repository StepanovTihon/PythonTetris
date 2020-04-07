from FigClass import *
from GameZone import *
from Pygame import *
import time as tm
Fig = FigClass()
Gamezone = GameZoneClass()
GameScreen = GameScreenClass()
GameScreen.DrawGrid()
GameScreen.Update()
t=0.8


while True:
    GameScreen.demon()
    Gamezone.Set(Fig.Xpos(),Fig.Ypos(),Fig.GetFig(), 1, Fig.FigColor())
    GameScreen.Write(Gamezone.GetGameZone(), Gamezone.GetZoneColor())
    GameScreen.Update()
    print(Gamezone.GetZoneColor())
    GameScreen.Clear()
    Gamezone.Set(Fig.Xpos(),Fig.Ypos(),Fig.GetFig(),-1, Fig.FigColor())
    if(GameScreen.N()):
        t=0.1
    else:
        t=0.8    
    if(GameScreen.L()==True and Gamezone.CheckPaste(Fig.Xpos()-1,Fig.Ypos(),Fig.GetFig())):
        Fig.Xpos(-1)
    
    if(GameScreen.R() and Gamezone.CheckPaste(Fig.Xpos()+1,Fig.Ypos(),Fig.GetFig())):
        Fig.Xpos(1)
    
    if(GameScreen.Rot() and Gamezone.CheckTurn(Fig.Xpos(),Fig.Ypos(),Fig.GetFig())):
        Fig.TurnFig()
    time.sleep(t)
    if(Gamezone.CheckPaste(Fig.Xpos(),Fig.Ypos()+1,Fig.GetFig())):
      Fig.Ypos(1)
    else:
        Gamezone.Set(Fig.Xpos(),Fig.Ypos(),Fig.GetFig(),1, Fig.FigColor())
        Fig = FigClass()
    Gamezone.DelStrings()

        

    
        



