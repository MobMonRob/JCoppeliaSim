import math
import coppeliaManager

class EuclidViewerCoppelia(coppeliaManager.CoppeliaManager):

    def setObjectProperties(self, location, color, label, objectHandle, transparency):
        self.setObjectPosition(objectHandle, location.x, location.y, location.z)
        self.setObjectColor(objectHandle, color.r, color.g, color.b)
        self.setObjectLabel(objectHandle, label)

        if transparency:
            self.makeObjectTransparent(objectHandle)     

    def addSphere(self, location, radius, color, label, transparency):
        # CoppeliaSim can generate spheroids, to get a equal-sided sphere you need to specify the 3 axis
        sphereHandle = self.createPrimitiveShape(self.sim.primitiveshape_spheroid, radius, radius, radius)

        # Sets the generic properties of every object like its color, transpareny and positon in space
        self.setObjectProperties(location, color, label, sphereHandle, transparency)

    def calculateLengthLine(self, p1, p2):
        x1, y1, z1 = p1
        x2, y2, z2 = p2
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

    def addLine(self, p1, p2, color, radius, label):
        length = self.calculateLengthLine(p1, p2)

        sphereHandle = self.createPrimitiveShape(self.sim.primitiveshape_cylinder, radius, radius, radius)