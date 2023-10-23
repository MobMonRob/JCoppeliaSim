from coppeliasim_zmqremoteapi_client import RemoteAPIClient

client = RemoteAPIClient()
sim = client.getObject('sim')

# Makes sure that the idle loop runs at full speed for this program:
defaultIdleFps = sim.getInt32Param(sim.intparam_idle_fps)
sim.setInt32Param(sim.intparam_idle_fps, 0)

'''
@dev: This function gets the x, y, and z lenghts of the bounding box of a given object
@param: the handle of the object to calculate its bounding box
@returns: 3 values. The x length, the y length and the z length
@author: Andres Masis
'''
def getObjectBoundingBoxSize(handle):
    # Gets the x lenght
    r, m = sim.getObjectFloatParameter(handle, sim.objfloatparam_objbbox_max_x)
    r, n = sim.getObjectFloatParameter(handle, sim.objfloatparam_objbbox_min_x)
    x = m - n

    # Gets the y lenght
    r, m = sim.getObjectFloatParameter(handle, sim.objfloatparam_objbbox_max_y)
    r, n = sim.getObjectFloatParameter(handle, sim.objfloatparam_objbbox_min_y)
    y = m - n

    # Gets the z lenght
    r, m = sim.getObjectFloatParameter(handle, sim.objfloatparam_objbbox_max_z)
    r, n = sim.getObjectFloatParameter(handle, sim.objfloatparam_objbbox_min_z)
    z = m - n

    # Returns all the values
    return x, y, z

dummyHandle = sim.getObject("/Dummy", None)
client.step()  # triggers next simulation step

x, y, z = getObjectBoundingBoxSize(dummyHandle)

boxHandle = sim.createPrimitiveShape(sim.primitiveshape_cuboid,[x, y, z], 0)
client.step()  # triggers next simulation step

# Color
sim.setShapeColor(boxHandle, None, sim.colorcomponent_emission, [0, 255, 0])
client.step()  # triggers next simulation step

# Transparency
sim.setShapeColor(boxHandle, None, sim.colorcomponent_transparency, [0.5])