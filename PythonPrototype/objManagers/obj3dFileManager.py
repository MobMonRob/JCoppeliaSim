import objManagers.objFileManager

class EuclidViewerCoppelia(objManagers.objFileManager.ObjFileManager):

    def __init__(self):
        # Creates an object to get methods calculateLengthLine() or calculateCenter()
        self.mathAuxiliar = mathClasses.mathAuxiliar.MathAuxiliar()

        # Calls the constructor of the superclass to get all the CoppeliaSim methods
        super().__init__()