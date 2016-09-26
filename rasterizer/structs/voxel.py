from structs.color import Color

# describes a voxel
# limits is a list of vectors describing the 8 corners of the voxels volume
# order is clockwise from top right, lower level, then same on top level
# perspective is facing outward
# ex:
#     4------1
#      \    /
#       3--2
class Voxel:

    # init to blank voxel
    def __init__(self, limits):
        self.color = Color(False)
        self.limits = limits

    # return true if line described by v1, v2 intersects voxel
    def hit(self, v1, v2):
        return True