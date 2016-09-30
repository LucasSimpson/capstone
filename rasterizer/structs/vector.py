# 3-space vector
class Vector:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        # safety cast to float
        self.x = 1.0 * x
        self.y = 1.0 * y
        self.z = 1.0 * z

    # dimension-wise addition
    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    # dimension-wise subtraction
    def __sub__(self, other):
        return Vector(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )

    # scalar mult
    def scale(self, scalar):
        return Vector(
            self.x * scalar,
            self.y * scalar,
            self.z * scalar
        )

    # dimension-wise multiplication
    def __mul__(self, other):
        return Vector(
            self.x * other.x,
            self.y * other.y,
            self.z * other.z
        )

    # dot product
    def dot(self, other):
        return sum([
            self.x * other.x,
            self.y * other.y,
            self.z * other.z
        ])

    # cross prodcut
    def cross (self, other):
        return Vector (
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )

    def __str__(self):
        return 'Vector(%s,%s,%s)' % (self.x, self.y, self.z)