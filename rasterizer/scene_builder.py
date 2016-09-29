from config import Config

from structs.voxel import Voxel
from structs.vector import Vector
from structs.color import Color

from time_frame import TimeFrame


# describes a static image on a high level basis
class SceneBuilder:
    # construct blank grid
    def __init__(self):

        # initialize all voxels
        # right now this assumes radial coordiantes and not cartesian for ease of use
        # describes a (VOXELS_PER_ROT) * (RADIAL_RES) * (NUM_BLADES) volume
        #                width         *   depth      *     height

        # calc scaling vector
        scale_vec = Vector(
            100.0 / Config.VOXELS_PER_ROT,
            100.0 / Config.RADIAL_RES,
            100.0 / Config.NUM_BLADES
        )

        # calc all voxels
        self.voxels = []
        for i in range(Config.NUM_BLADES):
            for j in range(Config.RADIAL_RES):
                for k in range(Config.VOXELS_PER_ROT):
                    bounds = [
                        Vector(k+1, j+1, i),
                        Vector(k+1, j, i),
                        Vector(k, j, i),
                        Vector(k, j+1, i),
                        Vector(k + 1, j + 1, i+1),
                        Vector(k + 1, j, i+1),
                        Vector(k, j, i+1),
                        Vector(k, j + 1, i+1),
                    ]

                    # scale everything to be in a 100x100x100 coordinate system
                    bounds = map(lambda vec: vec * scale_vec, bounds)

                    # create voxel and add to list
                    self.voxels += [Voxel(bounds)]

    # resets shit for a new scene
    def new_scene(self):
        for voxel in self.voxels:
            voxel.color = Color(False)

    # add a line to the scene
    def add_line(self, v1, v2, color):
        # calc intersection of line with all voxels and colorize
        for voxel in self.voxels:
            if voxel.hit(v1, v2):
                voxel.color = color

        # chaining, fuck yea
        return self

    # export to TimeFrame class
    def rasterize(self):
        return TimeFrame(map(lambda voxel: voxel.color, self.voxels))
