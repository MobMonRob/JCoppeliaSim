from coppeliasim_zmqremoteapi_client import RemoteAPIClient

class CoppeliaManager:
    def __init__(self):
        self.startSimulation()

    '''
    @dev: This function remotely starts the simulation in CoppeliaSim
    @param: None
    @returns: True if the process was succesful
              False if an exception happens
    @author: Andres Masis
    '''
    def startSimulation(self):
        try:
            # Starts the CoppeliaSim client
            self.client = RemoteAPIClient()
            self.sim = self.client.require('sim')

            # Run a simulation in stepping mode:
            self.sim.setStepping(True)
            self.sim.startSimulation()
            return True

        except Exception as e:
            return False

    '''
    @dev: This function creates a primitive shape (sphere, cuboid, etc) in the scene
    @param: type: https://coppeliarobotics.com/helpFiles/index.html -> Writing code -> CoppeliaSim API Framework -> Regular API Constants -> Primitive shape types
            x: Float value size of the figure in the x axis
            y: Float value size of the figure in the y axis
            z: Float value size of the figure in the z axis
    @returns: void
    @author: Andres Masis
    '''
    def createPrimitiveShape(self, type, x, y, z):
        # Creates the shape
        shapeHandle = self.sim.createPrimitiveShape(type, [x, y, z], 0)
        self.client.step()  # triggers next simulation step

        
        # Turns off the properties of the shape to make sure it will cause interference in the simulation

        # Makes the shape not dynamic
        self.sim.setModelProperty(shapeHandle, self.sim.modelproperty_not_dynamic)
        self.client.step()  # triggers next simulation step

        # Makes the shape not respondable
        self.sim.setModelProperty(shapeHandle, self.sim.modelproperty_not_respondable)
        self.client.step()  # triggers next simulation step

        # Makes the shape not detectable
        self.sim.setModelProperty(shapeHandle, self.sim.modelproperty_not_detectable)
        self.client.step()  # triggers next simulation step

        # Makes the shape not measurable
        self.sim.setModelProperty(shapeHandle, self.sim.modelproperty_not_measurable)
        self.client.step()  # triggers next simulation step

        # Makes the shape not collidable
        self.sim.setModelProperty(shapeHandle, self.sim.modelproperty_not_collidable)
        self.client.step()  # triggers next simulation step
        

        # The shape is ready, we can return its handle
        return shapeHandle

    '''
    @dev: This function sets the orientation of a figure in the space of the CoppeliaSim scene
          It is recommended to call this function before setObjectPosition(), because this function
          can also change the postion of the object, so first rotate it and then position it
    @param: objectHandle: integer of the handle of the object in CoppeliaSim
            alpha: Float value rotation of the figure in the alpha axis
            beta: Float value rotation of the figure in the beta axis
            gamma: Float value rotation of the figure in the gamma axis
    @returns: void
    @author: Andres Masis
    '''
    def setObjectOrientation(self, objectHandle, alpha, beta, gamma):
        self.sim.setObjectOrientation(objectHandle, self.sim.handle_parent, [alpha, beta, gamma])
        self.client.step()  # triggers next simulation step

    '''
    @dev: This function sets the position of a figure in the space of the CoppeliaSim scene
          It is recommended to call this function after createPrimitiveShape(), because that function
          can also change the postion of the object, so first rotate it and then position it
    @param: objectHandle: integer of the handle of the object in CoppeliaSim
            x: Float value of the position of the center of the figure in the x axis
            y: Float value of the position of the center of the figure in the y axis
            z: Float value of the position of the center of the figure in the z axis
    @returns: void
    @author: Andres Masis
    '''
    def setObjectPosition(self, objectHandle, x, y, z):
        self.sim.setObjectPosition(objectHandle, self.sim.handle_parent, [x, y, z])
        self.client.step()  # triggers next simulation step


    '''
    @dev: This function sets the color of a figure in the CoppeliaSim scene
    @param: objectHandle: integer of the handle of the object in CoppeliaSim
            r: integer between 0 and 255 of the red intensity
            g: integer between 0 and 255 of the green intensity
            b: integer between 0 and 255 of the blue intensity
    @returns: void
    @author: Andres Masis
    '''
    def setObjectColor(self, objectHandle, r, g, b):
        self.sim.setShapeColor(objectHandle, None, self.sim.colorcomponent_ambient_diffuse, [r, g, b])
        self.client.step()  # triggers next simulation step

    '''
    @dev: This function makes slightly transparent a figure in the CoppeliaSim scene
    @param: objectHandle: integer of the handle of the object in CoppeliaSim
            r: integer between 0 and 255 of the red intensity
            g: integer between 0 and 255 of the green intensity
            b: integer between 0 and 255 of the blue intensity
    @returns: void
    @author: Andres Masis
    '''
    def makeObjectTransparent(self, objectHandle):
        self.sim.setShapeColor(objectHandle, None, self.sim.colorcomponent_transparency, [0.5])
        self.client.step()  # triggers next simulation step

    """
    @dev: This function get the CoppeliaSim handle of a given object based on its name
    @param: the name of the object in CoppeliaSim, for example "/Dummy"
    @returns: the handle of an object
    @author: Andres Masis
    """
    def getObjectHandle(self, objectName):
        objectHandle = self.sim.getObject(objectName, None)
        self.client.step()  # triggers next simulation step

        return objectHandle
    
    '''
    @dev: This function gets the x, y, and z lenghts of the bounding box of a given object
    @param: the handle of the object to calculate its bounding box
    @returns: 3 float values. The x length, the y length and the z length of the bounding box
    @author: Andres Masis
    '''
    def getObjectBoundingBoxSize(self, objectHandle):
        # Gets the x length
        r, m = self.sim.getObjectFloatParameter(objectHandle, self.sim.objfloatparam_objbbox_max_x)
        self.client.step()  # triggers next simulation step
        r, n = self.sim.getObjectFloatParameter(objectHandle, self.sim.objfloatparam_objbbox_min_x)
        self.client.step()  # triggers next simulation step
        x = m - n

        # Gets the y length
        r, m = self.sim.getObjectFloatParameter(objectHandle, self.sim.objfloatparam_objbbox_max_y)
        self.client.step()  # triggers next simulation step
        r, n = self.sim.getObjectFloatParameter(objectHandle, self.sim.objfloatparam_objbbox_min_y)
        self.client.step()  # triggers next simulation step
        y = m - n

        # Gets the z length
        r, m = self.sim.getObjectFloatParameter(objectHandle, self.sim.objfloatparam_objbbox_max_z)
        self.client.step()  # triggers next simulation step
        r, n = self.sim.getObjectFloatParameter(objectHandle, self.sim.objfloatparam_objbbox_min_z)
        self.client.step()  # triggers next simulation step
        z = m - n

        # Returns all the values
        return x, y, z
    
    '''
    @dev: This function sets the alias of a given object in the CoppeliaSim simulation
    @param: objectHandel: int of the handle of the object to set a alias
            alias: string with the text of the alias            
    @returns: void
    @author: Andres Masis
    '''
    def setObjectAlias(self, objectHandle, alias):
        self.sim.setObjectAlias(objectHandle, alias)
        self.client.step()  # triggers next simulation step

    '''
    @dev: This function loads a model (.ttm file)
    @param: filepath: string with the absolute path of the file       
    @returns: void
    @author: Andres Masis
    '''
    def loadModel(self, filepath):
        objectHandle = self.sim.loadModel(filepath)
        self.client.step()  # triggers next simulation step
        
        return objectHandle
    
    """
    @dev: Auxiliary function
        This function sets the general properties of any shape. 
        Its position, color and label
    @param: location: Point3d with the x, y, z position
            color: Color data type with the r, g, b values
            label: string with the text of the label to assign
            objectHandle: int with the handle of the object to interact with 
    @returns: void
    @author: Andres Masis
    """
    def setObjectProperties(self, location, color, label, objectHandle):
        self.setObjectPosition(objectHandle, location[0], location[1], location[2])
        self.setObjectColor(objectHandle, color[0], color[1], color[2])
        self.setObjectAlias(objectHandle, label)   

    """
    @dev: Auxiliary funtion that creates an arrow by merging a cylinder and a cone
    @param: radius: double with the thickness of the arrow line
    @returns: long with the handle of the created arrow
    @author: Andres Masis
    """
    def createArrow(self, radius):
        # Calculates the lenght of the line based on the radius to make it symetrical
        lineLength = radius * 50

        # Creates the line
        # make sure to put the radius at first and length at last to make sure it is thin and long
        lineHandle = self.createPrimitiveShape(self.sim.primitiveshape_cylinder, radius, radius, lineLength)

        # Calculates the size of the nose(cone) based on the radius to make it symetrical
        coneDimension = radius * 5

        # Creates the nose
        coneHandle = self.createPrimitiveShape(self.sim.primitiveshape_cone, coneDimension, coneDimension, coneDimension)
        # Puts the nose (cone) at the final point of the line (cylinder)
        self.setObjectPosition(coneHandle, 0, 0, lineLength/2)

        # Merges both shapes in a single arrow
        arrowHandle = self.sim.groupShapes([lineHandle, coneHandle], False)

        return arrowHandle
    
    """
    @dev: This function imports a mesh (.obj model) into the CoppeliaSim scene
          Auxiliary funtion
    @param: pathAndFileName: string, location of the file to import
            scalingFactor: float, the scaling factor to apply to the imported vertices
    @returns: integer with the handle of the imported shape
    @author: Andres Masis
    """
    def importShape(self, pathAndFilename, scalingFactor):
        # This 32 is necessary to align the objects bounding box
        shapeHandle = self.sim.importShape(0, pathAndFilename, 32, 0, scalingFactor)
        return shapeHandle

    '''
    @dev: This function stops the CoppeliaSim simulation
    @param: None
    @returns: void
    @author: Andres Masis
    '''
    def stopSimulation(self):
       # Stops the CoppeliaSim simulation
       self.sim.stopSimulation()

    