from structs.color import Color

# describes a voxel
# voxel is pretty basic tbh
# only thing here really is the color we want it to light up
# as, and also the corresponding planes
class Voxel:

    # init to blank voxel
    def __init__(self):
        self.color = Color(False)
        self.planes = []

    @property
    def planes(self):
        return self.planes

    @planes.setter
    def planes(self, value):
        self.planes = value