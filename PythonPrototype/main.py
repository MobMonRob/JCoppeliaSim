import euclidViewerCoppelia
import time

location = (0, 0.25, 0.5)
color = (120, 205, 130)

manager = euclidViewerCoppelia.EuclidViewerCoppelia()
x = manager.loadModel("C:\\Users\\rahm-\\Documents\\coppeliaPythonZMQ\\JCoppeliaSim\\PythonPrototype\\models\\DottedCircle.obj")
time.sleep(8)
manager.stopSimulation()