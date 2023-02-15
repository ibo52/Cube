from core.base import Base
from core.openGLUtils import OpenGLUtils
from OpenGL.GL import *
from core.attribute import Attribute
from core.uniform import Uniform
from math import sin

#Test class that inherited from Base class
class Test(Base):
    def initialize(self):
        print("Initialization success!")

        #vertexshader code
        vsCode="""
        in vec3 position;
        out vec3 color;
        uniform vec3 translate;
        void main(){
            vec3 pos=position+translate;
            gl_Position=vec4(pos.x, pos.y, pos.z, 1.0);
        }
        """

        fsCode = """
        uniform vec3 baseColor;
        void main(){
        
            gl_FragColor=vec4(baseColor.r,baseColor.g, baseColor.b, 1.0);
        }
        """

        #send code-text to GPU, compile,get the program reference
        self.programRef=OpenGLUtils.initializeProgram(vsCode, fsCode)

        #render settings(optional)
        glPointSize(16)
        glLineWidth(8)
        glClearColor(0.6, 0.6, 0.6, 1.0)

        #---build an vertex object-------------
        vaoRef=glGenVertexArrays(1)
        glBindVertexArray(vaoRef)

        #object vertices to create geometric shape
        positionData=[[0., 0.2,0.0],
                      [0.2, -0.2, 0.0],
                      [-0.2, -0.2, 0.0]]
        #define data type as vec3 for program to interpet

        positionAttribute=Attribute("vec3",positionData)
        #concatenate positionData to "position" attribute of program
        positionAttribute.associateVariable(self.programRef,"position")

        self.vertexCount=len(positionData)
        # ---build an vertex object-------------

        self.translate1=Uniform("vec3",[-0.5, 0.0, 0.0])
        self.translate1.locateVariable(self.programRef,"translate")

        self.translate2 = Uniform("vec3", [0.5, 0.0, 0.0])
        self.translate2.locateVariable(self.programRef, "translate")

        self.baseColor1=Uniform("vec3",[1.0, 0.0, 0.0])
        self.baseColor1.locateVariable(self.programRef,"baseColor")

        self.baseColor2 = Uniform("vec3", [0.0, 0.5, 0.5])
        self.baseColor2.locateVariable(self.programRef, "baseColor")

        self.time=0
    def update(self):
        glUseProgram(self.programRef)

        #clear the screen
        glClear(GL_COLOR_BUFFER_BIT)

        #amount to move  triangle
        distance=0.01
        if self.input.isKeyPressed("left"):
            self.translate2.data[0]-=distance

        if self.input.isKeyPressed("right"):
            self.translate2.data[0]+=distance

        if self.input.isKeyPressed("up"):
            self.translate2.data[1]+=distance

        if self.input.isKeyPressed("down"):
            self.translate2.data[1]-=distance

        self.time+=1/self.FPS
        self.translate1.data[1]=(sin(self.time)+1)/2

        self.translate1.uploadData()
        self.baseColor1.uploadData()

        #render the points to geometric shape
        glDrawArrays(GL_TRIANGLE_FAN, 0, self.vertexCount)

        self.baseColor2.data[2]=(sin(self.time)+1)/2
        self.translate2.uploadData()
        self.baseColor2.uploadData()
        # render the points to geometric shape
        glDrawArrays(GL_TRIANGLE_FAN, 0, self.vertexCount)

#create instance of this class and run
Test().run()
