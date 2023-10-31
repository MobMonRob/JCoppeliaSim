from coppeliasim_zmqremoteapi_client import RemoteAPIClient

class CoppeliaManager:
    def __init__(self):
        self.startSimulation()

    '''
    @dev: This function remotely starts the simulation in CoppeliaSim
    @param: None
    @returns: void
    @author: Andres Masis
    '''
    def startSimulation(self):
        # Access to  the CoppeliaSim client
        self.client = RemoteAPIClient()
        self.sim = self.client.getObject('sim')

        # Makes sure that the idle loop runs at full speed for this program:
        self.defaultIdleFps = self.sim.getInt32Param(self.sim.intparam_idle_fps)
        self.sim.setInt32Param(self.sim.intparam_idle_fps, 0)

        # Runs a simulation in stepping mode:
        self.client.setStepping(True)
        self.sim.startSimulation()

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
        self.sim.setShapeColor(objectHandle, None, self.sim.colorcomponent_emission, [r, g, b])
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
    @dev: This function stops the CoppeliaSim simulation
    @param: None
    @returns: void
    @author: Andres Masis
    '''
    def stopSimulation(self):
       # Stops the CoppeliaSim simulation
       self.sim.stopSimulation()

       # Restore the original idle loop frequency:
       self.sim.setInt32Param(self.sim.intparam_idle_fps, self.defaultIdleFps)

    '''
    @dev: This function sets the label of a given object in the CoppeliaSim simulation
    @param: objectHandel: int of the handle of the object to set a label
            label: string with the text of the label            
    @returns: void
    @author: Andres Masis
    '''
    def setObjectLabel(self, objectHandle, label):
        self.sim.setObjectAlias(objectHandle, label)
        self.client.step()  # triggers next simulation step


    def loadModel(self, filename):
        objectHandle = self.sim.loadModel(filename)
        return objectHandle