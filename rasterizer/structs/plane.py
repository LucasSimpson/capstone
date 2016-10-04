import numpy as np

# describes a plane, comprised of 3 points
# we also keep a list of the voxels the plane is a part of
class Plane:
    def __init__(self, p0, p1, p2):
        self.p0 = p0
        self.p1 = p1
        self.p2 = p2
        self.voxels = []

    # add to internal list of voxels
    def add_voxel(self, voxel):
        self.voxels += [voxel]

    # check if the line segment [t0, t1] intersects self
    # algorigthm from http://geomalgorithms.com/a06-_intersect-2.html
    def hit(self, r0, r1):

        # get normal
        u = self.p1.vector - self.p0.vector
        v = self.p2.vector - self.p0.vector

        # implementing this by hand is faster than np.cross()
        normal = np.array([
            u[1]*v[2] - u[2]*v[1],
            u[2]*v[0] - u[0]*v[2],
            u[0]*v[1] - u[1]*v[0],
        ])

        # calc if perfectly co-planar. unlikely, but check just in case
        denom = np.dot(normal, r1 - r0)
        if denom == 0:
            # if co-planar, return false. We dont have time for such subtleties
            return False

        # calculate r, where hit with plane is r*(r1-r0).
        r = normal.dot(self.p0.vector - r0) / denom

        # check if hit occurs through line segment. simply check 0 < r < 1
        if not (0 <= r <= 1): # yes this works in python
            return False

        # at this point we know the line segment crosses the theoritcal plane
        # now we check if the hit location is within the triangle describes by t0, t1, t2
        # dont argue formula, check reference
        denom = (u.dot(v))**2 - (u.dot(u) * v.dot(v))
        w = r0 + (r1 - r0)*r - self.p0.vector
        s = ((np.dot(u, v) * np.dot(w, v)) - (np.dot(v, v) * np.dot(w, u))) / denom
        t = ((np.dot(u, v) * np.dot(w, u)) - (np.dot(u, u) * np.dot(w, v))) / denom

        # return hit or naawww
        return s >= 0 and t >= 0 and s + t <= 1
