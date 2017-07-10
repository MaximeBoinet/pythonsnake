from tkinter import*

direction = 0
speed = 1
window=None
can = None
       

def setDirUp():
    direction = 1
    
def setDirDown():
    direction = 3
    
def setDirLeft():
    direction = 4

def setDirRight():
    direction = 2

class Snake:
    parts  = None
    def __init__(self):
        parts = []
        parts.append(Parts())
    
    
    def avancer(self):
        return
        

class Part:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def _get_x(self):
        return self.x
    
    def _set_x(self, x):
        self.x = x
        
    def _get_y(self):
        return y
    
    def _set_y(self, y):
        self.y = y
        
    x = property(_get_x, _set_x)
    y = property(_get_y, _set_y)

def init():
    window = Tk()
    can=Canvas(height=600,width=600,bg="pink")
    can.pack()    
    window.bind("<Up>", setDirUp)
    window.bind("<Down>", setDirDown)
    window.bind("<Left>", setDirLeft)
    window.bind("<Right>", setDirRight)
    window.mainloop()
    
init()