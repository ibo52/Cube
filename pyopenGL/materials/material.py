from core.openGLUtils import OpenGLUtils
from core.uniform import Uniform

class Material(object):
    def __init__(self, vertexShaderCode, fragmentShaderCode):
        self.programRef=OpenGLUtils.initializeProgram(vertexShaderCode,fragmentShaderCode)

        #store niform objects
        self.uniforms={}

        #standard uniform objects(matrices)
        self.uniforms["modelMatrix"]=Uniform("mat4",None)
        self.uniforms["viewMatrix"]=Uniform("mat4",None)
        self.uniforms["projectionMatrix"]=Uniform("mat4",None)

        #openGL render gettings
        self.settings={}
        self.settings["drawStyle"]=None

    #initialize all uniform variable references
    def locateUniforms(self):
        for varName,uniformObj in self.uniforms.items():
            uniformObj.locateVariable(self.programRef, varName)

    #configure openGL render settings
    def updateRenderSettings(self):
        pass

    def setProperties(self,properties={}):
        for name,data in properties.items():
            #update uniforms
            if name in self.uniforms.keys():
                self.uniforms[name].data=data

            elif name in self.settings.keys():
                self.settings[name].data = data
            else:
                raise Exception("Material has no property:",name)