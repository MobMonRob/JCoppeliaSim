from coppeliasim_zmqremoteapi_client import RemoteAPIClient

class CoppeliaManager:
    def __init__(self):
        self.startSimulation()

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

    def createPrimitiveShape(self, type, x, y, z):
        shapeHandle = self.sim.createPrimitiveShape(type, [x, y, z], 0)
        self.client.step()  # triggers next simulation step

        return shapeHandle

    def setObjectOrientation(self, objectHandle, alpha, beta, gamma):
        self.sim.setObjectOrientation(objectHandle, self.sim.handle_parent, [alpha, beta, gamma])
        self.client.step()  # triggers next simulation step

    def setObjectPosition(self, objectHandle, x, y, z):
        self.sim.setObjectPosition(objectHandle, self.sim.handle_parent, [x, y, z])
        self.client.step()  # triggers next simulation step

    def setObjectColor(self, objectHandle, r, g, b):
        self.sim.setShapeColor(objectHandle, None, self.sim.colorcomponent_emission, [r, g, b])
        self.client.step()  # triggers next simulation step

    def makeObjectTransparent(self, objectHandle):
        self.sim.setShapeColor(objectHandle, None, self.sim.colorcomponent_transparency, [0.5])
        self.client.step()  # triggers next simulation step

    """
    @dev: This function get the CoppeliaSim handle of a given object based on its name
    @param: the name of the object in CoppeliaSim, for example "/Dummy"
    @returns: the handle of an object
    """
    def getObjectHandle(self, objectName):
        objectHandle = self.sim.getObject(objectName, None)
        self.client.step()  # triggers next simulation step

        return objectHandle
    
    '''
    @dev: This function gets the x, y, and z lenghts of the bounding box of a given object
    @param: the handle of the object to calculate its bounding box
    @returns: 3 values. The x length, the y length and the z length
    @author: Andres Masis
    '''
    def getObjectBoundingBoxSize(self, objectHandle):
        # Gets the x length
        r, m = self.sim.getObjectFloatParameter(objectHandle, self.sim.objfloatparam_objbbox_max_x)
        r, n = self.sim.getObjectFloatParameter(objectHandle, self.sim.objfloatparam_objbbox_min_x)
        x = m - n

        # Gets the y length
        r, m = self.sim.getObjectFloatParameter(objectHandle, self.sim.objfloatparam_objbbox_max_y)
        r, n = self.sim.getObjectFloatParameter(objectHandle, self.sim.objfloatparam_objbbox_min_y)
        y = m - n

        # Gets the z length
        r, m = self.sim.getObjectFloatParameter(objectHandle, self.sim.objfloatparam_objbbox_max_z)
        r, n = self.sim.getObjectFloatParameter(objectHandle, self.sim.objfloatparam_objbbox_min_z)
        z = m - n

        # Returns all the values
        return x, y, z
    
    def stopSimulation(self):
        # Stops the simulation
        self.sim.stopself.simulation()

        # Restore the original idle loop frequency:
        self.sim.setInt32Param(self.sim.intparam_idle_fps, self.defaultIdleFps)