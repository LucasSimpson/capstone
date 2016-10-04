from config import Config

from structs.voxel import Voxel
from structs.color import Color
from structs.point import Point
from structs.plane import Plane

from time_frame import TimeFrame

import numpy as np


# describes a static image on a high level basis
class SceneBuilder:
    # construct blank grid
    def __init__(self):

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
        X = Config.NUM_BLADES
        Y = Config.RADIAL_RES
        Z = Config.VOXELS_PER_ROT

        # create blank voxels
        # order is important!
        voxels = [[[Voxel() for i in range(Z)] for j in range(Y)] for k in range(X)]

        # create all points
        points = [[[Point(i, j, k) for i in range(Z+1)] for j in range(Y+1)] for k in range(X+1)]

        # create all planes and assign to voxels
        # XY planes
        self.planes = []
        for i in range(X):
            for j in range(Y):
                for k in range(Z + 1):
                    # create
                    p1 = Plane(
                        points[i][j][k],
                        points[i + 1][j][k],
                        points[i][j + 1][k]
                    )
                    p2 = Plane(
                        points[i + 1][j + 1][k],
                        points[i + 1][j][k],
                        points[i][j + 1][k]
                    )

                    # assign
                    self.planes += [p1, p2]
                    if k != 0:
                        p1.add_voxel(voxels[i][j][k - 1])
                        p2.add_voxel(voxels[i][j][k - 1])
                    if k != Z:
                        p1.add_voxel(voxels[i][j][k])
                        p2.add_voxel(voxels[i][j][k])


        # XZ
        for i in range(X):
            for j in range(Y + 1):
                for k in range(Z):
                    # create
                    p1 = Plane(
                        points[i][j][k],
                        points[i + 1][j][k],
                        points[i][j][k + 1]
                    )
                    p2 = Plane(
                        points[i + 1][j][k + 1],
                        points[i + 1][j][k],
                        points[i][j][k + 1]
                    )

                # assign
                self.planes += [p1, p2]
                if j != 0:
                    p1.add_voxel(voxels[i][j - 1][k])
                    p2.add_voxel(voxels[i][j - 1][k])
                if j != Y:
                    p1.add_voxel(voxels[i][j][k])
                    p2.add_voxel(voxels[i][j][k])

        # YZ
        for i in range(X + 1):
            for j in range(Y):
                for k in range(Z):
                    p1 = Plane(
                        points[i][j][k],
                        points[i][j + 1][k],
                        points[i][j][k + 1]
                    )
                    p2 = Plane(
                        points[i][j + 1][k + 1],
                        points[i][j + 1][k],
                        points[i][j][k + 1]
                    )

                    # assign
                    self.planes += [p1, p2]
                    if i != 0:
                        p1.add_voxel(voxels[i - 1][j][k])
                        p2.add_voxel(voxels[i - 1][j][k])
                    if i != X:
                        p1.add_voxel(voxels[i][j][k])
                        p2.add_voxel(voxels[i][j][k])

        # flatten points list
        self.points = []
        for i in points:
            for j in i:
                self.points += j

        # flatten voxels list
        self.voxels = []
        for i in voxels:
            for j in i:
                self.voxels += j

        # scale shit so thats its all in a 100x100x100 CS
        for point in self.points:
            point.vector = point.vector * scale_vec


    # resets shit for a new scene
    def new_scene(self):
        for voxel in self.voxels:
            voxel.color = Color(False)

        # freaking 2 chainz over here...
        return self

    # add a line to the scene
    def add_line(self, v1, v2, color):
        # calc intersection of line with all voxels and colorize
        for plane in self.planes:
            if plane.hit(v1, v2):
                for voxel in plane.voxels:
                    voxel.color = color

        # chaining, fuck yea
        return self

    # export to TimeFrame class
    def rasterize(self):
        return TimeFrame(map(lambda voxel: voxel.color, self.voxels))
