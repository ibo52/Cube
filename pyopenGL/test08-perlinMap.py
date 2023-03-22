import random

import pygame.mouse

from core.base import Base
from core.renderer import Renderer
from core.object3D import Scene,Group
from core.camera import Camera
from core.mesh import Mesh
from core.texture import Texture

from geometry.boxGeometry import BoxGeometry
from geometry.planeGeometry import PlaneGeometry
from geometry.cylinderGeometry import CylinderGeo
from geometry.prismGeometry import PrismGeometry
from geometry.ellipsoidGeometry import EllipsoidGeometry
from geometry.sphereGeometry import SphereGeometry
from geometry.rectangleGeometry import rectangleGeometry

from materials.surfaceBasicMaterial import SurfaceBasicMaterial
from materials.pointBasicMaterial import PointBasicMaterial
from materials.lineBasicMaterial import LineBasicMaterial
from materials.textureMaterial import TextureMaterial
#
#
#
from core.GRAVITY import Gravity
from mobs.mob import Mob
from mobs.player import Player
from numpy import sin,cos,pi

from block_texture.chunk import ChunkGeometry
from block_texture.chunkGenerator2 import WorldGenerator
#render a  scene
from datetime import datetime as time
from threading import Thread
class Test(Base):
    def initialize(self):
        print("Test class initialized and started")
        start=time.now()

        self.renderer=Renderer()
        self.scene=Scene
        self.camera=Player(ChunkGeometry(1,2,1), SurfaceBasicMaterial({"useVertexColors":1}))#Camera()

        material=SurfaceBasicMaterial({"useVertexColors":1})

        #all objects at origin at first
        #pull camera towards viewer
        self.camera.setPosition(8,20,8)
        self.camera.rotate(y=-pi/2)
        #self.scene.add(self.camera)

        skyDistance=100
        skyGeo = BoxGeometry(skyDistance,skyDistance,skyDistance)
        skyTexture=Texture("block_texture/sky.jpg")
        skyTexMat=TextureMaterial(skyTexture,{"doubleSide":True})
        self.sky=Mesh(skyGeo,skyTexMat)
        self.scene.add(self.sky)

        print("chunks will be generated please wait..")
        self.generator=WorldGenerator(self.scene)
        self.generator.generate(CHUNK_SIZE=4)

        print("data loaded to scene. elapsed time:",time.now()-start)

    def update(self):

        dt=self.clock.get_time()
        playerPos=self.camera.getPos()

        print("draw time:",dt,"FPS:",self.clock.get_fps(),"player position:",playerPos)
        #---------camera movement-----------------
        if self.input.isKeyPressed("w"):
            self.camera.move(0.0, 0, -0.02,dt)

        if self.input.isKeyPressed("s"):
            self.camera.move(0.0, 0, 0.02,dt)

        if self.input.isKeyPressed("a"):
            self.camera.move(-0.02, 0, 0,dt)

        if self.input.isKeyPressed("d"):
            self.camera.move(0.02, 0, 0.0,dt)

        if self.input.isKeyDown("space"):
            print("space press")
            self.camera.jump()

        x,y,z=self.camera.getPos()
        self.sky.setPos(x,y,z)
        """if self.input.isKeyUp("c"):
            self.camera.toggleView()"""

        # check if mouse buttons pressed
        mList = pygame.mouse.get_pressed()
        mouseP = pygame.mouse.get_rel()  # relative mouse pos

        if pygame.mouse.get_focused():
            self.camera.rotate(-mouseP[1] / 100.0, -mouseP[0] / 100.0)

        # ---------camera movement-----------------
        """
        scaleFactor=self.input.isMouseWheelPressed()
        if scaleFactor==1:
            self.mesh.scale(1.005)
        elif scaleFactor==-1:
            self.mesh.scale(0.995)
        
        """

        self.renderer.render(self.scene, self.camera.camera)

        if self.input.isKeyPressed("escape") or self.input.isKeyPressed("q"):
            self.input.quit=True


Test().run()
