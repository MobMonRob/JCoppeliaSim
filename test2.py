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

