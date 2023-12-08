"""
This class deals with the .obj files
.obj files can be imported into CoppeliaSim as scene objects
You can also write into a .obj file to set its properties
This class creates and edits a .obj file to generate an usable CoppeliaSim object
"""
import mathAuxiliar

class ObjFileManager:
    def __init__(self):
        # This varaible avoids repeating names
        self.fileCounter = 0

        self.mathAuxiliar = mathAuxiliar.MathAuxiliar()

    """
    @dev: This functions writes the instructions to set all the vertexes (v  x y z) 
          Example
                v  -1 -1 0
                v  1 -1 0
                v  1 1 0
    @param: corners: Point3d[] array of all the 3d points of the corners of the figure
            f: fileManager object to access the specific .obj file
    @returns: None
    @author: Andres Masis
    """
    def writeVertexes(self, corners, f):
         # We add each corner to the obj file
        for point in corners:
            # We get the point with the format: v  x y z
            line = "\nv  " + str(point[0]) + " " + str(point[1]) + " "  + str(point[2])
            f.write(line)

    """
    @dev: This functions writes the instructions of the texture
             usemtl $Material_0
    @param: f: fileManager object to access the specific .obj file
    @returns: None
    @author: Andres Masis
    """
    def writeTexture(self, f):
        # Then we write the generic line to set the texture
        f.write("\n\nusemtl $Material_0\n\n")

    """
    @dev: Writes the lines to connect the vertexes
             f  1//1 2//1 3//1
             f  1//1 3//1 4//1
             f  1//1 4//1 5//1
          Notice that the lines always start with 1//1
          The second element of the line is i//1
          The third element of the line i+1//1
    @param: limit: integer with the amount of corners that we have
            f: fileManager object to access the specific .obj file
    @returns: None
    @author: Andres Masis
    """
    def fillObject(self, limit, f):
        # We start writing the digits i//1 and i+1//1
        # We start from 2 because 1 is always there
        # to the last corner (amount of corners)
        for i in range(2, limit):
            f.write("\nf  1//1 " + str(i) + "//1 " + str(i+1) + "//1 ")
            # f  1//1 i//1 i+1//1

    """
    @dev: This functions writes the necessary instructions in a .obj file given its file manager object
          First it writes all the vertexes (v  x y z) 
          Then it writes the texture line (usemtl $Material_0)
          Then it writes the line to fill the polygone (f  1//1 2//1 3//1)
          Example of the file:
                v  -1 -1 0
                v  1 -1 0
                v  1 1 0
                v  -1 1 0

                usemtl $Material_0

                f 1//1 2//1 3//1 
                f 1//1 3//1 4//1 
    @param: corners: Point3d[] array of all the 3d points of the corners of the figure
            fullPath: string with the absolute path of the .obj to use
    @returns: None
    @author: Andres Masis
    """
    def editFlatObjFile(self, corners, fullPath):
        # Open the file in write mode, so it creates the file too
        f = open(fullPath, "w")

        # Writes the vertexes: v  x y z
        self.writeVertexes(corners, f)
        # Writes the texture line: usemtl $Material_0
        self.writeTexture(f)
        # Writes the lines that connect the vertexes:
        limit = len(corners) 
        self.fillObject(limit, f)

        # close the file
        f.close() 

    """
    @dev: This functions creates an obj file in the polygones folder
          Then (with the help of another function) it writes the necessary intructions in this file
          When it is ready, it closes the file and returns the path of this generated file
          IMPORTANT: This function does not deal with the order of points
          A bad order in points can lead to weird results
          But this ordering is out of the scope of this project
    @param: corners: Point3d[] array of all the 3d points of the corners of the figure
    @returns: string with the path of the generated new file
    @author: Andres Masis
    """
    def createPolygoneFile(self, corners):
        # We build the path of the file
        filePath = "C:\\Users\\rahm-\\Documents\\coppeliaPythonZMQ\\JCoppeliaSim\\PythonPrototype\\models\\polygones\\"
        fileName = "polygone" + str(self.fileCounter) + ".obj"  # fileCounter to create new names
        fullPath = filePath + fileName

        # Deals with the .obj intructions
        self.editFlatObjFile(corners, fullPath)

        # Updates the counter to avoid repeated names
        self.fileCounter += 1

        # The .obj file is ready, returns the path were it is located so then CoppeliaSim can load it
        return fullPath
    
    """
    @dev: This function creates a .obj file of a flat partial circle of n degrees
          It first creates an empty .obj file in the angles folder
          Then it uses an auxliary function to calculate the coordinates of the circle
          Then it writes all that information into the .obj file with the help of the editFile() function of this class
          Then it closes the file and finally it returns its full path
    """
    def createAngleFlatCircle(self, angle):
        # We build the path of the file
        filePath = "C:\\Users\\rahm-\\Documents\\coppeliaPythonZMQ\\JCoppeliaSim\\PythonPrototype\\models\\angles\\"
        fileName = "flatAngle" + str(angle) + "Degrees.obj"  # fileCounter to create new names
        fullPath = filePath + fileName

        # Calls the auxiliary function of the MathAuxliar class to calculate the coordinates of the circle´s corners
        radius = 0.1
        corners = self.mathAuxiliar.calculateCirclePoints(angle, radius)

        # Deals with the .obj intructions
        self.editFlatObjFile(corners, fullPath)

        # The .obj file is ready, returns the path were it is located so then CoppeliaSim can load it
        return fullPath

        def createAngle3DLine(self, angle):
        # We build the path of the file
        filePath = "C:\\Users\\rahm-\\Documents\\coppeliaPythonZMQ\\JCoppeliaSim\\PythonPrototype\\models\\angles\\"
        fileName = "3dAngle" + str(angle) + "Degrees.obj"  # fileCounter to create new names
        fullPath = filePath + fileName

        # Calls the auxiliary function of the MathAuxliar class to calculate the coordinates of the circle´s corners
        radius = 0.1
        corners = self.mathAuxiliar.calculateCirclePoints(angle, radius)

        # Deals with the .obj intructions
        self.editFlatObjFile(corners, fullPath)

        # The .obj file is ready, returns the path were it is located so then CoppeliaSim can load it
        return fullPath

