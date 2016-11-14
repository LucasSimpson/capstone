import numpy as np

from bin.collisions import ray_plane_intersection


# defines any object that can be rasterized
class Rasterizable(object):
    def __init__(self, *args, **kwargs):
        pass

    # check collisions and colorize
    def deal_with(self, voxel):
        raise NotImplemented("%s must implement deal_with() method" % (self.__class__))


# basic polygon
class Polygon(Rasterizable):

    # 3 points defining a triangle in 3space + color
    def __init__(self, p0, p1, p2, color):
        super(Polygon, self).__init__()
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
        self.color = color

    # check collision
    def deal_with(self, voxel):
        if ray_plane_intersection(voxel.r0, voxel.r1, self.p0, self.p1, self.p2):
            voxel.color = self.color

    # transform via transformation matrix
    def transform(self, M):
        self.p0 = np.dot(self.p0, M)
        self.p1 = np.dot(self.p1, M)
        self.p2 = np.dot(self.p2, M)

    # debugging
    def __str__(self):
        return "Polygon\n\t(%s,\n\t%s,\n\t%s\n)" % (self.p0, self.p1, self.p2)


# defines a collection of polygons
class Shape(set, Rasterizable):

    # defer to polygons
    def deal_with(self, voxel):
        for polygon in self:
            polygon.deal_with(voxel)

