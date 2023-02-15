import pygame
from OpenGL.GL import *
from OpenGL.GLUT import glutBitmapCharacter
from OpenGL.GLUT import *
from OpenGL.GLU import *

class TextObject():
    def __init__(self, color=(1, 1, 1)):
        self.color=color
        self.font=pygame.font.SysFont("ubuntu mono",12)
        glutInit()

    def generateTextSurface(self,textToPrint):
        return self.font.render(textToPrint,False, self.color)

    def print(self, text, x, y):

        glColor3fv(self.color)
        glPushMatrix()
        #glRasterPos2f(0.5,0.125)
        glWindowPos2f(0.5,0.125)
        for ch in text:
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ctypes.c_int( ord(ch) ) )
        glPopMatrix()
    def drawScreen(self):
        glClear



