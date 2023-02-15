from geometry.cylindricalGeometry import CylindricalGeometry

class PrismGeometry(CylindricalGeometry):
    def __init__self(self,radius, height,sides=4, heightSegmets=3,color=None):
        super().__init__(radius,radius,height,sides,heightSegmets,color=color)