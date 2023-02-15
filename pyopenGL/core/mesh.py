from core.object3D import object3D
from OpenGL.GL import *

class Mesh(object3D):
    def __init__(self, geometry, material):
        super().__init__()

        self.geometry=geometry
        self.material=material

        #determines if this object be rendered
        self.visible=True

        #set up associatins betweem attributes in geometry
        # and shader variables in material
        self.vaoRef=glGenVertexArrays(1)#open buffer on GPU
        glBindVertexArray(self.vaoRef)#bring GPU array on to process data over it

        for varName, attributeObj, in geometry.attributes.items():
            attributeObj.associateVariable(material.programRef,varName)

        #unbind vertex array obj
        glBindVertexArray(0)