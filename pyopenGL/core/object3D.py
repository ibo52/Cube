from core.matrix import Matrix

class object3D(object):
    def __init__(self):
        self.transform=Matrix.makeIdentity()
        self.parent=None
        self.children=[]

    def add(self,child):
        self.children.append(child)
        child.parent=self

    def remove(self,child):
        self.remove(child)
        child.parent=None

    #calculate transformation  of this object3D relative
    # to the rootobject3D of scene graph
    def getWorldMatrix(self):
        if self.parent==None:
            return self.transform
        else:
            return self.parent.getWorldMatrix()@self.transform

    #return a single list containing all descendents
    def getDescendentList(self):
        #master list of all descendant nodes
        descedants=[]
        #nodes to be added to descendant list,
        # wose children will be added to this list
        nodesToProcess=[self]

        while len(nodesToProcess)>0:
            #remove first node from list
            node=nodesToProcess.pop(0)
            descedants.append(node)

            nodesToProcess=node.children+nodesToProcess
        return descedants

    #apply geometric transfromations to object matrix
    def applyMatrix(self, matrix, localCoord=True):
        if localCoord:
            self.transform=self.transform@matrix

        else:
            self.transform=matrix@self.transform

    def translate(self, x, y, z ,localCoord=True):
        m=Matrix.translate(x,y,z)
        self.applyMatrix(m, localCoord)

    def rotateX(self, angle,localCoord=True):
        m=Matrix.rotateX(angle)
        self.applyMatrix(m, localCoord)

    def rotateY(self, angle,localCoord=True):
        m=Matrix.rotateY(angle)
        self.applyMatrix(m, localCoord)

    def rotateZ(self, angle,localCoord=True):
        m=Matrix.rotateZ(angle)
        self.applyMatrix(m, localCoord)

    def scale(self, factor, localCoord=True):
        m=Matrix.scale(factor)
        self.applyMatrix(m, localCoord)

    #get/seet position components of transform
    def getPos(self):
        return [self.transform.item((0,3)),
                self.transform.item((1,3)),
                self.transform.item((2,3))]

    def setPos(self,x,y,z):
        self.transform.itemset((0, 3), x)
        self.transform.itemset((1, 3), y)
        self.transform.itemset((2, 3), z)

    # to insert gravitational force to Y-axis
    def setPosX(self, x):
        self.transform.itemset((0, 3), x)

    #to insert gravitational force to Y-axis
    def setPosY(self,y):
        self.transform.itemset((1,3), y)

    # to insert gravitational force to Y-axis
    def setPosZ(self, z):
        self.transform.itemset((2, 3), z)


Scene=object3D()
Group=object3D()

