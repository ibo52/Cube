from core.attribute import Attribute

class Geometry(object):
    def __init__(self):
        #dictionary to store the attribute objs

        self.attributes={}

        #num of vertices
        self.vertexCount=None

    def countVertices(self):
        #attribute objects array of data
        attrib=list(self.attributes.values())[0]
        self.vertexCount=len( attrib.data )

    def addAttribute(self, dataType,varName,varData):
        self.attributes[varName]=Attribute(dataType,varData)

