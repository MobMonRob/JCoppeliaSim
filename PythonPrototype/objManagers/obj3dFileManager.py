import objManagers.objFileManager
import mathClasses.mathAuxiliar

"""
FOR TESTING PURPOSES, THIS CLASS SAVES ITS FILES IN AN ABSOLUTE PATH
BE CAREFUL IF YOU WANT TO HAVE THE FILES IN ANOTHER LOCATION OR RUNNING IN ANOTHER COMPUTER
"""

class Obj3dFileManager(objManagers.objFileManager.ObjFileManager):

    def __init__(self):
        # Creates an object to get methods calculateLengthLine() or calculateCenter()
        self.mathAuxiliar = mathClasses.mathAuxiliar.MathAuxiliar()

    def generateCompleteList(self, listDown):
        del listDown[0]
        
        listUp = [t[:-1] + (0.01,) for t in listDown]

        listComplete = [None] * (len(listDown) + len(listUp)) # create a list of the correct length
        listComplete[::2] = listDown # assign the elements of list1 to the even indices
        listComplete[1::2] = listUp # assign the elements of list2 to the odd indices

        return listComplete


    def createAngle3DLine(self, angle):
        # We build the path of the file
        filePath = "C:\\Users\\rahm-\\Documents\\coppeliaPythonZMQ\\JCoppeliaSim\\PythonPrototype\\models\\angles\\"
        fileName = "3dAngle" + str(angle) + "Degrees.obj"  # fileCounter to create new names
        fullPath = filePath + fileName

        # Calls the auxiliary function of the MathAuxliar class to calculate the coordinates of the INNER circle´s corners
        radius = 0.0095

        innerCircleDown = self.mathAuxiliar.calculateCirclePoints(angle, radius)

        innerCircleComplete = self.generateCompleteList(innerCircleDown)

       
        # The .obj file is ready, returns the path were it is located so then CoppeliaSim can load it
        return fullPath


