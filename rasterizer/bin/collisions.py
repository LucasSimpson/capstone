import numpy as np


# check if a ray (r0, r1) intersects a plane (p0, p1, p2)
# algorigthm from http://geomalgorithms.com/a06-_intersect-2.html
def ray_plane_intersection(r0, r1, p0, p1, p2):

    # get normal
    u = p1 - p0
    v = p2 - p0

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
    r = normal.dot(p0 - r0) / denom

    # check if hit occurs through line segment. simply check 0 < r < 1
    if not (0 <= r <= 1): # yes this works in python
        return False

    # at this point we know the line segment crosses the theoritcal plane
    # now we check if the hit location is within the triangle describes by t0, t1, t2
    # dont argue formula, check reference
    denom = (u.dot(v))**2 - (u.dot(u) * v.dot(v))
    w = r0 + (r1 - r0)*r - p0
    s = ((np.dot(u, v) * np.dot(w, v)) - (np.dot(v, v) * np.dot(w, u))) / denom
    t = ((np.dot(u, v) * np.dot(w, u)) - (np.dot(u, u) * np.dot(w, v))) / denom

    # return hit or naawww
    return s >= 0 and t >= 0 and s + t <= 1
