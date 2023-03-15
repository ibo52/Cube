from materials.material import Material
from OpenGL.GL import *

class TextureMaterial(Material):
    def __init__(self,texture,properties={}):
        vertexShaderCode="""
        uniform mat4 projectionMatrix;
        uniform mat4 viewMatrix;
        uniform mat4 modelMatrix;
        in vec3 vertexPosition;
        in vec2 vertexUV;
        out vec2 UV;
        
        void main(){
            gl_Position = projectionMatrix*viewMatrix*modelMatrix*vec4(vertexPosition,1);
            UV=vertexUV;
        }"""

        fragmentShaderCode="""
        uniform vec3 baseColor;
        uniform sampler2D texture;
        in vec2 UV;
        out vec4 fragColor;
        
        void main(){
            vec4 color=vec4(baseColor,1);
            fragColor=color * texture2D(texture,UV);
        }"""

        super().__init__(vertexShaderCode, fragmentShaderCode)

        self.addUniform("vec3","baseColor",[1,1,1])
        self.addUniform("sampler2D","texture",[texture.textureRef,1])
        self.locateUniforms()

        #setting:render both sides
        self.settings["doubleSide"]=False
        self.settings["drawStyle"] = GL_TRIANGLES
        #setting:render triangles as wireframe
        self.settings["wireframe"]=False
        #wireframe thickness
        self.settings["lineWidth"]=2

        self.setProperties(properties)

    def updateRenderSettings(self):
        if self.settings["doubleSide"]:
            glDisable(GL_CULL_FACE)
        else:
            glEnable(GL_CULL_FACE)

        if self.settings["wireframe"]:
            glPolygonMode(GL_FRONT_AND_BACK,GL_LINE)
        else:
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

        glLineWidth(self.settings["lineWidth"])
