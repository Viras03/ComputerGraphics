from graphics import *
import math

class graphwindow():

    def __init__(self):
        self.win = GraphWin("Graphics_lab",800,800)
        self.win.setBackground("gray")
        self.dic = {}
        self.ymin = 1000
        self.ymax = -1000

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
        	if D >= 0:
        		y += 1
        		D -= 2*dx
        	D += 2*dy
            
    def draw_polygon(self,n):
    	x0,y0 = map(int,input("Enter the coordinate of starting vertex : ").split())
    	if(y0>self.ymax):
    		self.ymax = y0
    	if(y0<self.ymin):
    		self.ymin = y0
    	x1,y1 = x0,y0
    	i=0
    	while(i<n-1):
    		x2,y2 = map(int,input("Enter the coordinate of vertex : ").split())
    		if(y2>self.ymax):
    			self.ymax = y2
    		if(y2<self.ymin):
    			self.ymin = y2
    		if(y1!=y2):
    			ym = min(y1,y2)
    			inverse_slope = (x2-x1)/(y2-y1)
    			if(ym == y1):
    				self.dic[ym] = [[x1,y2,inverse_slope]] + self.dic.get(ym,[])
    			else:
    				self.dic[ym] = [[x2,y1,inverse_slope]] + self.dic.get(ym,[])
    		self.draw_line(x1,y1,x2,y2)
    		x1,y1 = x2,y2
    		i+=1
    	if(y2!=y0):
    		ym = min(y2,y0)
    		inverse_slope = (x2-x0)/(y2-y0)
    		if(ym == y2):
    			self.dic[ym] = [[x2,y0,inverse_slope]] + self.dic.get(ym,[])
    		else:
    			self.dic[ym] = [[x0,y2,inverse_slope]] + self.dic.get(ym,[])
    	self.draw_line(x2,y2,x0,y0)
    
    def scanline_fill_polygon(self):
   		l = []
   		for i in range(self.ymin,self.ymax+1):
   			if i in self.dic:
   				for j in self.dic[i]:
   					l.append(j)
   			l.sort()
   			print(l)
   			j,k = 0,1
   			while(k<len(l)):
   				f = 0
   				x1 = l[j][0]
   				x2 = l[k][0]
   				self.draw_line(math.ceil(x1),i,math.floor(x2),i)
   				
   				if(l[k][1] == i+1):
   					f+=1
   					l.pop(k)
   				else:
   					l[k][0] += l[k][2]
   				
   				if(l[j][1] == i+1):
   					l.pop(j)
   					f+=1
   				else:
   					l[j][0] +=l[j][2]
   				
   				if f==0:
   					j,k = j+2,k+2
   				elif f==1:
   					j,k = j+1,k+1
   				else:
   					j,k = j,k
   					
   		print("Filling completed")
   		
    def put_text(self,x,y,msg):
        t = Text(Point(x,y),msg)
        t.setSize(8)
        t.draw(self.win)
          
vx,vy,wx,wy = 400,400,400,400
port = graphwindow()
port.set_viewport(-vx,-vy,vx,vy)
n = int(input("Enter the number of vertices : "))
port.draw_polygon(n)
print(port.dic)
port.scanline_fill_polygon()
port.win.getMouse() 
port.win.close()
