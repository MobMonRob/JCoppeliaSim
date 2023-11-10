import math
import coppeliaManager

class EuclidViewerCoppelia(coppeliaManager.CoppeliaManager):

    """
    @dev: This function opens the CoppeliaSim scene
          If a problem occurs while openning, an exception is raised
    @param: None
    @returns: void
    @author: Andres Masis
    """
    def open(self):
        # Code to autonatically open CoppeliaSim.exe

        success = self.startSimulation()

        if not success:
            raise Exception("Error openning the Coppelia scene")
    
    """
    @dev: This function closes the simulation
    @param: None
    @returns: void
    @author: Andres Masis
    """
    def close(self):
        self.stopSimulation()

        # Some code to close the CoppeliaSim app
    
    """
    @dev: getter for the AAAB object of the class
    @param: None
    @returns: AAAB object
    @author: Andres Masis
    """
    def getAABB(self):
        return self.AAAB

    """
    @dev: This function adds a sphere in the CoppeliaSim scene
        The spheroid is a native Coppelia figure, so just add a regular spheroid
    @param: location: Point3d with the x, y, z position
            radius: double with the radius of the sphere
            color: Color data type with the r, g, b values
            label: string with the text of the label to assign
            transparency: boolean determining if the sphere will be transparent(true) or not(false)
    @returns: long with the handle of the created sphere
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
    @param: p1: Point3d with the coordinates x1, y1, z1
            p2: Point3d with the coordinates x2, y2, z2
    @returns: double with the distance between those point
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
          There is no native line in CoppeliaSim, so it is actually a very long and thin cylinder
          INCOMPLETE, missing the euler angles and position in space
    @param: p1: Point3d with the x, y, z position of the start of the line
            p2: Point3d with the x, y, z position of the end of the line
            color: Color data type with the r, g, b values of the line
            radius: double that determines the thickness of the line (which is just a long cylinder)
            label: string with the text of the label to assign
    @returns: long with the handle of the created line
    @author: Andres Masis
    """
    def addLine(self, p1, p2, color, radius, label):
        # Calculates the lenght of the line
        length = self.calculateLengthLine(p1, p2)

        # Creates the line
        # make sure to put the radius at first length at last to make sure it is thin and long
        lineHandle = self.createPrimitiveShape(self.sim.primitiveshape_cylinder, radius, radius, length)

        # Calculates and sets the orientation of the line        

        # Calculates the location of the line
        location = 1 

        # Sets the general properties of the object: location, color and label
        self.setObjectProperties(location, color, label, lineHandle)

    """
    @dev: This function adds an arrow to the CoppeliaSim scene
          There is no native arrow in CoppeliaSim (add a premade model, cylinder and cone?)
    @param: location: Point3d with the x, y, z coordinates of the start point of the arrow
            direction: Vector3d that describes the direction of the arrow
            radius: double with the thickness of the arrow line
            color: Color with the r, g, b values
            label: String with the text of the label of the arrow
    @returns: long with the handle of the created arrow
    @author: Andres Masis
    """
    def addArrow(self, location, direction, radius, color, label):
        pass
    

    """
    @dev: This function adds a new 2d circle in the CoppeliaSim scene
          INCOMPLETE, missing the euler angles for the normal and the circle
          Missing dashed and empty circle
    @param: location: Point3d with the x, y, z position of the circle
            normal: Vector3d with the normal vector (90 degrees) to the circle
            radius: double with the radius of the circle
            color: Color data type with the r, g, b values of the line
            radius: double that determines the thickness of the line (which is just a long cylinder)
            label: string with the text of the label to assign
            isDashed: boolean that determines if the border is dashed (True......) or continuous border(False_______)
            isFilled: boolean that determines if the circle is filled(True) or empty(False)
    @returns: long with the handle of the created circle
    @author: Andres Masis
    """
    def addCircle(self, location, normal, radius, color, label, isDashed, isFilled):

        circleHandle = self.createPrimitiveShape(self.sim.primitiveshape_disc, radius, radius, radius)
        self.setObjectProperties(self, location, color, label, circleHandle)

    """
    @dev: Adds a polygone (any proportions and amount of sides) to the CoppeliaSim scene
          There is not native way to create polygons in CoppeliaSim. (Connect lines between all the point?)
    @param: location: Point3d with the x, y, z location of the center of the figure
            corners: Point3d[] array of all the 3d points of the corners of the figure
            color: Color with the r, g, b values of the polygone
            label: String with the text to add to the label
            showNormal: boolean that determines if the normal should be drawn in the scene (True) or not (drawn)
            transparency: boolean that determines if the figure will be transparent (True) or not(False)
    @returns: long with the handle of the generated polygone 
    @author: Andres Masis
    """
    def addPolygone(self, location, corners, color, label, showNormal, tranparency):
        pass
    
    """
    @dev: This function adds a cube to the CoppeliaSim scene
          The cuboid is a native Coppelia figure, so just add a regular cuboid
    @param: location: Point3d with the x, y, z location of the cube
            dir: Vector3d with a vector that determines the direction/orientation of the cube
            width: double that determines the siye of the cube
            color: Color with the r, g, b values 
            label: String with the text to add
            transparency: boolean that determines if the figure will be transparent (True) or not(False)
    @returns: long with the handle of the generated cube
    @author: Andres Masis
    """
    def addCube(self, location, dir, width, color, label, tranparency):
        pass
    
    """
    @dev: This function adds a new robot into the CoppeliaSim scene
    @param: None
    @returns: long with the handle of the created line
    @author: Andres Masis
    """
    def addRobot(self):
        # Hardcoded location of the robot file
        ur5Path = "C:\\Program Files\\CoppeliaRobotics\\CoppeliaSimEdu\\models\\robots\\non-mobile\\UR5.ttm"

        # Load the model in the scene
        robotHandle = self.loadModel(ur5Path)

        # Return the handle of the loaded robot
        return robotHandle
    
    public void moveRobot(long handle, double[] angels);

    public boolean removeNode(long handle);

    public void transform(long handle, Matrix4d transform);

