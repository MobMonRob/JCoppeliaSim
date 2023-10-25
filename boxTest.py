from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import time

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

# Access to  the CoppeliaSim client
client = RemoteAPIClient()
sim = client.getObject('sim')

# Makes sure that the idle loop runs at full speed for this program:
defaultIdleFps = sim.getInt32Param(sim.intparam_idle_fps)
sim.setInt32Param(sim.intparam_idle_fps, 0)

# Run a simulation in stepping mode:
client.setStepping(True)
sim.startSimulation()

# Get all of the elements of the scene.
scene_objects = sim.getObjectsInTree(sim.handle_scene, sim.handle_all, 0)
client.step()  # triggers next simulation step

# Create group of objects
groupHandle = sim.groupShapes(scene_objects, False)
client.step()  # triggers next simulation step

x, y, z = getObjectBoundingBoxSize(groupHandle)

sim.ungroupShape(groupHandle)
client.step()  # triggers next simulation step

boxHandle = sim.createPrimitiveShape(sim.primitiveshape_cuboid,[x, y, z], 0)
client.step()  # triggers next simulation step

# Color
sim.setShapeColor(boxHandle, None, sim.colorcomponent_emission, [0, 255, 0])
client.step()  # triggers next simulation step

# Transparency
sim.setShapeColor(boxHandle, None, sim.colorcomponent_transparency, [0.5])
client.step()  # triggers next simulation step

# Position
sim.setObjectPosition(boxHandle, sim.handle_parent, [0.255, 0.225, 0.225])
client.step()  # triggers next simulation step

# Sleep to appreciate the result
time.sleep(10)

# Finishes the programS
sim.stopSimulation()

# Restore the original idle loop frequency:
sim.setInt32Param(sim.intparam_idle_fps, defaultIdleFps)

print('Program ended')


