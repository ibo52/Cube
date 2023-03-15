from core.mesh import Mesh
from core.GRAVITY import Gravity
class Mob(Mesh):
    def __init__(self,geometry, material):
        super().__init__(geometry,material)

        self.mass=75
        self.a=0.002
        self.velocity=0
        self.time=0

        self.gravity=Gravity()

    def move(self,x=0,y=0,z=0):
        self.translate(x,y,z)

    def update(self,fps_time=1):
        self.gravity.applyGravityForce(self,fps_time=fps_time)
