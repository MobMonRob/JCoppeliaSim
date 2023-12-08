"""
import euclidViewerCoppelia
import time
import objFileManager


location = (0, 0, 0.5)
color = (0, 255, 0)

manager = euclidViewerCoppelia.EuclidViewerCoppelia()

p1 = (0,0,0)
p2 = (0,0,1)
x = manager.addLine(p1, p2, color, 0.01, "myLabel", True)
time.sleep(6)
print(manager.removeNode(x))
time.sleep(6)
manager.stopSimulation()

corners = [(0.2,-0.5,0),(0.5,-0.2,0),(0.5,0.2,0),(0.2,0.5,0),(-0.2,0.5,0),(-0.5,0.2,0),(-0.5,-0.2,0),(-0.2,-0.5,0)]
manager.addPolygone(location, corners, color, "My Test", True, True)
"""

import math

radius = 0.095
sides = 8

# Number of points
num_points = 8

# Generate x, y coordinates for the circle points
circle_points = [(radius * math.cos(2 * math.pi * i / num_points), radius * math.sin(2 * math.pi * i / num_points), 0) for i in range(sides)]
print(circle_points)

radius = 0.105

# Generate x, y coordinates for the circle points
circle_points = [(radius * math.cos(2 * math.pi * i / num_points), radius * math.sin(2 * math.pi * i / num_points), 0) for i in range(sides)]
print(circle_points)


amountOfVertexes = 1
def connectInnerCircle():   

    f  3//amountOfVertexes 4//amountOfVertexes 2//amountOfVertexes
    f  3//amountOfVertexes 2//amountOfVertexes 1//amountOfVertexes

    f  5//2 6//2 4//2
    f  5//2 4//2 3//2

    f  7//3 8//3 6//3
    f  7//3 6//3 5//3

    f  9//4 10//4 8//4
    f  9//4 8//4 7//4

    f  11//5 12//5 10//5
    f  11//5 10//5 9//5

    f  13//6 14//6 12//6
    f  13//6 12//6 11//6

    f  15//7 16//7 14//7
    f  15//7 14//7 13//7



