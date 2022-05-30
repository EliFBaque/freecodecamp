class Rectangle:
    def __init__(self, width, height):
        '''Initialize the rectangle'''
        self.width = width
        self.height = height
        
    def __str__(self):
        '''Return a string representation of the rectangle'''
        return f'Rectangle(width={self.width}, height={self.height})'
    
    def set_width(self, width):
        '''Set a different width'''
        self.width = width
        
    def set_height(self, height):
        '''Set a different height'''
        self.height = height
        
    def get_area(self):
        '''Return the area of the rectangle'''
        return self.width * self.height
    
    def get_perimeter(self):
        '''Return the perimeter of the rectangle'''
        return 2 * (self.width + self.height)
    
    def get_diagonal(self):
        '''Return the diagonal of the rectangle'''
        return (self.width ** 2 + self.height ** 2) ** 0.5
    
    def get_picture(self):
        '''Return a string representing the rectangle'''
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            horizontal = self.width
            vertical = self.height
            picture = ''
            
            while vertical:
                picture += ('*' * horizontal) + '\n'
                vertical -= 1
                
            return picture
    
    def get_amount_inside(self, shape):
        '''Return the amount of times a shape is inside the rectangle'''
        return self.get_area() // shape.get_area()
    
class Square(Rectangle):
    def __init__(self, side):
        '''Initialize the square'''
        super().__init__(side, side)
        
    def __str__(self):
        '''Return a string representation of the square'''
        return f'Square(side={self.width})'   
    
    def set_side(self, side):
        '''Set a different side'''
        return self.set_width(side) , self.set_height(side)
