from graphics import *
from time import sleep as delay
from unit import Unit

__winX__, __winY__ = 1200, 800

map =[[0 for i in range(40)] for i in range(40)]
book = [[0 for i in range(40)] for i in range(40)]

di = [
    [-1,-1],
    [-1,0],
    [-1,1],
    [0,-1],
    [0,1],
    [1,-1],
    [1,0],
    [1,1]
]

def initMap(win):
    for i in range(40):
        line = Line(Point(i*20, 0), Point(i*20, 800))
        line.draw(win)
        line = Line(Point(0, i*20), Point(800, i*20))
        line.draw(win)

def va(x):
    if(x>=0 and x<40):
        return True
    else:
        return False

def checkSat(x, y):
    r = 0
    for i in range(8):
        if(va(x + di[i][0]) and va(y + di[i][1])):
            if(map[x + di[i][0] ][ y + di[i][1]].stat):
                r += 1
    return r
            


def run(win):
    for i in range(40):
        for j in range(40):
            r = checkSat(i, j)
            if(map[i][j].stat):
                if(r == 2 or r == 3):
                    book[i][j] = True
                else:
                    book[i][j] = False
            else:
                if(r == 3):
                    book[i][j] = True
                else:
                    book[i][j] = False

    for i in range(40):
        for j in range(40):
            if(book[i][j] != map[i][j].stat):
                map[i][j].inverse(win)



if __name__ == '__main__':

    win = GraphWin('QAQ', __winX__, __winY__)
    #initMap(win)
    rect = Rectangle(Point(800, 0), Point(1200, 800))
    rect.setFill('blue')
    rect.draw(win)
    for i in range(40):
        for j in range(40):
            map[i][j] = Unit(i,j, False,win)
            map[i][j].update(win)

    # num = input("input：")
    for i in range(200):
        q = win.getMouse()
        if(q.getX()>800):
            break
        map[int(q.x/20)][int(q.y/20)].set(True)
        map[int(q.x/20)][int(q.y/20)].update(win)

    text = Text(Point(50, 50), "1")
    text.setTextColor('red')
    text.draw(win)
    for i in range(10000000000):
        run(win)
        text.setText(str(i))
        

    text =Text(Point(400, 400), "END")
    text.setTextColor('red')
    text.setSize(36)
    text.draw(win)

    while(True):
        q = win.getMouse()
    
    
    

    delay(1000)
    