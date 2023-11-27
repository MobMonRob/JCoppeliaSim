"""
This class deals with the .obj files
.obj files can be imported into CoppeliaSim as scene objects
You can also write into a .obj file to set its properties
This class creates and edits a .obj file to generate an usable 
CoppeliaSim object
"""

class ObjFileManager:
    def __init__(self):
        # This varaible avoids repeating names
        self.fileCounter = 0

    """
    @dev: This functions creates an obj file
          First it writes all the vertexes (v  x y z)
          Then it writes the texture line (usemtl $Material_0)
          Then it writes the line to fill the polygone (f  1//1 2//1 3//1)
          Example of the file:
                v  -1 -1 0
                v  1 -1 0
                v  1 1 0
                v  -1 1 0

                usemtl $Material_0

                f 1//1 2//1 3//1 4//1 
         IMPORTANT: This function does not deal with the order of points
         A bad order in points can lead to weird results
         But this ordering is out of the scope of this project
    @param: corners: Point3d[] array of all the 3d points of the corners of the figure
    @returns: string with the path of the generated new file
    @author: Andres Masis
    """
    def createObjFile(self, corners):
        # We build the path of the file
        filePath = "C:\\Users\\rahm-\\Documents\\coppeliaPythonZMQ\\JCoppeliaSim\\PythonPrototype\\models\\polygones\\"
        fileName = "polygone" + str(self.fileCounter) + ".obj"  # fileCounter to create new names
        fullPath = filePath + fileName

        # Open the file in write mode, so it creates the file too
        f = open(fullPath, "w")

        # We add each corner to the obj file
        for point in corners:
            # We get the point with the format: v  x y z
            line = "\nv  " + str(point[0]) + " " + str(point[1]) + " "  + str(point[2])
            f.write(line)

        # Then we write the generic line to set the texture
        f.write("\n\nusemtl $Material_0\n\n")
        
        # We write the last line with the format
        # f  1//1 2//1 3//1 4//1

        # We start the line to fill the polygone with f
        f.write("f ")

        # We start writing the digits i//1
        # We go from 1 to the last corner (amount of corners)
        limit = len(corners)+1
        for i in range(1, limit):
            f.write(str(i) + "//1 ")

        f.close() # close the file

        # Updates the counter to avoid repeated names
        self.fileCounter += 1

        # The .obj file is ready, returns the path were it is located so then CoppeliaSim can load it
        return fullPath
