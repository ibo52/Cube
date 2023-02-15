from OpenGL.GL import *
from core.mesh import Mesh

class Renderer(object):
    def __init__(self,clearColor=[0,0,0]):
        glEnable(GL_DEPTH_TEST)
        glClearColor(clearColor[0],clearColor[1],clearColor[2], 1.0)

    def render(self, scene, camera):
        #clear buffers
        glClear(GL_COLOR_BUFFER_BIT| GL_DEPTH_BUFFER_BIT)

        #update camera view
        camera.updateViewMatrix()

        #put list of meshes in scene
        descendentList=scene.getDescendentList()

        meshFilt=lambda x: isinstance(x,Mesh)
        meshList=list( filter(meshFilt, descendentList))

        for mesh in meshList:
            #if mesh is not visible; do not render
            if not mesh.visible:
                continue;
            glUseProgram(mesh.material.programRef)

            #bind vertex array object
            glBindVertexArray(mesh.vaoRef)

            #update uniform matrices
            mesh.material.uniforms["modelMatrix"].data=mesh.getWorldMatrix()
            mesh.material.uniforms["viewMatrix"].data=camera.viewMatrix
            mesh.material.uniforms["projectionMatrix"].data=camera.projectionMatrix

            #update unifroms stored in material
            for varName, uniformObj in mesh.material.uniforms.items():
                uniformObj.uploadData()

            #update render settings
            mesh.material.updateRenderSettings()

            glDrawArrays(mesh.material.settings["drawStyle"], 0, mesh.geometry.vertexCount)
