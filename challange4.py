class Rectangle:
  def __init__(self, length, height):
    self.length = length
    self.height = height

  def __str__(self):
    outp = f"Rectangle(width="+str(self.length)+", height="+str(self.height)+")"
    return outp

  def set_width(self, length):
    self.length = length
    return self.length
    
  def set_height(self, height):
    self.height = height
    return self.height
    
  def get_area(self):
    area = self.length * self.height
    return area
    
  def get_perimeter(self):
    return (self.length * 2) + (self.height * 2)
    
  def get_diagonal(self):
    #(width ** 2 + height ** 2) ** .5
    return (self.length ** 2 + self.height ** 2) ** .5
    
   
  def get_picture(self):
    pict = ""
    if self.height < 50 and self.length < 50:
        for x in range(self.height):
            for y in range(self.length):
                pict = pict + "*"
            pict = pict + "\n"
    else :
        pict = "Too big for picture."

    return pict

  def get_amount_inside(self, shape):
    high = self.height / shape.height
    long = self.length / shape.length
    return int(high) * int(long)


class Square(Rectangle):

  def __init__(self, length):
    #super().__init__(length)
    self.length = length
    self.height = length

  def __str__(self):
    outp = f"Square(side="+str(self.length)+")"
    return outp

  def set_side(self, length):
    self.length = length
    self.height = length    
    return length
    
  def set_width(self, length):
    self.length = length
    self.height = length    
    return length
    
  def set_height(self, height):
    self.length = length
    self.height = length    
    return length


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))

var = '''50
26
Rectangle(width=10, height=3)
**********
**********
**********

81
5.656854249492381
Square(side=4)
****
****
****
****

8'''
print ("Should be\n", var)
