from DrawingPanel import *

class point:
    x=0
    y=0
    def __init__(self, x, y,g):
        self.x=x
        self.y=y
        g.fill_oval(self.x-6, self.y+6, 3, 3)
        if(175>self.x-6>25 and 150>y+6>50):
            g.draw_string("("+str(self.x)+","+str(self.y)+")", self.x, self.y,"red")
        else:
            g.draw_string("("+str(self.x)+","+str(self.y)+")",self.x, self.y, "black")


panel = DrawingPanel(200, 200, background="white")
panel.draw_oval(25,25,150,150,"black")


p1=point(50,20,panel)
p2=point(10,72,panel)
p3=point(90,60,panel)
p4=point(74,98,panel)
p5=point(150,91,panel)
p6=point(5,136,panel)
