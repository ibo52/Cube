from geometry.geometry import Geometry
from random import randint

class ParametricGeometry(Geometry):
    """
    recurse the geometry on given axes

    @param uInit: horizontal start position of geometry
    @param uInit: horizontal end position of geometry
    @param uResolution recursion size on horizontal axis

    @param vInit: vertical start position of geometry
    @param vInit: vertical end position of geometry
    @param vResolution recursion size on vertical axis
    """
    def __init__(self, uInit, uEnd, uResolution,
                       vInit, vEnd, vResolution, S, color:list=None):

        super().__init__()
        #generate a set of points on the function
        deltaU=(uEnd-uInit)/uResolution
        deltaV=(vEnd-vInit)/vResolution

        positions=[]
        uvs=[]

        for uIndex in range(uResolution+1):
            vArray=[]
            texArray=[]
            for vIndex in range(vResolution+1):
                u=uInit+uIndex*deltaU
                v=vInit+vIndex*deltaV
                vArray.append( S(u,v) )

                u_=uIndex/uResolution
                v_ = vIndex / vResolution
                texArray.append([u_,v_])

            positions.append(vArray)
            uvs.append(texArray)

        """for uIndex in range(uResolution+1):
            vArray=[]
            for vIndex in range(vResolution+1):
                u=uIndex/uResolution
                v=vIndex/vResolution
                vArray.append([u,v])
            uvs.append(vArray)"""
        #store vertex data
        positionData=[]
        colorData=[]
        uvData=[]

        #default vertex colors
        c1,c2,c3=[1,0,0],[0,1,0],[0,0,1]
        c4,c5,c6=[0,1,1],[1,0,1],[1,1,0]

        #group vertex data into triangles(triangles is better for faster GPU processing)
        for xIndex in range(uResolution):
            for yIndex in range(vResolution):
                #position data
                pA=positions[xIndex][yIndex]
                pB=positions[xIndex+1][yIndex]
                pC=positions[xIndex+1][yIndex+1]
                pD=positions[xIndex][yIndex+1]

                r=randint(0,50)
                positionData += [pA,pB,pC, pA,pC,pD]

                if color!=None:
                    colorData+=[color[:3]*3, color[3:]*3, color[:3]*3, color[3:]*3]
                else:
                    colorData +=[c1,c2,c3 ,c4,c5,c6]

                #texture data
                uvA = uvs[xIndex][yIndex]
                uvB = uvs[xIndex + 1][yIndex]
                uvC = uvs[xIndex + 1][yIndex + 1]
                uvD = uvs[xIndex][yIndex + 1]

                uvData=[uvA,uvB,uvC, uvA,uvC,uvD]


        self.addAttribute("vec3","vertexPosition",positionData)
        self.addAttribute("vec3","vertexColor",colorData)
        self.addAttribute("vec2","vertexUV",uvData)
        self.countVertices()

