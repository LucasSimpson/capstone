# TODO everything so far only describes 1 frame in time, without considering the LED timings
# this means that so far, from the software, everything is split into frame times. this is
# not the case for the final product, and will have to be adjusted accordingly

from config import Config
from structs.color import Color


# describes 1 frame
class TimeFrame:

    # initializer
    def __init__(self, colors):
        self.colors = colors

    # return lines of string values for write out
    def write_out(self):

        # iter over voxels and append to list
        lines = []
        for color in self.colors:
            lines += [str(color)]

        # return lines
        return lines