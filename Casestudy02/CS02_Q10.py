from rectangle import Rectangle

class Parallelepiped(Rectangle):
    def __init__(self,height,length,width):
        self.length = length
        self.width = width
        self.height = height
        
    def volume(self):
        v = self.area()*self.height
        return v
    
    def display(self):
        print("Height", self.height)
        print("Length", self.length)
        print("Width", self.width)
        print("Volume", self.volume())
        
Rect1 =  Rectangle(5,6)
Rect1.display()
print(10)

Parallel1 = Parallelepiped(4,5,6)
Parallel1.display()