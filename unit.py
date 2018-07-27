from graphics import *

class Unit(object):
    
    def __init__(self, x , y, stat ,win):
        self.x = x
        self.y = y
        self.stat = stat
        self.s = Rectangle(Point(self.x*20,self.y*20),Point(self.x*20+20, self.y*20+20))
        self.s.draw(win)

    def update(self, win):
        if(self.stat):
            self.s.setFill('green')
        else:
            self.s.setFill('white')

    def set(self, stat):
        self.stat = stat
    
    def inverse(self, win):
        self.stat = not self.stat
        self.update(win)

