'''
Created on Oct 5, 2012

@author: Erwin Alvarez C
'''

import pygame
import sys

class Rectangle:
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    # Dibuja un rectangulo verde en una ventana de 640x480 pixeles
    def draw(self):
        self.init_pygame_screen(640, 480)
        color = (0, 184, 46)
        vertexs = (50, 50, self.width, self.height)
        pygame.draw.rect(self.screen, color, vertexs)
        pygame.display.flip()
    
    def init_pygame_screen(self, screen_width, screen_height):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))

    def area(self):
        return self.height * self.width

if __name__ == '__main__':
    
    rectangle = Rectangle(200, 300)
    print(rectangle.area())
    while True:
        rectangle.draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        

