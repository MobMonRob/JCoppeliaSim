"""
This class provided methids to calculate certain mathematical operations
This class contains a method to calculate the distance between 2 points
It also contains a method to calculate the middle point between 2 3D points
It also deals with the Euler angles
"""
import math

class MathAuxiliar:

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
    @dev: Auxiliary function
            This function calculates the center of a line given 2 points
    @param: p1: Point3d with the coordinates x1, y1, z1
            p2: Point3d with the coordinates x2, y2, z2
    @returns: x, y, z values of the center
    @author: Andres Masis
    """
    def calculateCenter(self, p1, p2):
        # Gets the indivudual values
        x1, y1, z1 = p1
        x2, y2, z2 = p2

        # Calculates the average to get the center in each dimension
        x = (x1+x2) / 2
        y = (y1+y2) / 2
        z = (z1+z2) / 2

        return x, y, z
    