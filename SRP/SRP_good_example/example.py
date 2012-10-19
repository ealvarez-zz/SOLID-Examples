'''
@author: Erwin Alvarez C
'''
from Rectangle import Rectangle
from RectangleRenderer import RectangleRenderer

if __name__ == '__main__':
    
    width = 200
    height = 300
    
    window_width = 640
    window_height = 480
    
    # La unica responsabilidad de un Rectagle es hacer calculos geometricos
    rectangle = Rectangle(width, height)
    print("Area de primer rectangulo {0}".format(rectangle.area))
    
    # Si deseo dibujar, debo instanciar RentangleRenderer en su lugar
    rectangle_render = RectangleRenderer(width, height, window_height, window_width)
    print("Area de segundo rectangulo {0}".format(rectangle_render.area))
    rectangle_render.draw()
    
    
    
    
