from mobs.mob import Mob
from core.GRAVITY import Gravity
from core.input import Input
from core.camera import Camera

class Player(Mob):
    def __init__(self,geometry, material):
        super().__init__(geometry,material)

        self.camera=Camera()
        self.input=Input()

        self.view=True

    def move(self,x=0,y=0,z=0,dt=1):
        x*=dt; y*=dt; z*=dt;
        self.translate(x,y,z)
        self.camera.translate(x,y,z)

    def rotate(self,x=0,y=0,z=0):

        self.camera.rotateZ(z)
        self.camera.rotateY(y)
        self.camera.rotateX(x)

        self.rotateZ(z)
        self.rotateY(y)
        self.rotateX(x)

    def setPosition(self,x,y,z):
        self.setPos(x,y,z)
        self.camera.setPos(x,y,z)

    def jump(self):
        self.gravity.impulse=0
        self.gravity.repulse=0.3

    def update(self,fps_time=1):
        self.gravity.applyGravityForce(self,fps_time=fps_time)
        self.gravity.applyGravityForce(self.camera,fps_time=fps_time)

    def toggleView(self):
        x, y, z= self.getPos()

        if self.view==True:

            self.camera.setPos(x, y+.1, z+.3)
            self.view=False

        elif self.view==False:

            self.setPosition(x,y,z)
            self.view=True