import numpy as np

from bin.collisions import ray_plane_intersection
from config import Config
from structs.color import Color
from structs.voxel import Voxel
from time_frame import TimeFrame


# describes a static image on a high level basis
class SceneBuilder:
    # constants for grid specification
    CS_RECT = "rectangular_coordinate_system"
    CS_CIRC = "circular_coordinate_system"

    # construct blank grid
    def __init__(self, cs=None):
        if not cs:
            cs = SceneBuilder.CS_CIRC

        # initialize all voxels
        # right now this assumes radial coordiantes and not cartesian for ease of use
        # describes a (VOXELS_PER_ROT) * (RADIAL_RES) * (NUM_BLADES) volume
        #                width         *   depth      *     height

        # calc scaling vector
        scale_vec = np.array([
            100.0 / Config.VOXELS_PER_ROT,
            100.0 / Config.RADIAL_RES,
            100.0 / Config.NUM_BLADES
        ])

        # rename some params for readability
        X = Config.VOXELS_PER_ROT
        Y = Config.RADIAL_RES
        Z = Config.NUM_BLADES

        # init voxels based on CS
        if cs == SceneBuilder.CS_CIRC:
            voxels = [[[Voxel(
                np.array([i, j + 0.5, k + 0.5]) * scale_vec,
                np.array([i + 1, j + 0.5, k + 0.5]) * scale_vec,
            ) for i in range(X)] for j in range(Y)] for k in range(Z)]
        elif cs == SceneBuilder.CS_RECT:
            voxels = [[[Voxel(
                np.array([
                   50.0 * (float(j) / Y) * np.sin(2 * np.pi * float(i) / X) + 50,
                   50.0 * (float(j) / Y) * np.cos(2 * np.pi * float(i) / X) + 50,
                   100.0 * (float(k) / Z),
                ]),
                np.array([
                   50.0 * (float(j) / Y) * np.sin(2 * np.pi * (float(i) + 1) / X) + 50,
                   50.0 * (float(j) / Y) * np.cos(2 * np.pi * (float(i) + 1) / X) + 50,
                   100.0 * (float(k) / Z),
                ]),
            ) for i in range(X)] for j in range(Y)] for k in range(Z)]

        # flatten voxels
        self.voxels = []
        for i in voxels:
            for j in i:
                self.voxels += j


    # resets shit for a new scene
    def new_scene(self):
        for voxel in self.voxels:
            voxel.color = Color(False)

        # freaking 2 chainz over here...
        return self


    # add a plane for intersection with
    def add_plane(self, p0, p1, p2, color):

        # iter voxels and check collision
        for voxel in self.voxels:
            if ray_plane_intersection(voxel.r0, voxel.r1, p0, p1, p2):
                voxel.color = color

        # chainin FTW
        return self


    # export to TimeFrame class
    def rasterize(self):
        return TimeFrame(map(lambda voxel: voxel.color, self.voxels))
