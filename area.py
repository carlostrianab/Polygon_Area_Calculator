#Rectangle constructor
class Rectangle:

  width = 0
  height = 0

  #Sets the heigth if the rectangle with a new value input
  def set_height(self, height):
    self.height = height

  #Sets the width if the rectangle with a new value input
  def set_width(self, width):
    self.width = width

  #Initializes the rectangle instance with values of width and height
  def __init__(self, width, height):
    self.width = width
    self.height = height

  #prints a string in the format "Rectangle(width=5, height=10)"
  def __str__(self):
    prints = 'Rectangle(width=' + str(self.width) + ', height=' + str(
      self.height) + ')'
    return prints

  #Calculates the area using the values of width and height
  def get_area(self):
    return self.width * self.height

  #Calculates the perimeter using the values of width and height
  def get_perimeter(self):
    return ((self.width + self.height) * 2)

  #Calculates the length of the diagonal using the values of width and height
  def get_diagonal(self):
    return ((self.width**2 + self.height**2)**.5)

  #Returns a string representing the width and height of the rectangle using '*' signs
  def get_picture(self):

    if self.height > 50 or self.width > 50:
      return 'Too big for picture.'

    picture = ''
    width_counter = self.width
    height_counter = self.height

    while height_counter > 0:
      if width_counter > 0 and height_counter != 0:
        picture += '*'
        width_counter = width_counter - 1
      elif width_counter == 0 and height_counter != 0:
        picture += '\n'
        width_counter = width_counter + self.width
        height_counter = height_counter - 1

    return picture

  #Calculates how many poligons can fit inside the current instance, receives other instance as argument
  def get_amount_inside(self, shape):
    if type(shape).__name__ == 'Rectangle':
      if shape.height > self.height or shape.width > self.width:
        return 0
      else:
        horizontal_fill = self.height // shape.height
        vertical_fill = self.width // shape.width

        amount_inside = horizontal_fill * vertical_fill
    else:
      if shape.side > self.height or shape.side > self.width:
        return 0
      else:
        horizontal_fill = self.height // shape.side
        vertical_fill = self.width // shape.side

        amount_inside = horizontal_fill * vertical_fill
    return amount_inside


#Square is a subclass of Rectangle
class Square(Rectangle):
  side = 0

  #Initializes the square instance with the same values fot height and width, passed as a side of the square
  def __init__(self, side):
    self.set_height(side)
    self.set_width(side)

  #Returns a string in the format "Square(side=5)"
  def __str__(self):
    prints = 'Square(side=' + str(self.side) + ')'
    return prints

  #Sets the height of the square with a new value input, and adjusts the width and side values
  def set_height(self, height):
    self.side = height
    self.height = self.side
    self.width = self.side

  #Sets the width of the square with a new value input, and adjusts the height and side values
  def set_width(self, width):
    self.side = width
    self.width = self.side
    self.height = self.side

  #Sets the side of the square with a new value input, and adjusts the width and height values
  def set_side(self, side):
    self.side = side
    self.height = side
    self.width = side


#TESTING

rect = Rectangle(5, 10)
print('Rectangle with a width of 5 and a height of 10 was created \n')
print(rect)
print('\n')
print('The area of this rectangle is: \n')
print(rect.get_area())
print('\n')
print('The perimeter of this rectangle is: \n')
print(rect.get_perimeter())
print('\n')
print('The diagonal of this rectangle is: \n')
print(rect.get_diagonal())
print('\n')
print('This is a picture of our rectangle: \n')
print(rect.get_picture())

sq = Square(9)
print('Square of sides lengh 9 was created \n')
print(sq)
print('\n')
print('The area of this square is: \n')
print(sq.get_area())
print('\n')
print('The perimeter of this square is: \n')
print(sq.get_perimeter())
print('\n')
print('The diagonal of this square is: \n')
print(sq.get_diagonal())
print('\n')
print('This is a picture of our square: \n')
print(sq.get_picture())

