import numpy
import numpy as np


class Matrix(object):

    @staticmethod
    def makeIdentity():
        return numpy.array([[1, 0, 0 ,0],
                            [0, 1, 0 ,0],
                            [0, 0, 1 ,0],
                            [0, 0, 0 ,1]]).astype(float)

    @staticmethod
    def translate(x, y, z):
        return numpy.array([[1, 0, 0 ,x],
                            [0, 1, 0 ,y],
                            [0, 0, 1 ,z],
                            [0, 0, 0 ,1],]).astype(float)

    @staticmethod
    def rotateX(angle):
        cosa=np.cos(angle)
        sina=np.sin(angle)

        return numpy.array([[1, 0, 0, 0],
                            [0, cosa, -sina, 0],
                            [0, sina, cosa, 0],
                            [0, 0, 0, 1]]).astype(float)

    @staticmethod
    def rotateY(angle):
        cos = np.cos(angle)
        sin = np.sin(angle)

        return numpy.array([[cos, 0, sin, 0],
                            [0, 1, 0, 0],
                            [-sin, 0, cos, 0],
                            [0, 0, 0, 1]]).astype(float)

    @staticmethod
    def rotateZ(angle):
        cosa = np.cos(angle)
        sina = np.sin(angle)

        return numpy.array([[cosa, -sina, 0, 0],
                            [sina, cosa, 0, 0],
                            [0, 0, 1, 0],
                            [0, 0, 0, 1]]).astype(float)

    @staticmethod
    def scale(factor):
        return numpy.array([[factor, 0, 0, 0],
                            [0, factor, 0, 0],
                            [0, 0, factor, 0],
                            [0, 0, 0, 1]]).astype(float)

    @staticmethod
    def perspective(angleOfView=60, aspectRatio=1, nearDistance=0.1, farDistance=100):
        a=np.radians(angleOfView)#angle*pi/180
        d=1.0/np.tan(a/2)
        r=aspectRatio
        b=(farDistance+nearDistance)/(nearDistance-farDistance)
        c=2*farDistance*nearDistance/(nearDistance-farDistance)

        return numpy.array([[d/r, 0, 0, 0],
                            [0, d, 0, 0],
                            [0, 0, b, c],
                            [0, 0, -1, 0]]).astype(float)
