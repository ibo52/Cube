from core.mesh import Mesh
class Gravity:
    def __init__(self):
        self.g=0.0005#gravitational force

        self.impulse=0
        self.repulse=0

    #create gravitational acceleration on geometries
    def applyGravityForce(self, obj:Mesh,fps_time=1):
        objY=obj.getPos()[1]

        self.impulse += self.g * fps_time/2

        #if collided (simulation)
        if objY<=0:
            obj.setPosY(0.0)

            if (self.impulse<(self.g * fps_time/2) and self.repulse<(self.g * fps_time/2)):
                self.repulse=0
            else:
                self.repulse=self.impulse/2.5
                print("rep",self.repulse,"imp",self.impulse)

            self.impulse=0

        self.reaction(obj, (self.impulse - self.repulse))


    def reaction(self, obj:Mesh,forceToApply,affectionAxis=[0,1,0]):

        if affectionAxis[0]:
            objX = obj.getPos()[0]
            obj.setPosX(objX - forceToApply)

        if affectionAxis[1]:
            objY = obj.getPos()[1]
            obj.setPosY(objY - forceToApply)

        if affectionAxis[2]:
            objZ = obj.getPos()[2]
            obj.setPosZ(objZ - forceToApply)

        """
    def collision(self,obj:Mesh, worldList):

        objPos=obj.getPos()
        objVertices = list(obj.geometry.attributes.values())[0]
        #
        #
        for anyObj in worldList:

            anyObjPos=anyObj.getPos()
            anyObjVertices=list(anyObj.geometry.attributes.values())[0]


            x_col=objPos.item((0,3))>= anyObjPos.item((0,3))
            y_col = objPos.item((0, 3)) >= anyObjPos.item((0, 3))
            z_col = objPos.item((0, 3)) >= anyObjPos.item((0, 3))
            
    """
