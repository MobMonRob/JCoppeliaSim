"""
import math


def toEuler(rot, angle):
        heading = 0.0
        attitude = 0.0
        bank = 0.0
   
        if rot.lengthSquared() == 0:
            raise ValueError("Length of the given rotation vector is 0 is not allowed!")
        
        s = math.sin(angle)
        c = math.cos(angle)
        t = 1 - c
        
        if (rot.x*rot.y*t + rot.z*s) > 0.998:
            # north pole singularity detected
            heading = 2 * math.atan2(rot.x * math.sin(angle / 2), math.cos(angle / 2))
            attitude = math.PI / 2
            bank = 0
            return (heading, attitude, bank)
        
        if (rot.x * rot.y * t + rot.z * s) < -0.998:
            # south pole singularity detected
            heading = -2 * math.atan2(rot.x * math.sin(angle / 2), math.cos(angle / 2))
            attitude = -math.PI / 2
            bank = 0
            return (heading, attitude, bank)
        
        heading = math.atan2(rot.y * s - rot.x * rot.z * t, 1 - (rot.y * rot.y + rot.z * rot.z) * t)
        attitude = math.asin(rot.x * rot.y * t + rot.z * s)
        bank = math.atan2(rot.x * s - rot.y * rot.z * t, 1 - (rot.x * rot.x + rot.z * rot.z) * t)
        return (heading, attitude, bank)



def getEulerAnglesToRotateFromZ(targetDir):
        # Vector in direction of the z-Achse
        z = (0,0,1)
       
        # Rotation axis upright to z and target direction
        rot = (0,0,0)
        rot.cross(z, targetDir)
        
        # Rotation angle betwee z-axis and target direction
        alpha = z.angle(targetDir)
        
        return toEuler(rot, alpha)
"""
# Make sure to have the add-on "ZMQ remote API"
# running in CoppeliaSim
#
# All CoppeliaSim commands will run in blocking mode (block
# until a reply from CoppeliaSim is received). For a non-
# blocking example, see simpleTest-nonBlocking.py

import time

from coppeliasim_zmqremoteapi_client import RemoteAPIClient


print('Program started')

client = RemoteAPIClient()
sim = client.require('sim')

# Run a simulation in stepping mode:
sim.setStepping(True)
sim.startSimulation()

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
client.step()  # triggers next simulation step

sim.setModelProperty(capsuleHandle, sim.modelproperty_not_dynamic)
client.step()  # triggers next simulation step

sim.setObjectAlias(capsuleHandle, "Pepe")
client.step()  # triggers next simulation step

time.sleep(10)

sim.stopSimulation()


print('Program ended')
