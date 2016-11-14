# constants file
# TODO this (and the simulator) should grab these from same file for parity

class Config:
    DEGREE_ACC = 2
    RADIAL_RES = 20
    NUM_BLADES = 10
    RADIUS_COEF_START = 0.3

    VOXELS_PER_ROT = int(360.0 / DEGREE_ACC)
    NUM_VOXELS = VOXELS_PER_ROT * RADIAL_RES * NUM_BLADES
