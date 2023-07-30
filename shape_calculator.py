class Rectangle:
  def __init__(self,width,height):
    self.width = width
    self.height = height

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"
  
  def set_width(self,width):
    self.width = width

  def set_height(self,height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    if self.height > 50 or self.width > 50:
      return "Too big for picture."
    else:
      picture = ""
      for i in range(self.height):
        picture += "*"*self.width+"\n"
      return picture

  def get_amount_inside(self,shape):
   if self.height < shape.height and self.width < shape.width:
     return 0
   elif shape.height == shape.width:
     a = shape.width
     return (((self.height + a - 1) // a) *
            ((self.width + a - 1) // a))
   else:
     if (shape.width > self.width) or (shape.height > self.height):
        return 0
     else:
       value = (shape.height // self.width ) * (shape.width // self.height)
       # +1 compesate the floor tending to 0 when at least one shape fits
       return value+1    
       

class Square(Rectangle):
  def __init__(self,side):
    super().__init__(side,side)

  def __str__(self):
    return f"Square(side={self.width})"
  

  def set_side(self,side):
    self.height,self.width = side,side

  
