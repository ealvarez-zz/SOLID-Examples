'''
@author: Erwin Alvarez C
'''

class Rectangle(object):


    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
    
    def area(self):
        return self.width * self.height