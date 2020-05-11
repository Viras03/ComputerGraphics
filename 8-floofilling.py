from graphics import *

class graphwindow():

    def __init__(self):
        self.win = GraphWin("Graphics_lab",800,800)
        self.win.setBackground("gray")
        self.dic = {}
        self.boundary = []

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
    
    def draw_line(self,x0,y0,x1,y1):
        dx = x1 - x0
        dy = y1 - y0

        xsign = 1 if dx > 0 else -1
        ysign = 1 if dy > 0 else -1

        dx = abs(dx)
        dy = abs(dy)

        if dx > dy:
            xx, xy, yx, yy = xsign, 0, 0, ysign
        else:
            dx, dy = dy, dx
            xx, xy, yx, yy = 0, ysign, xsign, 0

        D = 2*dy - dx
        y = 0
        for x in range(dx + 1):
        	temp1 = x0 + x*xx + y*yx
        	temp2 = y0 + x*xy + y*yy
        	self.draw_point(temp1,temp2,3,"blue")
        	self.dic[(temp1,temp2)] = self.dic.get((temp1,temp2),0) + 1
        	self.boundary.append((temp1,temp2))
        	if D >= 0:
        		y += 1
        		D -= 2*dx
        	D += 2*dy
            
    def draw_polygon(self,n):
    	x0,y0 = map(int,input("Enter the coordinate of starting vertex : ").split())
    	x1,y1 = x0,y0
    	i=0
    	while(i<n-1):
    		x2,y2 = map(int,input("Enter the coordinate of vertex : ").split())
    		self.draw_line(x1,y1,x2,y2)
    		x1,y1 = x2,y2
    		i+=1
    	self.draw_line(x2,y2,x0,y0)
    	
    def fill_polygon(self,x,y):
    	l = []
    	l.append((x,y))
    	while(len(l)!=0):
    		x,y = l.pop()
    		if((x+1,y) not in self.boundary) and ((x,y+1) not in self.boundary) and ((x+1,y+1) not in self.dic):
    			l.append((x+1,y+1))
    			
    		if((x+1,y) not in self.boundary) and ((x,y-1) not in self.boundary) and ((x+1,y-1) not in self.dic):
    			l.append((x+1,y-1))
    			
    		if((x-1,y) not in self.boundary) and ((x,y-1) not in self.boundary) and ((x-1,y-1) not in self.dic):
    			l.append((x-1,y-1))
    			
    		if((x-1,y) not in self.boundary) and ((x,y+1) not in self.boundary) and ((x-1,y+1) not in self.dic):
    			l.append((x-1,y+1))
    			
    		if((x,y) not in self.dic):
    			self.draw_point(x,y,3,"yellow")
    			self.dic[(x,y)] = self.dic.get((x,y),0)+1
    			
    		if((x+1,y) not in self.dic):
    			l.append((x+1,y))
    			
    		if((x,y+1) not in self.dic):
    			l.append((x,y+1))
    			
    		if((x-1,y) not in self.dic):
    			l.append((x-1,y))
    			
    		if((x,y-1) not in self.dic):
    			l.append((x,y-1))
                
    def put_text(self,x,y,msg):
        t = Text(Point(x,y),msg)
        t.setSize(8)
        t.draw(self.win)
          
vx,vy,wx,wy = 400,400,400,400
port = graphwindow()
port.set_viewport(-vx,-vy,vx,vy)
n = int(input("Enter the number of vertices : "))
port.draw_polygon(n)
x,y = map(int,input("Enter any vertex coordinate inside the polygon : ").split())
port.fill_polygon(x,y)
#port.draw_line(new_x1,new_y1,new_x2,new_y2)
port.win.getMouse() 
port.win.close()
