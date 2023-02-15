from core.base import Base
from core.openGLUtils import OpenGLUtils
from OpenGL.GL import *
from core.attribute import Attribute

#Test class that inherited from Base class
class Test(Base):
    def initialize(self):
        print("Initialization success!")

        #vertexshader code
        vsCode="""
        in vec3 position;
        void main(){
            gl_Position=vec4(position.x, position.y, position.z, 1.0);
        }
        """

        fsCode = """
                void main(){
                    gl_FragColor=vec4(0.0, 1.0, 1.0, 1.0);
                }
                """

        #send code-text to GPU, compile,get the program reference
        self.programRef=OpenGLUtils.initializeProgram(vsCode, fsCode)

        #render settings(optional)
        glPointSize(16)
        glLineWidth(8)

        #---build an vertex object-------------
        vaoRef=glGenVertexArrays(1)
        glBindVertexArray(vaoRef)

        #object vertices to create geometric shape
        positionData=[[0.8, 0.0,0.0],
                      [0.4, 0.6, 0.0],
                      [-0.4, 0.6, 0.0],
                      [-0.8, 0.0, 0.0],
                      [-0.4, -0.6, 0.0],
                      [0.4, -0.6, 0.0]]
        #define data type as vec3 for program to interpet

        positionAttribute=Attribute("vec3",positionData)
        #concatenate positionData to "position" attribute of program
        positionAttribute.associateVariable(self.programRef,"position")

        self.vertexCount=len(positionData)
        # ---build an vertex object-------------

    def update(self):
        glUseProgram(self.programRef)

        #render the points to geometric shape
        glDrawArrays(GL_TRIANGLE_FAN, 0, self.vertexCount)

#create instance of this class and run
Test().run()
