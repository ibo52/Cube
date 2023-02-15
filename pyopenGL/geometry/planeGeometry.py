from geometry.parametricGeometry import ParametricGeometry

class PlaneGeometry(ParametricGeometry):
    def __init__(self,width=1,height=1,wResolution=8,hResolution=8, color=None):
        def S(u,v):
            return [u,v,0]
        super().__init__(-width,width,wResolution,
                         -height,height,hResolution, S,color=color)