import euclidViewerCoppelia
import time

location = (0, 0.25, 0.5)
color = (120, 205, 130)

manager = euclidViewerCoppelia.EuclidViewerCoppelia()
manager.addSphere(location, 0.5, color, "QaIeze Pepeh", True)
time.sleep(8)
manager.stopSimulation()