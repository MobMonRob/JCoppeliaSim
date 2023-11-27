import euclidViewerCoppelia
import time
import objFileManager


location = (0, 0, 0.5)
color = (0, 255, 0)

manager = euclidViewerCoppelia.EuclidViewerCoppelia()
"""
p1 = (0,0,0)
p2 = (0,0,1)
x = manager.addLine(p1, p2, color, 0.01, "myLabel", True)
time.sleep(6)
print(manager.removeNode(x))
time.sleep(6)
manager.stopSimulation()
"""
corners = [(-1,-1,0),(1,-1,0),(1,1,0),(-1,1,0)]
manager.addPolygone(location, corners, color, "My Test", True, True)
