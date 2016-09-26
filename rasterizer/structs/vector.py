# 3-space vector
class Vector:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    # dimension-wise multiplication
    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y, self.z * other.z)