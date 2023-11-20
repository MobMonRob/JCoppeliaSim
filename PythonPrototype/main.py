import euclidViewerCoppelia
import time

location = (1, 1, 1)
color = (0, 0, 0)

manager = euclidViewerCoppelia.EuclidViewerCoppelia()
x = manager.addCircle(location, [], 1, color, "Summertime", False, False)
time.sleep(8)
manager.stopSimulation()