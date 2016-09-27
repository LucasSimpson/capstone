import unittest

from structs.voxel import Voxel
from structs.vector import Vector


class VoxelTest(unittest.TestCase):
    def setUp(self):
        self.p0 = Vector(0, 0, 50)
        self.p1 = Vector(100, 0, 50)
        self.p2 = Vector(0, 100, 50)

    def test_ray_intersection_hit01(self):
        r0 = Vector(10, 10, 0)
        r1 = Vector(10, 10, 100)
        self.assertTrue(Voxel._ray_plane_intersect(r0, r1, self.p0, self.p1, self.p2))

    def test_ray_intersection_hit02(self):
        r0 = Vector(0, 0, 0)
        r1 = Vector(50, 50, 100)
        self.assertTrue(Voxel._ray_plane_intersect(r0, r1, self.p0, self.p1, self.p2))

    def test_ray_intersection_hit04(self):
        r0 = Vector(-400, -400, 45)
        r1 = Vector(450, 450, 55)
        self.assertTrue(Voxel._ray_plane_intersect(r0, r1, self.p0, self.p1, self.p2))

    def test_ray_intersection_hit05(self):
        r0 = Vector(1, 1, 0)
        r1 = Vector(1, 1, 100)
        self.assertTrue(Voxel._ray_plane_intersect(r0, r1, self.p0, self.p1, self.p2))

    def test_ray_intersection_hit06(self):
        r0 = Vector(99, 1, 0)
        r1 = Vector(99, 1, 100)
        self.assertTrue(Voxel._ray_plane_intersect(r0, r1, self.p0, self.p1, self.p2))

    def test_ray_intersection_hit07(self):
        r0 = Vector(1, 99, 0)
        r1 = Vector(1, 99, 100)
        self.assertTrue(Voxel._ray_plane_intersect(r0, r1, self.p0, self.p1, self.p2))



    def test_ray_intersection_miss01(self):
        r0 = Vector(1, 99, 0)
        r1 = Vector(1, 99, 49)
        self.assertTrue(Voxel._ray_plane_intersect(r0, r1, self.p0, self.p1, self.p2))

    def test_ray_intersection_miss02(self):
        r0 = Vector(0, -1, 0)
        r1 = Vector(0, 0, 100)
        self.assertTrue(Voxel._ray_plane_intersect(r0, r1, self.p0, self.p1, self.p2))

    def test_ray_intersection_miss03(self):
        r0 = Vector(45, 100, 0)
        r1 = Vector(45, 100, 100)
        self.assertTrue(Voxel._ray_plane_intersect(r0, r1, self.p0, self.p1, self.p2))

    def test_ray_intersection_miss04(self):
        r0 = Vector(100, 1, 0)
        r1 = Vector(100, 1, 100)
        self.assertTrue(Voxel._ray_plane_intersect(r0, r1, self.p0, self.p1, self.p2))

    def test_ray_intersection_miss05(self):
        r0 = Vector(1, 100, 0)
        r1 = Vector(1, 100, 100)
        self.assertTrue(Voxel._ray_plane_intersect(r0, r1, self.p0, self.p1, self.p2))
