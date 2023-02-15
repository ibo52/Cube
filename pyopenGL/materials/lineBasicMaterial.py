from materials.basicMaterial import basicMaterial
from OpenGL.GL import *

class LineBasicMaterial(basicMaterial):
    def __init__(self,properties={}):
        super().__init__()

        #render vertices as continuous by default

        self.settings["drawStyle"]=GL_LINE_STRIP
        self.setProperties(properties)

    def updateRenderSettings(self):
        glLineWidth(self.settings["lineWidth"])

        if self.settings["lineType"]=="connected":
            self.settings["drawStyle"]=GL_LINE_STRIP
        elif self.settings["lineType"]=="loop":
            self.settings["drawStyle"]=GL_LINE_LOOP
        elif self.settings["lineType"]=="segments":
            self.settings["drawStyle"]=GL_LINES
        else:
            raise Exception("unknown style:",self.settings["lineType"])