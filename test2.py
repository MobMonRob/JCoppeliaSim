import numpy as np

def euler_angles(direction, up):
    # Normalize input vectors
    direction = np.array(direction) / np.linalg.norm(direction)
    up = np.array(up) / np.linalg.norm(up)

    # Calculate heading
    heading = np.arctan2(direction[1], direction[0])

    # Calculate pitch
    pitch = np.arcsin(direction[2])

    # Calculate bank
    right = np.cross(direction, up)
    bank = np.arccos(np.dot(right, np.array([1, 0, 0])))

    return (heading, pitch, bank)

p1 = np.array((0, 0, 1))
p2 = np.array((0, 0, 0))

a, b, g = euler_angles(p1, p2)

print(a)