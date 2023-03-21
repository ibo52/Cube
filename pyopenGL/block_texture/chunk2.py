import random

from OpenGL.GL import *
from geometry.boxGeometry import BoxGeometry

SIZE_BLK=1#size of individual block

#default chunk values
CHUNK_WIDTH=16
CHUNK_HEIGHT=16
CHUNK_DEPTH=16

class ChunkGeometry(BoxGeometry):
    def __init__(self, width=CHUNK_WIDTH, height=CHUNK_HEIGHT, depth=CHUNK_DEPTH,position=[0,0,0], color: list = None,imgParse=1,generateList=None):
        super().__init__()

        # colors
        C1 = C2 = [0, 0, 1]
        C3 = C4 = [1, 1, 0]
        C5 = C6 = [1, 0, 0]
        C7 = C0 = [1, 0, 1]


        positionData=[]
        colorData=[]
        uvData=[]

        imgUVBuff={}#side,side,top,bottom,side
        if imgParse<1:
            imgParse=1
        else:
            r_=1/imgParse
            for _ in range(imgParse):
                k=(_*r_)
                T0, T1, T2, T3 = [k, 0], [r_+k, 0], [k, 1], [r_+k, 1]
                imgUVBuff[ f"{_}" ]=[T0, T1, T3, T0,T3, T2]

        for x in range(position[0],width+position[0]):
            for y in range(position[1],height+position[1]):
                for z in range(position[2],depth+position[2]):
                    #random hollows at ground
                    if y>generateList[ position[0]-x ] or y>generateList[ position[2]-z ] :
                        continue

                    P0 = [x / SIZE_BLK, y / SIZE_BLK, z / SIZE_BLK]
                    P1 = [(x+1) / SIZE_BLK, y / SIZE_BLK, z / SIZE_BLK]
                    P2 = [x / SIZE_BLK, (y+1) / SIZE_BLK, z / SIZE_BLK]
                    P3 = [(x+1) / SIZE_BLK, (y+1) / SIZE_BLK, z / SIZE_BLK]

                    P4 = [x / SIZE_BLK, y / SIZE_BLK, (z+1) / SIZE_BLK]
                    P5 = [(x+1) / SIZE_BLK, y / SIZE_BLK, (z+1) / SIZE_BLK]
                    P6 = [x / SIZE_BLK, (y+1) / SIZE_BLK, (z+1) / SIZE_BLK]
                    P7 = [(x+1)/ SIZE_BLK, (y+1) / SIZE_BLK, (z+1) / SIZE_BLK]

                    positionData +=[P5, P1, P3, P5, P3, P7, P0, P4, P6, P0, P6, P2,
                                    P6, P7, P3, P6, P3, P2, P0, P1, P5, P0, P5, P4,
                                    P4, P5, P7, P4, P7, P6, P1, P0, P2, P1, P2, P3]

                    if color != None:
                        colorData = color
                    else:
                        colorData += [C1] * 6 + [C2] * 6 + [C3] * 6 + [C4] * 6 + [C5] * 6 + [C6] * 6

                    # texture data
                    #T0, T1, T2, T3 = [0, 0], [1, 0], [0, 1], [1, 1]
                    #uvData += [T0, T1, T3, T0, T3, T2] * 6
                    if imgParse==3:
                        side, top,bottom = imgUVBuff.values()
                        uvData += [side, side, top, bottom, side,side]
                    elif imgParse==2:
                        side,top_bottom=imgUVBuff.values()
                        uvData += [side, side, top_bottom, top_bottom, side,side]
                    else:#default: accept dict has one element
                        uvData += [imgUVBuff["0"]*6]
        self.addAttribute("vec3", "vertexPosition", positionData)
        self.addAttribute("vec3", "vertexColor", colorData)
        self.addAttribute("vec2", "vertexUV", uvData)
        self.countVertices()


