import time

from coppeliasim_zmqremoteapi_client import RemoteAPIClient


print('Program started')

# Access to  the CoppeliaSim client
client = RemoteAPIClient()
sim = client.getObject('sim')

# Makes sure that the idle loop runs at full speed for this program:
defaultIdleFps = sim.getInt32Param(sim.intparam_idle_fps)
sim.setInt32Param(sim.intparam_idle_fps, 0)

# Run a simulation in stepping mode:
client.setStepping(True)
sim.startSimulation()

x= 0

# Create shape
capsuleHandle = sim.createPrimitiveShape(sim.primitiveshape_capsule,[0.2, 0.3, 1], 0)
client.step()  # triggers next simulation step

# Orientation
sim.setObjectOrientation(capsuleHandle, sim.handle_parent, [0, 1.57, 0])
client.step()  # triggers next simulation step

# Position
sim.setObjectPosition(capsuleHandle, sim.handle_parent, [0, 0, 0.5])
client.step()  # triggers next simulation step

# Color
sim.setShapeColor(capsuleHandle, None, sim.colorcomponent_emission, [0, 255, 0])
client.step()  # triggers next simulation step

# Transparency
sim.setShapeColor(capsuleHandle, None, sim.colorcomponent_transparency, [0.5])

# Get a handle
dummyHandle = sim.getObject("/Dummy", None)

sim.stopSimulation()

# Restore the original idle loop frequency:
sim.setInt32Param(sim.intparam_idle_fps, defaultIdleFps)

print('Program ended')
