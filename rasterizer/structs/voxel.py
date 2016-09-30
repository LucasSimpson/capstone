from structs.color import Color

# describes a voxel
# limits is a list of vectors describing the 8 corners of the voxels volume
# order is clockwise from top right, lower level, then same on top level
# perspective is facing outward
# ex:
#     3------0
#      \    /
#       2--1
class Voxel:

    # init to blank voxel
    def __init__(self, bounds):
        self.color = Color(False)
        self.bounds = bounds

        # iter on all triangles comprising the voxel boundaries and check for hit
        # dont ask me on the indicies, just trust me
        # if you're curious; its all 6 six planes described clockwise facing inwards
        self.surfaces = [
            [self.bounds[0], self.bounds[3], self.bounds[2], self.bounds[1]],
            [self.bounds[0], self.bounds[1], self.bounds[5], self.bounds[4]],
            [self.bounds[1], self.bounds[2], self.bounds[6], self.bounds[5]],
            [self.bounds[2], self.bounds[3], self.bounds[7], self.bounds[6]],
            [self.bounds[3], self.bounds[0], self.bounds[4], self.bounds[7]],
            [self.bounds[4], self.bounds[5], self.bounds[6], self.bounds[7]],
        ]

    # determine if a ray intersects a triangle
    # algorigthm from http://geomalgorithms.com/a06-_intersect-2.html
    @staticmethod
    def _ray_plane_intersect(p0, p1, t0, t1, t2):

        # get normal
        u = t1 - t0
        v = t2 - t0
        normal = (u).cross(v)

        # calc if perfectly co-planar. unlikely, but check just in case
        denom = normal.dot(p1 - p0)
        if denom == 0:
            # if co-planar, return false. We dont have time for such subtleties
            return False

        # calculate r, where hit with plane is r*(p1-p0).
        r = normal.dot(t0 - p0) / denom

        # check if hit occurs through line segment. simply check 0 < r < 1
        if not (0 <= r <= 1): # yes this works in python
            return False

        # at this point we know the line segment crosses the theoritcal plane
        # now we check if the hit location is within the triangle describes by t0, t1, t2
        # dont argue formula, check reference
        denom = (u.dot(v))**2 - (u.dot(u) * v.dot(v))
        w = p0 + (p1 - p0).scale(r) - t0
        s = ((u.dot(v) * w.dot(v)) - (v.dot(v) * w.dot(u))) / denom
        t = ((u.dot(v) * w.dot(u)) - (u.dot(u) * w.dot(v))) / denom

        # return hit or naawww
        return s >= 0 and t >= 0 and s + t <= 1

    # return true if line described by v1, v2 intersects voxel
    def hit(self, v1, v2):
        for surface in self.surfaces:
            if Voxel._ray_plane_intersect(v1, v2, surface[0], surface[1], surface[2]):
                return True

            if Voxel._ray_plane_intersect(v1, v2, surface[0], surface[2], surface[3]):
                return True

        return False