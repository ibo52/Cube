from geometry.geometry import Geometry
from math import sin,cos,pi
from random import randint

class PolygonGeometry(Geometry):
    def __init__(self,sides=3, radius=1 ):
        super().__init__()

        angle=2*pi/sides

        positionData=[]
        colorData=[]
        uvData=[]

        for n in range(sides):
            positionData.append( [0,0,0] )
            positionData.append( [ radius*cos(angle*n), radius*sin(angle*n), 0 ] )
            positionData.append([radius * cos(angle * (n+1)), radius * sin(angle * (n+1)), 0])

            r=[randint(0,255)/255.0, randint(0,255)/255.0, randint(0,255)/255.0]
            colorData+=r,r,r

            uvData.append([0.5,0.5])
            uvData.append([ cos(angle * n)*0.5 +0.5, sin(angle * n)*0.5 +0.5 ])
            uvData.append( [cos(angle * (n+1))*0.5 +0.5, sin(angle * (n+1))*0.5 +0.5 ] )

        self.addAttribute("vec3","vertexPosition",positionData)
        self.addAttribute("vec3","vertexColor", colorData)
        self.addAttribute("vec2","vertexUV",uvData)
        self.countVertices()

