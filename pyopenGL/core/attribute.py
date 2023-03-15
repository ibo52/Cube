import numpy
from OpenGL.GL import *

class Attribute(object):
    def __init__(self, dataType, data):
        #type of elements in the data array
        #int | float | vec2 | vec3 | vec4
        self.dataType=dataType
        self.data=data

        #reference to available bufers in GPU
        self.bufferRef=glGenBuffers(1)

        #upload data immediately
        self.uploadData()

    #upload ddata to GPU buffer
    def uploadData(self):
        #convert data to numpy format of 32bit float
        data=numpy.array(self.data).astype(numpy.float32)

        #select GPU buffer used by functions
        glBindBuffer(GL_ARRAY_BUFFER,self.bufferRef)

        #store data in currently bound buffer
        glBufferData(GL_ARRAY_BUFFER, data.ravel(), GL_STATIC_DRAW)

    #associate variable in the GPU program with this buffer
    def associateVariable(self, programRef, variableName):
        #get reference for program variable with given name
        variableRef=glGetAttribLocation(programRef, variableName)

        #if program does not reference variable; exit
        if variableRef==-1:
            return

        #select buffer used by following functions
        glBindBuffer(GL_ARRAY_BUFFER, self.bufferRef)

        #specify how data will be read
        #from the buffer currently bound to GL_ARRAY_BUFFER
        if self.dataType=="int":
            glVertexAttribPointer(variableRef,1,GL_INT,False,0,None)

        elif self.dataType=="float":
            glVertexAttribPointer(variableRef,1,GL_FLOAT,False,0,None)

        elif self.dataType=="vec2":
            glVertexAttribPointer(variableRef, 2, GL_FLOAT, False, 0, None)

        elif self.dataType=="vec3":
            glVertexAttribPointer(variableRef, 3, GL_FLOAT, False, 0, None)

        elif self.dataType=="vec4":
            glVertexAttribPointer(variableRef, 4, GL_FLOAT, False, 0, None)
        else:
            raise Exception("Unknown attribute type:",self.dataType)

        #indicate data should be streamed to variable from buffer
        glEnableVertexAttribArray(variableRef)