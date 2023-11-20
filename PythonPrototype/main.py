import euclidViewerCoppelia
import time

location = (1, 1, 1)
color = (0, 0, 0)

manager = euclidViewerCoppelia.EuclidViewerCoppelia()
x = manager.addCube(location, [], 0.5, color, "Tanzkurs", True)
time.sleep(8)
manager.stopSimulation()