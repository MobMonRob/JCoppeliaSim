import math
import coppeliaManager

class EuclidViewerCoppelia(coppeliaManager.CoppeliaManager):

    def setObjectProperties(self, location, color, label, objectHandle):
        self.setObjectPosition(objectHandle, location[0], location[1], location[2])
        self.setObjectColor(objectHandle, color[0], color[1], color[2])
        self.setObjectLabel(objectHandle, label)   

    def addSphere(self, location, radius, color, label, transparency):
        # CoppeliaSim can generate spheroids, to get a equal-sided sphere you need to specify the 3 axis
        sphereHandle = self.createPrimitiveShape(self.sim.primitiveshape_spheroid, radius, radius, radius)

        if transparency:
            self.makeObjectTransparent(sphereHandle)  

        # Sets the generic properties of every object like its color, and positon in space
        self.setObjectProperties(location, color, label, sphereHandle)

    def calculateLengthLine(self, p1, p2):
        x1, y1, z1 = p1
        x2, y2, z2 = p2
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

    def addLine(self, p1, p2, color, radius, label):
        length = self.calculateLengthLine(p1, p2)

        lineHandle = self.createPrimitiveShape(self.sim.primitiveshape_cylinder, radius, radius, length)

        location = 1 
        self.setObjectProperties(location, color, label, lineHandle)

    def addCircle(self, location, normal, radius, color, label, isDashed, isFilled):
        circleHandle = self.createPrimitiveShape(self.sim.primitiveshape_disc, radius, radius, radius)
        self.setObjectProperties(self, location, color, label, circleHandle)

    def addRobot(self):
        robotHandle = self.loadModel("UR5.ttm")
        return robotHandle

x = EuclidViewerCoppelia()
y = x.calculateLengthLine((0,0,0), (1,1,1))
print(y)