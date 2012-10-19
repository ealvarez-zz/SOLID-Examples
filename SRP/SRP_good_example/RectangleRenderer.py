'''
@author: python
'''
from Rectangle import Rectangle
import pygame
import sys

class RectangleRenderer(Rectangle):

    def __init__(self, width, height, window_width, window_height):
        Rectangle.__init__(self, width, height)
        self.__window_height = window_height
        self.__window_width = window_width
        self.__color = (0, 184, 46)
        
    def draw(self):
        self.__init_pygame_screen(self.__window_height, self.__window_width) 
        vertexs = (50, 50, self.width, self.height)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            pygame.draw.rect(self.screen, self.__color, vertexs)
            pygame.display.flip()
    
    def __init_pygame_screen(self, screen_width, screen_height):
        pygame.init()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        
        
    