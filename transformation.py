from graphics import *
import math,sys

class graphwindow():

    def __init__(self):
        self.win = GraphWin("Graphics_lab",800,800)
        self.win.setBackground("gray")

    def set_viewport(self,xvmin,yvmin,xvmax,yvmax):
        self.win.setCoords(xvmin,yvmin,xvmax,yvmax)
        
    def set_axis(self,xvmin,yvmin,xvmax,yvmax):
        l = Line(Point(xvmin,(yvmin+yvmax)/2),Point(xvmax,(yvmin+yvmax)/2))
        l.setFill("white")
        l.setArrow("both")
        l.setWidth(2)
        l.draw(self.win)
        l = Line(Point((xvmin+xvmax)/2,yvmin),Point((xvmin+xvmax)/2,yvmax))
        l.setFill("white")
        l.setWidth(2)
        l.setArrow("both")
        l.draw(self.win)

    def map_to(self,xvmin,yvmin,xvmax,yvmax,xwmin,ywmin,xwmax,ywmax,x,y):
        xv = xvmin + ((x-xwmin)*(xvmax-xvmin)/(xwmax-xwmin))
        yv = yvmin + ((y-ywmin)*(yvmax-yvmin)/(ywmax-ywmin))
        return int(xv),int(yv)
            
    def draw_point(self,x,y,width,color):
        p = Point(x,y)
        p.setFill(color)
        p.draw(self.win)
    
    def draw_line(self,x0,y0,x1,y1,color):
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
        	self.draw_point(temp1,temp2,3,color)
        	#self.dic[(temp1,temp2)] = self.dic.get((temp1,temp2),0) + 1
        	if D >= 0:
        		y += 1
        		D -= 2*dx
        	D += 2*dy
            
    def draw_polygon(self,l,color):
    	x0,y0 = l[0][0],l[0][1]
    	x1,y1 = x0,y0
    	i=1
    	while(i<len(l)):
    		x2,y2 = l[i][0],l[i][1]
    		self.draw_line(x1,y1,x2,y2,color)
    		x1,y1 = x2,y2
    		i+=1
    	self.draw_line(x2,y2,x0,y0,color)

    def add_padding(self,l):
        for i in l:
            i.append(1)
        return l

    def remove_padding(self,l):
        for i in range(len(l)):
            l[i] = l[i][:-1]
        return l

    def matrix_multiply(self,m1,m2):
        return [[int(sum(a*b for a,b in zip(A_row,B_col))) for B_col in zip(*m2) ] for A_row in m1]

    def translation(self,l,tx,ty):
        l = self.add_padding(l)
        translation_matrix = [[1,0,0],[0,1,0],[-tx,-ty,1]]
        resultant_matrix = self.matrix_multiply(l,translation_matrix)
        resultant_matrix = self.remove_padding(resultant_matrix)
        return resultant_matrix
        
    def scalling(self,l,x,y,sx,sy):
        l = self.translation(l,x,y)
        l = self.add_padding(l)
        scalling_matrix = [[sx,0,0],[0,sy,0],[0,0,1]]
        resultant_matrix = self.matrix_multiply(l,scalling_matrix)
        resultant_matrix = self.remove_padding(resultant_matrix)
        resultant_matrix = self.translation(resultant_matrix,-x,-y)
        return resultant_matrix

    def rotation(self,l,x,y,angle):
        l = self.translation(l,x,y)
        resultant_matrix = self.main_rotation(l,x,y,angle)
        resultant_matrix = self.translation(resultant_matrix,-x,-y)
        return resultant_matrix

    def main_rotation(self,l,x,y,angle):
        self.draw_polygon(l,"gray")
        angle = (math.pi*angle/180)
        l = self.add_padding(l)
        rotation_matrix = [[math.cos(angle),math.sin(angle),0],[-math.sin(angle),math.cos(angle),0],[0,0,1]]
        resultant_matrix = self.matrix_multiply(l,rotation_matrix)
        return (self.remove_padding(resultant_matrix))

    def reflection(self,l,x,y,angle):
        l = self.translation(l,x,y)
        l = self.main_rotation(l,x,y,angle)
        l = self.add_padding(l)
        reflection_matrix = [[-1,0,0],[0,1,0],[0,0,1]]
        resultant_matrix = self.matrix_multiply(l,reflection_matrix)
        resultant_matrix = self.remove_padding(resultant_matrix)
        resultant_matrix = self.main_rotation(resultant_matrix,x,y,-angle)
        resultant_matrix = self.translation(l,-x,-y)
        return resultant_matrix

    def shear_x(self,l,shx):
        l = self.add_padding(l)
        shear_matrix = [[1,0,0],[shx,1,0],[0,0,1]]
        resultant_matrix = self.matrix_multiply(l,shear_matrix)
        return self.remove_padding(resultant_matrix)

    def shear_y(self,l,shy):
        l = self.add_padding(l)
        shear_matrix = [[1,shy,0],[0,1,0],[0,0,1]]
        resultant_matrix = self.matrix_multiply(l,shear_matrix)
        return self.remove_padding(resultant_matrix)

vx,vy,wx,wy = 400,400,400,400
port = graphwindow()
port.set_viewport(-vx,-vy,vx,vy)
port.set_axis(-vx,-vy,vx,vy)
n = int(input("Enter number of edges : "))
l = []
for i in range(n):
    x,y = map(int,input("Enter coordinates of vertex : ").split())
    l.append([x,y])
print("Enter any operation : ")
print("t.Translate")
print("c.Scale")
print("r.Rotate")
print("f.Reflect")
print("s.Shear_x")
print("h.Shear_y")
print("q.quit")
print("e.erase current polygon")
while 1:
    port.draw_polygon(l,"black")
    key = port.win.getKey()
    port.draw_polygon(l,"gray")
    port.set_axis(-vx,-vy,vx,vy)
    if(key == 't'):
        l2 = port.translation(l,30,-30)
    elif(key == 'c'):
        l2 = port.scalling(l,30,-30,2,2)
    elif(key == 'r'):
        l2 = port.rotation(l,0,0,45)
    elif(key == 'f'):
        l2 = port.reflection(l,20,-30,60)
    elif(key == 's'):
        l2 = port.shear_x(l,2)
    elif(key == 'h'):
        l2 = port.shear_y(l,2)
    elif(key == 'q'):
        port.win.getMouse() 
        port.win.close()
        sys.exit()
    else:
        print("Invalid key pressed...")
        continue
    port.draw_polygon(l2,"blue")
    print("Operation is completed...Press e to erase")
    if(port.win.getKey() == 'e'):
        port.draw_polygon(l2,"gray")
        port.set_axis(-vx,-vy,vx,vy)

'''
4
20 20
120 20
120 120
20 120
'''
