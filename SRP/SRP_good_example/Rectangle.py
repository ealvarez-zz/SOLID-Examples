'''
@author: Erwin Alvarez C
'''

class Rectangle(object):


    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        
    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height
    
    @property
    def area(self):
        return self.__width * self.__height