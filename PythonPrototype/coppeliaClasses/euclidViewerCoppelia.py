import coppeliaClasses.coppeliaManager
import mathClasses.mathAuxiliar
import objManagers.objFileManager 

"""
This  class implements the interface iEuclidViewer3D
This class inherits from EuclidViewerCoppelia
So it can access all the CoppeliaSim methods
The super class deals with the stepping mode and with other CoppeliaSim details
So this class only has to call the methods of its superclass
This class just implements the methods of the interface
And sends parameters to its superclass methods
And then return those values
Sometimes, it needs help to know the value of the parameters it should send to the superclass
For this it imports some other classes made in this project
mathAuxiliary provides methods to calculate distances, positions and orientations
objFileManager provides the method to create an .obj file for the polyognes
"""

class EuclidViewerCoppelia(coppeliaClasses.coppeliaManager.CoppeliaManager):

    def __init__(self):
        # Creates an object to get methods calculateLengthLine() or calculateCenter()
        self.mathAuxiliar = mathClasses.mathAuxiliar.MathAuxiliar()
        # Creates an object to get the methods to create an .obj file
        self.objFileManager = objManagers.objFileManager.ObjFileManager()
        # Calls the constructor of the superclass to get all the CoppeliaSim methods
        super().__init__()

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
    @dev: This function adds a new line in the CoppeliaSim scene
          There is no native line in CoppeliaSim, so it is actually a very long and thin cylinder
          INCOMPLETE, missing the euler angles
    @param: p1: Point3d with the x, y, z position of the start of the line
            p2: Point3d with the x, y, z position of the end of the line
            color: Color data type with the r, g, b values of the line
            radius: double that determines the thickness of the line (which is just a long cylinder)
            label: string with the text of the label to assign
    @returns: long with the handle of the created line
    @author: Andres Masis
    """
    def addLine(self, p1, p2, color, radius, label, addCones):
        # Calculates the lenght of the line with a method of MathAuxiliar
        length = self.mathAuxiliar.calculateLengthLine(p1, p2)

        # Creates the line     
        if addCones:
            # It has cones, we need to call a function to created that merged shape
            lineHandle = self.createLineWithCones(radius, length)

        else:
            # It is a simple line, we can create a primitive cylinder
            # make sure to put the radius at first and length at last to make sure it is thin and long
            lineHandle = self.createPrimitiveShape(self.sim.primitiveshape_cylinder, radius, radius, length)

        # Calculates and sets the orientation of the line  
        
        # Some code for the euler angles

        # Calculates the location of the line with a method of MathAuxiliar
        location = self.mathAuxiliar.calculateCenter(p1, p2)

        # Sets the general properties of the object: location, color and label
        self.setObjectProperties(location, color, label, lineHandle)

        # The line is ready, now it can be returned
        return lineHandle

    """
    @dev: This function adds an arrow to the CoppeliaSim scene
          There is no native arrow in CoppeliaSim (add a cylinder and cone)
          INCOMPLETE, missing the Euler angles
    @param: location: Point3d with the x, y, z coordinates of the start point of the arrow
            direction: Vector3d that describes the direction of the arrow
            radius: double with the thickness of the arrow line
            color: Color with the r, g, b values
            label: String with the text of the label of the arrow
    @returns: long with the handle of the created arrow
    @author: Andres Masis
    """
    def addArrow(self, location, direction, radius, color, label):
        arrowHandle = self.createArrow(radius)

        # SOME CODE TO MANAGE THE EULER ANGLES

        # Sets the properties of the new arrow
        self.setObjectProperties(location, color, label, arrowHandle)

        return arrowHandle

    """
    @dev: This function adds a new 2d circle in the CoppeliaSim scene
          INCOMPLETE, MISSING THE EULER ANGLES BASED ON THE NORMAL
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

        if isFilled:
            # It is a normal circle, we can create the circle based on the given radius
            circleHandle = self.createPrimitiveShape(self.sim.primitiveshape_disc, radius, radius, radius)

        else:
            # Is empty, may be dashed or not
            if isDashed:
                #It is empty and dashed, we can import the shape and send the given radius to scale it
                circleHandle = self.importShape("C:\\Users\\rahm-\\Documents\\coppeliaPythonZMQ\\JCoppeliaSim\\PythonPrototype\\models\\DashedCircle.obj",  radius)
                                     
            else:
                #It is just empty, we can import the shape to scale it
                circleHandle = self.importShape("C:\\Users\\rahm-\\Documents\\coppeliaPythonZMQ\\JCoppeliaSim\\PythonPrototype\\models\\EmptyCircle.obj",  radius)
                               
        # SOME CODE TO MANAGE THE EULER ANGLES

        # Sets the circle general properties like its location, color and label
        self.setObjectProperties(location, color, label, circleHandle)

        # The circle is ready, we can return its handle
        return circleHandle


    """
    @dev: Adds a polygone (any proportions and amount of sides) to the CoppeliaSim scene
          There is not native way to create polygons in CoppeliaSim
          It generates a .obj file and then loads it to the CoppeliaSim scene
          Then it treats it as any other object with its handle
          MISSING EULER ANGLES AND 
          CHECK THE NORMAL IF THE POLYGONE IS NOT PARALLEL TO THE GROUND
          AND CENTERED IN 0,0,0
    @param: location: Point3d with the x, y, z location of the center of the figure
            corners: Point3d[] array of all the 3d points of the corners of the figure
            color: Color with the r, g, b values of the polygone
            label: String with the text to add to the label
            showNormal: boolean that determines if the normal should be drawn in the scene (True) or not (drawn)
            transparency: boolean that determines if the figure will be transparent (True) or not(False)
    @returns: long with the handle of the generated polygone 
    @author: Andres Masis
    """
    def addPolygone(self, location, corners, color, label, showNormal, transparency):
        # Creates a .obj file with the polygone given its corners
        filePath = self.objFileManager.createPolygoneFile(corners)

        # Loads the generated .obj file into the CoppeliaSim scene
        polygoneHandle = self.importShape(filePath,  1)

        # Checks if a normal arrow has to be added to the polygone
        if showNormal:
            # For this is assumed that the polygone at this point is centered in 0,0,0
            # It is also assumed that the polygone is parallel to the floor
            polygoneHandle = self.createPolygoneWithNormal(polygoneHandle)

        # Checks if has to make the polygone transparent
        if transparency:
            self.makeObjectTransparent(polygoneHandle)  

        # CODE TO MANAGE THE EULER ANGLES OF THE POLYGONE

        # Sets the polygone´s general properties like its location, color and label
        self.setObjectProperties(location, color, label, polygoneHandle)

        # The polygone is ready so we can return its handle
        return polygoneHandle
    
    """
    @dev: This function adds into the simulation a partial 2D circle representing an angle
          First it generates an .obj file with the partial circle given its angle
          Then it loads the generated shape into the CoppeliaSim scene
          Next, it sets the properties of the shape, like its orientation, label, color, etc
          iNCOMPLETE, MISSING THE CODE FOR THE EULER ANGLES
    @param: angle: integer between 0 and 360, with the angle to generate
            location: Point3d with the x, y, z location of the center of the figure
            color: Color with the r, g, b values of the polygone
            MAYBE A PARAMETER FOR THE ORIENTATION WILL BE ADDED
    @returns: long with the handle of the generated cube
    @author: Andres Masis
    """
    def addFlatAngle(self, angle, location, color):
        # Creates a .obj file with the polygone given its corners
        filePath = self.objFileManager.createAngleFlatCircle(angle)

        # Loads the generated .obj file into the CoppeliaSim scene
        angleHandle = self.importShape(filePath,  1)


        # CODE TO MANAGE THE EULER ANGLES OF THE POLYGONE

        label = str(angle)+"Degrees"

        # Sets the polygone´s general properties like its location, color and label
        self.setObjectProperties(location, color, label, angleHandle)

        # The polygone is ready so we can return its handle
        return angleHandle
                            
    """
    @dev: This function adds a cube to the CoppeliaSim scene
          The cuboid is a native Coppelia figure, so just add a regular cuboid
          INCOMPLETE, MISSING THE EULER ANGLES BASED ON DIR
    @param: location: Point3d with the x, y, z location of the cube
            dir: Vector3d with a vector that determines the direction/orientation of the cube
            width: double that determines the siye of the cube
            color: Color with the r, g, b values 
            label: String with the text to add
            transparency: boolean that determines if the figure will be transparent (True) or not(False)
    @returns: long with the handle of the generated cube
    @author: Andres Masis
    """
    def addCube(self, location, dir, width, color, label, transparency):
        cubeHandle = self.createPrimitiveShape(self.sim.primitiveshape_cuboid, width, width, width)

        # Checks if has to make the sphere transparent
        if transparency:
            self.makeObjectTransparent(cubeHandle)  

        # DO SOME STUFF TO MANAGE THE EULER ANGLES BASED ON DIR

        # Sets the circle general properties like its location, color and label
        self.setObjectProperties(location, color, label, cubeHandle)

        # The circle is ready, we can return its handle
        return cubeHandle


    
    """
    @dev: This function adds a new robot into the CoppeliaSim scene
    @param: None
    @returns: long with the handle of the created line
    @author: Andres Masis
    """
    def addRobot(self):
        # Hardcoded location of the robot file
        ur5Path = "C:\\Users\\rahm-\\Documents\\coppeliaPythonZMQ\\JCoppeliaSim\\PythonPrototype\\models\\UR5.ttm"

        # Load the model in the scene
        robotHandle = self.loadModel(ur5Path)

        # Return the handle of the loaded robot
        return robotHandle
    
    """
    @dev: This function moves a robot into a new position in the CoppeliaSim scene
    @param: handle: long with the numeric handle of the object
            angles: double[] array with the angles of the movement
    @returns: void
    @author: Andres Masis
    """
    def moveRobot(self, handle, angles):
        self.setObjectOrientation(handle, angles.alpha, angles.beta, angles.gamma)

    """
    @dev: This function removes and object in the CoppeliaSim scene
    @param: handle: long with the numeric handle of the object
    @returns: boolean. True if it was removed properly, False if an error happened
    @author: Andres Masis
    """
    def removeNode(self, handle):
        try:
            self.sim.removeModel(handle)
            self.client.step()  # triggers next simulation step

            return True
        except Exception as e:
            return False

    """
    @dev: This function removes and object in the CoppeliaSim scene
    @param: handle: long with the numeric handle of the object
            transform: Matrix4d with the transformation matrix
    @returns: void
    @author: Andres Masis
    """
    def transform(self, handle, transform):
        # Pseudocode of how it would look like in Java, there is no Matrix4d data type in Python
        # Just to give an example of how to get the values we need
        alpha = transform.getAlphaDegree()
        beta = transform.getAlphaDegree()
        gamma = transform.getAlphaDegree()

        x = transform.getX()
        y = transform.getY()
        z = transform.getY()
        
        # Real code of how to use the CoppeliaManager functions once we have the necessary values
        self.setObjectPosition(handle, x, y, z)
        self.setObjectOrientation(handle, alpha, beta, gamma)

