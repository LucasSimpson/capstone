from structs.color import Color

# describes a voxel
# voxel is pretty basic tbh
# only thing here really is the color we want it to light up
# as, and also the corresponding planes
# self.ray is the path the LED sweeps out during a time unit
class Voxel:

    # init to blank voxel
    def __init__(self, r0, r1):
        self.color = Color(False)
        self._r0 = r0
        self._r1 = r1

    @property
    def r0(self):
        return self._r0

    @property
    def r1(self):
        return self._r1