import numpy as np


# util for points in space
class Point:
    def __init__(self, x, y, z):
        self.vector = np.array([x, y, z])