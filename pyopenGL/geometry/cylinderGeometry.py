from geometry.cylindricalGeometry import CylindricalGeometry

class CylinderGeo(CylindricalGeometry):

    def __init__(self,radius=1, height=1, radialSegments=16,
                 heightSegments=8,color=None):

        super().__init__(radius,radius, height, radialSegments, heightSegments,color=color)
