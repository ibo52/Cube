import pygame
import sys
from core.input import Input


class Base(object):
    def __init__(self):
        pygame.init()
        pygame.font.init()
        #define window size
        self.SCREEN_SIZE=(720,720)
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)

        #indicate rendering options
        displayFlags=pygame.DOUBLEBUF|pygame.OPENGL

        #create and display window
        self.screen=pygame.display.set_mode(self.SCREEN_SIZE,displayFlags)
        #set window title
        pygame.display.set_caption("ESC or Q to quit")

        #main loop flag
        self.running=True

        #clock
        self.clock=pygame.time.Clock()
        self.FPS=60

        #manage user inputs
        self.input=Input()

    #below functions is for extending classess that inherits this base class
    def initialize(self):
        pass

    def update(self):
        pass

    def run(self):
        #start program
        self.initialize()

        #main loop
        while self.running:

            #process stage
            #check for pressed keys
            self.input.update()

            if self.input.quit:
                self.running=False

            #update input
            self.update()

            #render

            # constant clock to FPS
            self.clock.tick()

            #display
            pygame.display.flip()

        #exit
        pygame.quit()
        sys.exit()