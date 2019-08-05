
# class A:
#     def __init__(self):
#         print('__init__被调用')
#         self.data=100
#     def show_data(self):
#         self.data=200
#         print(self.data)

# class B(A):
#     def __init__(self):
#         print('__init__被调用2')


class Shape:
    def draw(self):
        pass
class Point(Shape):
    def __init__(self,x,y):
        self.x,self.y=x,y
    def draw(self):
        print('我是一个点(%d,%d)'%(self.x,self.y))


Shapes=Point(10,20)

def draw_shape(s):
    s.draw()
draw_shape(Shapes)

