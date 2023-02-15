from core.object3D import object3D
from core.matrix import Matrix
from numpy.linalg import inv

class Camera(object3D):
    def __init__(self,angleOfView=60, aspectRatio=1,
                 nearDistance=0.1, farDistnce=100):
        super().__init__()

        self.projectionMatrix=Matrix.perspective(angleOfView, aspectRatio, nearDistance,farDistnce)

        self.viewMatrix=Matrix.makeIdentity()

    def updateViewMatrix(self):
        self.viewMatrix=inv(self.getWorldMatrix() )

