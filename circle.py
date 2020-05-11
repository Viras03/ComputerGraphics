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
        p.setFill(color)
        p.draw(self.win)
    
    def circle_points(self,x,y,xc,yc):
        self.draw_point(xc+x,yc+y,3,"blue")
        self.draw_point(xc+x,yc-y,3,"blue")
        self.draw_point(xc-x,yc-y,3,"blue")
        self.draw_point(xc-x,yc+y,3,"blue")
        self.draw_point(xc+y,yc+x,3,"blue")
        self.draw_point(xc+y,yc-x,3,"blue")
        self.draw_point(xc-y,yc+x,3,"blue")
        self.draw_point(xc-y,yc-x,3,"blue")
       
    def draw_circle(self,xc,yc,r):
        x=0
        y=r
        d = 5/4 - r
        while(x<y):
            self.circle_points(x,y,xc,yc)
            if(d<0):
                x+=1
                d+=2*x+3
            else:
                x+=1
                y-=1
                d+=(2*x)-(2*y)+5         
        
    def put_text(self,x,y,msg):
        t = Text(Point(x,y),msg)
        t.setSize(8)
        t.draw(self.win)
        
print()
print("***Midpoint circle algorithm implemented using point function of graphics.py library***")
print()        
x,y = map(int,input("Enter the center of circle : ").split())
r = int(input("Enter the radius of circle : "))
print()
print("You need to enter the coordinates of viewport and window in terms of half of total size of viewport")
print("ie.if you enter 400 400 then these will be extended to x(-400,400) and y(-400,400)")
print()
vx,vy = map(int,input("Enter the size of viewport : ").split())
wx,wy = map(int,input("Enter the size of window : ").split())
port = graphwindow()
#port.draw_axis()
port.set_viewport(-vx,-vy,vx,vy)
new_x,new_y = port.map_to(-vx,-vy,vx,vy,-wx,-wy,wx,wy,x,y)
new_x1,new_y1 = port.map_to(-vx,-vy,vx,vy,-wx,-wy,wx,wy,x,y+r)
new_r = new_y1 - new_y
print("Given center of circle after mapping is :","(",new_x,new_y,")")
print("Given radius of circle after mapping is :",new_r)
port.draw_circle(new_x,new_y,new_r)
#port.circle_points(10,14)
port.win.getMouse() 
port.win.close()







































