from graphics import *
import math,sys
class graphwindow():

    def __init__(self):
        self.win = GraphWin("Graphics_lab",800,800)
        self.win.setBackground("gray")

    def draw_axis(self):
        color = 'white'
        self.line_function(0,0,0,300,color,2,arrow=True)
        self.line_function(0,0,300,0,color,2,arrow=True)
        self.line_function(0,0,-210,-210,color,2,arrow=True)
    
    def line_function(self,x1,y1,x2,y2,color,width,arrow=False):
        l = Line(Point(x1,y1),Point(x2,y2))
        l.setFill(color)
        l.setWidth(width)
        if(arrow): l.setArrow("last")
        l.draw(self.win)

    def add_padding(self,l):
        for i in l:
            i.append(1)
        return l

    def remove_padding(self,l):
        for i in range(len(l)):
            for j in range(len(l[0])):
                l[i][j] = l[i][j]//l[i][3]
        for i in range(len(l)):
            l[i] = l[i][:-1]
        return l

    def matrix_multiply(self,m1,m2):
        return [[int(sum(a*b for a,b in zip(A_row,B_col))) for B_col in zip(*m2) ] for A_row in m1]

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
        for x in range(int(dx + 1)):
        	temp1 = x0 + x*xx + y*yx
        	temp2 = y0 + x*xy + y*yy
        	self.draw_point(temp1,temp2,3,color)
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

    def draw_2d_polygon(self,l2d,color,undraw=False):
        n = len(l2d)
        port.draw_polygon(l2d[:n//2],color)
        port.draw_polygon(l2d[n//2:],color)
        for i in range(n//2):
            x1,y1,x2,y2 = l2d[i][0],l2d[i][1],l2d[(n//2)+i][0],l2d[(n//2)+i][1]
            self.line_function(x1,y1,x2,y2,color,3)
        if undraw:    self.draw_axis()

    def parallel(self,l,x0,y0,z0,n1,n2,n3,a,b,c):
        d0 = n1*x0 + n2*y0 + n3*z0
        d1 = n1*a + n2*b + n3*c
        l = self.add_padding(l)
        trans_matrix = [
            [d1-a*n1,-b*n1,-c*n1,0],
            [-a*n2,d1-b*n2,c*n2,0],
            [-a*n3,-b*n3,d1-c*n3,0],
            [a*d0,b*d0,c*d0,d1]
        ]
        result = self.matrix_multiply(l,trans_matrix)
        result = self.remove_padding(result)
        return convert_to_2d(result)

    def perspective(self,l,x0,y0,z0,n1,n2,n3,a,b,c):
        d0 = x0*n1 + y0*n2 + z0*n3
        d1 = a*n1 + b*n2 + c*n3
        d = d0-d1
        l = self.add_padding(l)
        trans_matrix = [
            [n1*a+d,b*n1,c*n1,n1],
            [a*n2,b*n2+d,c*n2,n2],
            [a*n3,b*n3,c*n3+d,n3],
            [-a*d0,-b*d0,-c*d0,-d1]
        ]
        result = self.matrix_multiply(l,trans_matrix)
        result = self.remove_padding(result)
        return convert_to_2d(result)

    def orthographic_projection(self,l):
        x0,y0,z0 = 0,0,0
        n1,n2,n3 = 0,0,1
        a,b,c = 0,0,1
        return self.parallel(l,x0,y0,z0,n1,n2,n3,a,b,c)

    def isometric_projection(self,l):
        x0,y0,z0 = 50,50,50
        n1,n2,n3 = 1,1,1
        a,b,c = 1,1,1
        return self.parallel(l,x0,y0,z0,n1,n2,n3,a,b,c)

    def diametric_projection(self,l):
        x0,y0,z0 = 50,0,0
        n1,n2,n3 = 1,1,2
        a,b,c = 1,1,2
        return self.parallel(l,x0,y0,z0,n1,n2,n3,a,b,c)

    def trimetric_projection(self,l):
        x0,y0,z0 = 50,0,0
        n1,n2,n3 = 6,4,3
        a,b,c = 6,4,3
        return self.parallel(l,x0,y0,z0,n1,n2,n3,a,b,c)

    def cavalier_projection(self,l):
        x0,y0,z0 = 0,0,0
        n1,n2,n3 = 0,0,1
        a,b,c = 3,4,5
        return self.parallel(l,x0,y0,z0,n1,n2,n3,a,b,c)

    def cabinet_projection(self,l):
        x0,y0,z0 = 0,0,0
        n1,n2,n3 = 0,0,1
        a,b,c = 3,4,10
        return self.parallel(l,x0,y0,z0,n1,n2,n3,a,b,c)

    def one_point_perspective(self,l):
        x0,y0,z0 = 0,0,0
        n1,n2,n3 = 0,0,1
        a,b,c = 50,50,150
        return self.perspective(l,x0,y0,z0,n1,n2,n3,a,b,c)

    def two_point_perspective(self,l):
        x0,y0,z0 = 200,0,0
        n1,n2,n3 = 1,1,0
        a,b,c = -100,-75,-50
        return self.perspective(l,x0,y0,z0,n1,n2,n3,a,b,c)

    def three_point_perspective(self,l):
        x0,y0,z0 = 0,0,0
        n1,n2,n3 = 1,1,1
        a,b,c = 150,150,150
        return self.perspective(l,x0,y0,z0,n1,n2,n3,a,b,c)
                
def convert_to_2d(l):
    l2d = []
    for i in l:
        l2d.append([i[0] - int(i[2]*(math.cos(math.pi/4))), i[1] - int(i[2]*(math.sin(math.pi/4)))])
    return l2d

port = graphwindow()
port.win.setCoords(-400,-400,400,400)
port.draw_axis()
l = [
    [0,0,0],[80,0,0],[80,80,0],[0,80,0],
    [0,0,80],[80,0,80],[80,80,80],[0,80,80]
]
l2d = convert_to_2d(l)
print("\n***Python code for implementing parallel and perspective projections***\n")
print("\n***A cube(length 80) is used as a polygon to perform all projections operations***\n")
port.draw_2d_polygon(l2d,"black")
print("Press any key from following in graphics window : ")
print("o -> orthographic")
print("i -> isometric")
print("d -> diametric")
print("t -> trimetric")
print("c -> cavalier")
print("a -> cabinet")
print("l -> original polygon")
print("1 -> one point perspective")
print("2 -> two point perspective")
print("3 -> three point perspective")
print("q -> quit")
print("Press e after each operation to undraw the projected polygon")
i=0
while(True):
    key = port.win.getKey()
    if(i==0):
        port.draw_2d_polygon(l2d,"gray",undraw=True)
        i=1
    if(key == 'o'):
        mat = port.orthographic_projection(l)
    elif(key == 'i'):
        mat = port.isometric_projection(l)
    elif(key == 'd'):
        mat = port.diametric_projection(l)
    elif(key == 't'):
        mat = port.trimetric_projection(l)
    elif(key == 'c'):
        mat = port.cavalier_projection(l)
    elif(key == 'a'):
        mat = port.cabinet_projection(l)
    elif(key == 'l'):
        mat = l2d
    elif(key == '1'):
        mat = port.one_point_perspective(l)
    elif(key == '2'):
        mat = port.two_point_perspective(l)
    elif(key == '3'):
        mat = port.three_point_perspective(l)
    elif(key == 'q'):
        break
    else:
        print("Invalid key pressed...")
        continue
    port.draw_2d_polygon(mat,"blue")
    
    print("Operation is completed...Press e to erase")
    if(port.win.getKey() == 'e'):
        port.draw_2d_polygon(mat,"gray",undraw=True)
port.win.getMouse() 
port.win.close()
