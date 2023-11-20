import euclidViewerCoppelia
import time

location = (1, 1, 1)
color = (0, 0, 0)

manager = euclidViewerCoppelia.EuclidViewerCoppelia()
x = manager.addCircle(location, [], 0.25, color, "My circle", True, False)
time.sleep(4)
manager.removeNode(x)
print("Removed the circle")
time.sleep(3)
manager.stopSimulation()