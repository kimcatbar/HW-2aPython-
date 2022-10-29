class Base:
    def __init__(self, x, y, size):
    # TODO: will need to fill this in
        self.x=x
        self.y=y
        self.size=size
    def draw(self): 
        return ""


class Square(Base):
    def __init__(self, x, y, size):
        super().__init__(x,y,size)
    def draw(self): 
        output = "\n" * self.y  +  " " * self.x  + "-" * ((self.size*7)+2) + "\n"
        for _ in range (0,(self.size*3)):
            output += " " * self.x + "|" + " " * (self.size*7) + "|" + "\n"
        output += " " * self.x + "-" * ((self.size*7)+2)
        return output 
def draw_any_shape(myShape): 
    print(myShape.draw())
def main():
    s = Square(1,2,3) 
    draw_any_shape(s)
    #c = Circle(2,2,1)
   # draw_any_shape(c)
main()
