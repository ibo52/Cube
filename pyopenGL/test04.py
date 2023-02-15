import random

import pygame.mouse

from core.base import Base
from core.renderer import Renderer
from core.object3D import Scene,Group
from core.camera import Camera
from core.mesh import Mesh

from geometry.boxGeometry import BoxGeometry
from geometry.planeGeometry import PlaneGeometry
from geometry.parametricGeometry import ParametricGeometry
from geometry.cylinderGeometry import CylinderGeo
from geometry.prismGeometry import PrismGeometry
from geometry.ellipsoidGeometry import EllipsoidGeometry
from geometry.sphereGeometry import SphereGeometry
from materials.surfaceBasicMaterial import SurfaceBasicMaterial
#
#
#
from core.GRAVITY import Gravity
from numpy import sin,cos,pi

#render a  scene
class Test(Base):
    def initialize(self):
        print("Test class initialized and started")

        self.renderer=Renderer()
        self.scene=Scene
        self.camera=Camera()

        material=SurfaceBasicMaterial({"useVertexColors":1})

        self.sphere=Mesh(SphereGeometry(),material)
        self.sphere2=Mesh(SphereGeometry(color=[random.random() for a in range(6)]),material)
        self.ellipse=Mesh(EllipsoidGeometry(1,2,1,color=[random.random() for a in range(6)]),material)

        self.box=Mesh(BoxGeometry(color=[random.random() for a in range(108)]),material)
        self.box2=Mesh(BoxGeometry(),material)

        self.plane=Mesh(PlaneGeometry(width=6,height=6,color=[1,1,1,0,0,0]),material)

        self.cylinder=Mesh(CylinderGeo(color=[random.random() for a in range(6)]),material)
        self.prism=Mesh(PrismGeometry(color=[random.random() for a in range(6)]),material)

        self.sphere.setPos(0,12,0)
        self.sphere2.setPos(-2,12,2)
        self.sphere2.rotateX(90)
        self.ellipse.setPos(-2, 15, -3)

        self.box.setPos(2, 16, 0)
        self.box.rotateX(0.28)
        self.box.rotateY(0.14)

        self.box2.setPos(1,18,3)
        self.box.rotateY(0.36)
        self.box.rotateZ(0.56)

        self.plane.rotateX(pi/2)
        self.plane.setPos(0,-1,0)

        self.cylinder.setPos(-2,0,-2)
        self.prism.setPos(3.5,0.5, 1)


        self.scene.add(self.sphere)
        self.scene.add(self.sphere2)
        self.scene.add(self.ellipse)
        self.scene.add(self.box)
        self.scene.add(self.box2)
        self.scene.add(self.plane)
        self.scene.add(self.cylinder)
        self.scene.add(self.prism)

        #all objects at origin at first
        #pull camera towards viewver
        self.camera.setPos(0,0,10)
        self.camera.rotateX(pi/8)


        self.worldList=[self.box,self.box2,self.sphere,self.sphere2,self.ellipse,
                        self.cylinder,self.prism]

        self.gravity=[Gravity() for a in range(len(self.worldList))]

    def update(self):
        for idx in range(len(self.worldList)):
            self.gravity[idx].affectForce( self.worldList[idx] )

        #---------camera movement-----------------
        if self.input.isKeyPressed("w"):
            self.camera.translate(0.00, 0, -0.04)
        if self.input.isKeyPressed("s"):
            self.camera.translate(0.00, 0, 0.04)
        if self.input.isKeyPressed("a"):
            self.camera.translate(-0.04, 0, 0)
        if self.input.isKeyPressed("d"):
            self.camera.translate(0.04, 0, 0.0)


        # check if mouse buttons pressed
        mList = pygame.mouse.get_pressed()
        mouseP = pygame.mouse.get_rel()  # relative mouse pos

        if pygame.mouse.get_focused():
            self.camera.rotateX(-mouseP[1] / 100.0)
            self.camera.rotateY(-mouseP[0] / 100.0)
        # ---------camera movement-----------------
        """
        scaleFactor=self.input.isMouseWheelPressed()
        if scaleFactor==1:
            self.mesh.scale(1.005)
        elif scaleFactor==-1:
            self.mesh.scale(0.995)
        
        """

        self.renderer.render(self.scene, self.camera)

        if self.input.isKeyPressed("escape") or self.input.isKeyPressed("q"):
            self.input.quit=True


Test().run()
