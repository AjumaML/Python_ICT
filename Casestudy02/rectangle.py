class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
    def perimeter(self):
        p = 2*(self.length+self.width)
        return p
    
    def area(self):
        a = self.length*self.width
        return a
        
    def display(self):
        print("Length", self.length)
        print("Width", self.width)
        print("Perimeter", self.perimeter( ))
        print("Circumference", self.area( ))