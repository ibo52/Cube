from geometry.geometry import Geometry
from core.attribute import Attribute

class rectangleGeometry(Geometry):
    def __init__(self,width=1, height=1):
        super().__init__()

        #vertice points
        P0 = [-width/2, -height/2, 0]
        P1 = [width / 2, -height / 2, 0]
        P2 = [-width / 2, height / 2, 0]
        P3 = [width / 2, height / 2, 0]

        #colors
        C0 = [0 ,0 ,1]
        C1 = [1, 1, 0]
        C2 = [1, 0, 0]
        C3 = [1, 0, 1]

        #draw rect object as triangles
        positionData=[P0, P1, P3, P0, P3, P2 ]

        colorData = [C0, C1, C3, C0, C3, C2 ]

        #texture data
        T0,T1,T2,T3=[0,0],[1,0],[0,1],[1,1]
        uvData=[T0,T1,T3, T0,T3,T2]

        self.addAttribute("vec3","vertexPosition",positionData)
        self.addAttribute("vec3","vertexColor",colorData)
        self.addAttribute("vec2","vertexUV",uvData)
        self.countVertices()

