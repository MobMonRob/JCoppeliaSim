import math
import coppeliaManager

class EuclidViewerCoppelia(coppeliaManager.CoppeliaManager):

    """
    @dev: Auxiliary function
        This function sets the general properties of any shape. 
        Its position, color and label
    @param: location: tuple of floats with the x, y, z position
            color: Color data type with the r, g, b values
            label: string with the text of the label to assign
            objectHandle: int with the handle of the object to interact with 
    @returns: void
    @author: Andres Masis
    """
    def setObjectProperties(self, location, color, label, objectHandle):
        self.setObjectPosition(objectHandle, location[0], location[1], location[2])
        self.setObjectColor(objectHandle, color[0], color[1], color[2])
        self.setObjectLabel(objectHandle, label)   

    """
    @dev: This function adds a sphere in the CoppeliaSim scene
    @param: location: tuple of floats with the x, y, z position
            radius: float with the radius of the sphere
            color: Color data type with the r, g, b values
            label: string with the text of the label to assign
            transparency: boolean determining if the sphere will be transparent(true) or not(false)
    @returns: int with the handle of the created sphere
    @author: Andres Masis
    """
    def addSphere(self, location, radius, color, label, transparency):
        # CoppeliaSim can generate spheroids, to get a equal-sided sphere you need to specify the 3 axis
        sphereHandle = self.createPrimitiveShape(self.sim.primitiveshape_spheroid, radius, radius, radius)

        # Checks if has to make the sphere transparent
        if transparency:
            self.makeObjectTransparent(sphereHandle)  

        # Sets the generic properties of every object like its color, and positon in space
        self.setObjectProperties(location, color, label, sphereHandle)

        # Returns the sphere handle
        return sphereHandle

    """
    @dev: Auxiliary function
          This function calculates the distance between 2 3d points
    @param: p1: tuple of floats with the coordinates x1, y1, z1
            p2: tuple of floats with the coordinates x2, y2, z2
    @returns: float with the distance between those point
    @author: Andres Masis
    """
    def calculateLengthLine(self, p1, p2):
        # Gets the independent x, y, z values
        x1, y1, z1 = p1
        x2, y2, z2 = p2

        # Calculates the length in the 3d space and returns that result
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

    """
    @dev: This function adds a new line in the CoppeliaSim scene
          INCOMPLETE, missing the euler angles and position in space
    @param: p1: tuple of floats with the x, y, z position of the start of the line
            p2: tuple of floats with the x, y, z position of the end of the line
            color: Color data type with the r, g, b values of the line
            radius: float that determines the thickness of the line (which is just a long cylinder)
            label: string with the text of the label to assign
    @returns: int with the handle of the created line
    @author: Andres Masis
    """
    def addLine(self, p1, p2, color, radius, label):
        # Calculates the lenght of the line
        length = self.calculateLengthLine(p1, p2)

        # Creates the line
        lineHandle = self.createPrimitiveShape(self.sim.primitiveshape_cylinder, radius, radius, length)

        # Calculates and sets the orientation of the line        

        # Calculates the location of the line
        location = 1 

        # Sets the general properties of the object: location, color and label
        self.setObjectProperties(location, color, label, lineHandle)

    """
    @dev: This function adds a new line in the CoppeliaSim scene
          INCOMPLETE, missing the euler angles and position in space
    @param: p1: tuple of floats with the x, y, z position of the start of the line
            p2: tuple of floats with the x, y, z position of the end of the line
            color: Color data type with the r, g, b values of the line
            radius: float that determines the thickness of the line (which is just a long cylinder)
            label: string with the text of the label to assign
    @returns: int with the handle of the created line
    @author: Andres Masis
    """
    def addCircle(self, location, normal, radius, color, label, isDashed, isFilled):
        circleHandle = self.createPrimitiveShape(self.sim.primitiveshape_disc, radius, radius, radius)
        self.setObjectProperties(self, location, color, label, circleHandle)

    def addRobot(self):
        ur5Path = "C:\\Program Files\\CoppeliaRobotics\\CoppeliaSimEdu\\models\\robots\\non-mobile\\UR5.ttm"
        robotHandle = self.loadModel(ur5Path)
        return robotHandle

