import turtle as t
import random
barrier_namelist = []
class Barrier():
    def __init__(self,a,b,color='black',bwid=5):
        self.color = color
        self.bwid = bwid
        self.leftlower = a
        self.rightupper = b
        self.leftupper = (a[0],b[1])
        self.rightlower = (b[0],a[1])
        self.center = ((a[0]+b[0])/2,(a[1]+b[1])/2)
        self.hlen = (b[0]-a[0])/2
        self.hwid = (b[1]-a[1])/2
        self.display()
        barrier_namelist.append(self)

    def display(self):
        t.penup()
        t.pencolor(self.color)
        t.speed(10)
        t.pensize(self.bwid)
        x = self.bwid
        t.goto(self.leftlower[0]+x,self.leftlower[1]+x)
        t.pendown()
        t.begin_fill()
        t.goto(self.rightlower[0]-x,self.rightlower[1]+x)
        t.goto(self.rightupper[0]-x,self.rightupper[1]-x)
        t.goto(self.leftupper[0]+x,self.leftupper[1]-x)
        t.goto(self.leftlower[0]+x,self.leftlower[1]+x)
        t.end_fill()
        t.penup()

class Snake():
    def __init__(self,thickness=5,segment=6,length=10,speed=10,start=(-350,150),heading=0):#segment蛇的段数，length蛇每段的长度
        t.pensize(thickness)
        t.penup()
        t.speed(speed)
        t.seth(heading)
        self.length = length
        self.segment = segment
        self.start = start
        self.body = [start]
        
    def go_ahead(self):
        while True:
            t.penup()
            t.goto(self.body[-1][0],self.body[-1][1])
            #产生随机数决定方向 
            direction=random.randint(0,2)
            arc=random.randint(0,90)
            if direction==0:    
                t.left(arc)
            elif direction==1:
                pass
            elif direction==2:
                t.right(arc)
            t.forward(self.length)
            temp_pos = t.pos()
            if not iscollision(temp_pos,*barrier_namelist):
                t.goto(self.body[-1][0],self.body[-1][1])
                t.pencolor('red')
                t.pendown()
                t.pencolor((random.random(),random.random(),random.random()))
                t.goto(temp_pos[0],temp_pos[1])
                t.penup()
                self.body.append(temp_pos)
                break
    def erase_tail(self):
        st = self.body.pop(0)
        ed = self.body[0]
        t.penup()
        t.pencolor('white')
        t.goto(st[0],st[1])
        t.pendown()
        t.goto(ed[0],ed[1])
        t.penup()
    def step_generator(self):            
        for i in range(self.segment):
            self.go_ahead()
        while True:
            self.go_ahead()
            self.erase_tail()
            yield 



def iscollision(p,*args):
    def barrier_collision(args):
        for b in args:
            if -b.hlen< (p[0]-b.center[0]) <b.hlen and -b.hwid< (p[1]-b.center[1]) < b.hwid:
                return True
        return False

    out_of_border = p[0]>400-5 or p[0]<-400+5 or p[1]>300-5 or p[1]<-300+5 #5为碰撞体积

    if barrier_collision(args) or out_of_border:
        # print('发生碰撞')
        return True
    else:
        return False


t.setup(800,600)
t.hideturtle()

# b1 = Barrier((-90,-90),(-30,-30))
# b2 = Barrier((30,30),(90,90))
# b3 = Barrier((-90,30),(-30,90))
# b4 = Barrier((30,-90),(90,-30))
# 批量新建对象
counter = 1
for row in range(-400,400,80):
    for column in range(-300,300,80):
        counter += 1
        exec(f'xb{counter} = Barrier((row,column),(row+40,column+40))')
snake1 = Snake(start=(0,0))
# snake2 = Snake(start=(200,200))
step_1 =snake1.step_generator()
# step_2 =snake2.step_generator()

for i in range(200):
    next(step_1)
    # next(step_2)
    

