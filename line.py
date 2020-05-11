from graphics import *

class graphwindow():

    def __init__(self):
        self.win = GraphWin("Graphics_lab",800,800)
        self.win.setBackground("gray")

    def set_viewport(self,xvmin,yvmin,xvmax,yvmax):
        self.win.setCoords(xvmin,yvmin,xvmax,yvmax)
        for i in range(xvmin,xvmax):
            p = self.draw_point(i,(yvmin+yvmax)/2,3,"white")
        for i in range(yvmin,yvmax):
            p = self.draw_point((xvmin+xvmax)/2,i,3,"white")

    def map_to(self,xvmin,yvmin,xvmax,yvmax,xwmin,ywmin,xwmax,ywmax,x,y):
        xv = xvmin + ((x-xwmin)*(xvmax-xvmin)/(xwmax-xwmin))
        yv = yvmin + ((y-ywmin)*(yvmax-yvmin)/(ywmax-ywmin))
        return int(xv),int(yv)
            
    def draw_point(self,x,y,width,color):
        p = Point(x,y)
        #p.setWidth(width)
        p.setFill(color)
        p.draw(self.win)
    
    def draw_line(self,x0,y0,x1,y1):
        dx = x1 - x0
        dy = y1 - y0

        xsign = 1 if dx > 0 else -1
        ysign = 1 if dy > 0 else -1

        dx = abs(dx)
        dy = abs(dy)

        if dx > dy:
            xx = xsign
            xy = 0
            yx = 0
            yy = ysign
        else:
            dx, dy = dy, dx
            #xx, xy, yx, yy = 0, ysign, xsign, 0
            xx = 0
            xy = ysign
            yx = xsign
            yy = 0

        D = 2*dy - dx
        y = 0
        for x in range(dx + 1):
            self.draw_point(x0 + x*xx + y*yx, y0 + x*xy + y*yy,4,"blue")
            if D >= 0:
                y += 1
                D -= 2*dx
            D += 2*dy
                
    def put_text(self,x,y,msg):
        t = Text(Point(x,y),msg)
        t.setSize(8)
        t.draw(self.win)

print()
print("***Midpoint line algorithm implemented using point function of graphics.py library***")
print()          
x1,y1 = map(int,input("Enter the coordinates of the first point : ").split())
x2,y2 = map(int,input("Enter the coordinates of the second point : ").split())
print()
print("You need to enter the coordinates of viewport and window in terms of half of total size of viewport")
print("ie.if you enter 400 400 then these will be extended to x(-400,400) and y(-400,400)")
print()
vx,vy = map(int,input("Enter the size of viewport : ").split())
wx,wy = map(int,input("Enter the size of window : ").split())
port = graphwindow()
port.set_viewport(-vx,-vy,vx,vy)
new_x1,new_y1 = port.map_to(-vx,-vy,vx,vy,-wx,-wy,wx,wy,x1,y1)
new_x2,new_y2 = port.map_to(-vx,-vy,vx,vy,-wx,-wy,wx,wy,x2,y2)
print("Given points after mapping are : ","(",new_x1,",",new_y1,") & (",new_x2,",",new_y2,")")
port.draw_line(new_x1,new_y1,new_x2,new_y2)
port.win.getMouse() 
port.win.close()














