from core.base import Base
from core.openGLUtils import OpenGLUtils
from OpenGL.GL import *
from core.attribute import Attribute
from core.uniform import Uniform
from core.matrix import Matrix

#Test class that inherited from Base class
class Test(Base):
    def initialize(self):
        print("Initialization success!")

        #vertexshader code
        vsCode="""
        in vec3 position;
        uniform mat4 projectionMatrix;
        uniform mat4 modelMatrix;
        out vec3 color;
        uniform vec3 translate;
        void main(){
            vec3 pos=position+translate;
            gl_Position=projectionMatrix*modelMatrix*vec4(position,1.0);
        }
        """

        fsCode = """
        uniform vec3 baseColor;
        out vec4 fragColor;
        void main(){
        
            gl_FragColor=vec4(baseColor.r,baseColor.g, baseColor.b, 1.0);
        }
        """

        #send code-text to GPU, compile,get the program reference
        self.programRef=OpenGLUtils.initializeProgram(vsCode, fsCode)

        #render settings(optional)
        glPointSize(16)
        glLineWidth(8)
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_DEPTH_TEST)

        #---build an vertex object-------------
        vaoRef=glGenVertexArrays(1)
        glBindVertexArray(vaoRef)

        #object vertices to create geometric shape
        positionData=[[0.0, 0.2, 0.0],
                      [0.2, -0.2, 0.0],
                      [-0.2, -0.2, 0.0]]
        #define data type as vec3 for program to interpet

        positionAttribute=Attribute("vec3",positionData)
        #concatenate positionData to "position" attribute of program
        positionAttribute.associateVariable(self.programRef,"position")

        self.vertexCount=len(positionData)
        # ---build an vertex object-------------
        ##
        #
        #
        modelMatrix=Matrix.translate(0,0,-1)
        self.modelMatrix=Uniform("mat4",modelMatrix)
        self.modelMatrix.locateVariable(self.programRef,"modelMatrix")

        projectionMatrix=Matrix.perspective()
        self.projectionMatrix=Uniform("mat4",projectionMatrix)
        self.projectionMatrix.locateVariable(self.programRef,"projectionMatrix")


        self.baseColor1=Uniform("vec3",[1.0, 0.0, 0.0])
        self.baseColor1.locateVariable(self.programRef,"baseColor")

        self.time=0
    def update(self):
        glUseProgram(self.programRef)

        #clear the screen
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #amount to move  triangle
        distance=0.01
        if self.input.isKeyPressed("left"):
            m = Matrix.translate(-distance,0, 0)
            self.modelMatrix.data = m @ self.modelMatrix.data

        if self.input.isKeyPressed("right"):
            m = Matrix.translate(distance,0, 0)
            self.modelMatrix.data = m @ self.modelMatrix.data

        if self.input.isKeyPressed("up"):
            m=Matrix.translate(0,distance,0)
            self.modelMatrix.data=m @ self.modelMatrix.data

        if self.input.isKeyPressed("down"):
            m = Matrix.translate(0, -distance, 0)
            self.modelMatrix.data = m @ self.modelMatrix.data


        #rotation section(mult as m on right for local rotation, otherwise global rotation)
        #X axis
        if self.input.isKeyPressed("u"):
            m=Matrix.rotateX(distance)
            self.modelMatrix.data=self.modelMatrix.data @ m
        if self.input.isKeyPressed("o"):
            m=Matrix.rotateX(-distance)
            self.modelMatrix.data=self.modelMatrix.data @ m

        #Y axis
        if self.input.isKeyPressed("j"):
            m=Matrix.rotateY(distance)
            self.modelMatrix.data=self.modelMatrix.data @ m
        if self.input.isKeyPressed("l"):
            m=Matrix.rotateY(-distance)
            self.modelMatrix.data=self.modelMatrix.data @ m

        self.projectionMatrix.uploadData()
        self.modelMatrix.uploadData()

        self.baseColor1.uploadData()
        # render the points to geometric shape
        glDrawArrays(GL_TRIANGLE_FAN, 0, self.vertexCount)

#create instance of this class and run
Test().run()
