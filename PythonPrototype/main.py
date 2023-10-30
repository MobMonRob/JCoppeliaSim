import euclidViewerCoppelia

location = (0, 0, 1)
color = (0, 255, 0)

manager = euclidViewerCoppelia.EuclidViewerCoppelia()
manager.addSphere(location, 0.5, color, "My circle", True)