from tkinter import*
import random

directions = []
snakesheartbeat = []
speed = 150
window= None
can = None
nomnom = None
snakes = []
mapsize = 600
mapunit = 15
margin = 2
started = False
foodf = "red"
f_s1 = "green"
f_s2 = "yellow"
outl = "black"

def gameOver():
    noir=can.create_rectangle(0,0,mapsize,mapsize,fill="black",stipple="gray50")
    can.create_text(mapsize/2,mapsize/2,text="PERDU !",fill="red",font="Comic 30")
    window.after(2000,initGame)  
    
def snekAccident():
    global snakes, snakesheartbeat
    heads = []
    
    for l, dangernoodle in enumerate(snakes):
        if snakesheartbeat[l]:
            heads.append(dangernoodle.getHead())
        
    for i, snek in enumerate(snakes):
        if snakesheartbeat[i]:
            for j, part in enumerate(snek.parts[1:]):
                for k, head in enumerate(heads):
                    if head.sameCoord(part):
                        snakesheartbeat[i] = False

def oob():
    global snakes,mapsize,mapunit
    
    for i, snek in enumerate(snakes):
        if snakesheartbeat[i]:
            head = snek.getHead()
            if head.x < 0 or head.x > mapsize-(mapunit-1) or head.y < 0 or head.y > mapsize-(mapunit-1):
                snakesheartbeat[i] = False
    
def spawnNomNom():
    global nomnom,mapunit,mapsize
    nomnom = Part(random.randint(mapunit, int(mapsize/mapunit))*mapunit - mapunit,random.randint(mapunit, int(mapsize/mapunit))*mapunit - mapunit)

def draw():
    global snakes,can,mapunit,margin,nomnom
    can.delete("all")
    
    for i, snek in enumerate(snakes):
        for part in snek.parts:
            if snakesheartbeat[i]:
                can.coords(can.create_oval( margin, margin, mapunit - 2*margin, mapunit - 2*margin,  fill=(f_s1 if (i == 0) else f_s2), outline=outl),
                           part.x,part.y,part.x+mapunit,part.y+mapunit)
            
    can.coords(can.create_oval( margin, margin, mapunit - 2*margin, mapunit - 2*margin,  fill=foodf, outline=outl),
               nomnom.x,nomnom.y,nomnom.x+mapunit,nomnom.y+mapunit)  
    
    if started == True:
        calculatenextcoord()
    
def calculatenextcoord():
    global snakes, window, started, nomnom, snakesheartbeat
    started = True
    
    for i, snek in enumerate(snakes):
        if snakesheartbeat[i]:
            snek.avancer(i)
            if snek.getHead().sameCoord(nomnom):
                snek.nomnom()
                spawnNomNom()
    
    snekAccident()
    oob()
    alive = False 
    
    for j, beat in enumerate(snakesheartbeat):
        if beat:
            alive = beat
            print(snakesheartbeat)
            print("ok" + str(j))
        else:
            snakesheartbeat[j] = False
        
    if not alive:
        gameOver()
    else:
        window.after(speed,draw)

def addSnake():
    global snakes,snakesheartbeat
    dangernoodle = Snake()
    snakes.append(dangernoodle)
    snakesheartbeat.append(True)
    
class Snake:
    global directions,mapsize,mapunit
    parts  = None
    snakelenght = 0
    
    def __init__(self):
        self.parts = []
        self.createBaseSnake()
    
    def createBaseSnake(self):
        for i in range(1,6):
            self.parts.append(Part(((mapsize/2)+(i*mapunit)),(mapsize/2)))
        self.snakelenght = 5
        
    def getHead(self):
        return self.parts[0]
    
    def avancer(self, wichsnek):
        x = 0;
        y = 0;
        
        if directions[wichsnek] == 1:
            y = -1
        elif directions[wichsnek] == 2:
            x = 1
        elif directions[wichsnek] == 3:
            y = 1
        else:
            x = -1
            
        self.parts.insert(0, Part((self.parts[0].x) + x*mapunit, (self.parts[0].y) + y*mapunit))
        self.parts.pop()
    
    def nomnom(self):
        self.parts.append(Part(self.parts[self.snakelenght-1].x, self.parts[self.snakelenght-1].y))

class Part:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def _get_x(self):
        return self._x
    
    def _set_x(self, x):
        self._x = x
        
    def _get_y(self):
        return self._y
    
    def _set_y(self, y):
        self._y = y
    
    def sameCoord(self, part):
        return self.x == part.x and self.y == part.y
    
    x = property(_get_x, _set_x)
    y = property(_get_y, _set_y)

def setDirUp(e):
    if directions[0] != 3:
        directions[0] = 1
    if started == False:
        calculatenextcoord()
        
def setDirDown(e):
    if directions[0] != 1:
        directions[0] = 3
        
    if started == False:
        calculatenextcoord()  
    
def setDirLeft(e):
    if directions[0] != 2:
        directions[0] = 4
        
    if started == False:
        calculatenextcoord()  

def setDirRight(e):
    if directions[0] != 4:
        directions[0] = 2  

def setDirSec(e):
    if len(directions) == 1:
        addSnake()
        directions.append(0)
        
    if e.char == 'z' and directions[1] != 3:
        directions[1] = 1
    if e.char == 's' and directions[1] != 2:
        directions[1] = 3
    if e.char == 'q' and directions[1] != 1:
        directions[1] = 4
    if e.char == 'd' directions[1] != 4:
        directions[1] = 2
        
def initGame():
    global snakes,snakesheartbeat,started,nomnom,directions
    started = False
    snakes = []
    snakesheartbeat = []
    nomnom = None
    directions = []
    addSnake()
    directions.append(0)
    spawnNomNom()
    draw() 
    
def init():
    global can,window
    window = Tk()
    can=Canvas(height=mapsize,width=mapsize,bg="beige")
    can.pack()
    window.bind("<Up>", setDirUp)
    window.bind("<Down>", setDirDown)
    window.bind("<Left>", setDirLeft)
    window.bind("<Right>", setDirRight)
    window.bind("<Key>", setDirSec)   
    initGame()
    window.mainloop()
    
init()