from core.mesh import Mesh
class Gravity:
    def __init__(self):
        self.g=0.0005#gravitational force
        self.t=0

        self.impulse=0
        self.repulse=0

        self.direction=1

    #create gravitational acceleration on geometries
    def affectForce(self,obj:Mesh):
        objY=obj.getPos()[1]

        if self.direction==1:
            self.impulse=self.g*(self.t**2)/2
            self.reaction(obj,self.impulse)
            self.t+=1

            if objY<=0:
                self.direction=-1
                self.repulse=self.impulse/3.
                self.t=0

        else:
            self.impulse=self.g*(self.t**2)/2

            if self.impulse>=self.repulse:
                self.t=0
                self.direction=1
                self.reaction(obj,-(self.impulse-self.repulse))#last time repulse

            self.reaction(obj, - abs(self.repulse-self.impulse))
            self.t+=1

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
