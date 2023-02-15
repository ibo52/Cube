from geometry.ellipsoidGeometry import EllipsoidGeometry

class SphereGeometry(EllipsoidGeometry):
    def __init__(self,radius=1,color=None):
        super().__init__(2*radius, 2*radius, 2*radius,color=color)
