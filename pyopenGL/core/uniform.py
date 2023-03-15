from OpenGL.GL import *

class Uniform(object):
    def __init__(self,dataType,data):
        self.dataType=dataType

        #data to be sent to uniform variable
        self.data=data

        #reference for variable location in the program
        self.variableRef=None

    #get and store reference to uniform variable
    def locateVariable(self,programRef,variablename):
        self.variableRef=glGetUniformLocation(programRef,variablename)

    #store data in uniform variable
    def uploadData(self):
        #if variable does not exist; exit
        if self.variableRef==-1:
            return

        if self.dataType=="int":
            glUniform1i(self.variableRef,self.data)
        elif self.dataType=="bool":
            glUniform1i(self.variableRef, self.data)
        elif self.dataType=="float":
            glUniform1f(self.variableRef,self.data)
        elif self.dataType=="vec2":
            glUniform2f(self.variableRef, self.data[0], self.data[1])
        elif self.dataType=="vec3":
            glUniform3f(self.variableRef, self.data[0], self.data[1], self.data[2])
        elif self.dataType=="vec4":
            glUniform4f(self.variableRef, self.data[0], self.data[1], self.data[2], self.data[3])
        elif self.dataType=="mat4":
            glUniformMatrix4fv(self.variableRef, 1, GL_TRUE, self.data)
        elif self.dataType=="sampler2D":
            textureObjectRef,textureUnitRef=self.data
            #activate texture unit
            glActiveTexture(GL_TEXTURE0+textureUnitRef)
            #associate texture object with active texture unit
            glBindTexture(GL_TEXTURE_2D, textureObjectRef)
            #upload texture unit number to uniform variable in shader
            glUniform1i(self.variableRef,textureUnitRef)
        else:
            raise Exception("Unknown uniform data type:",self.dataType)
