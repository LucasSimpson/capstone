from base import Printer
from config import Config

# prints out to arduino
class ArduinoPrinter(Printer):

    # takes in a color as a string and transforms it into the bits necessary according to the color resolution
    def color_str_to_arduino(self, color_str):
        res = Config.COLOR_RES

        # samples a float value with Config.COLOR_RES resolution, on range (0,255)
        def descretize(num):
            bins = 2**res
            bin = int((float(num) / 256.0) * bins)
            return bin

        def to_binary(num):
            return bin(num)

        # for now well just return strings of 1's and 0's
        if color_str is '0':
            rgb = [0,0,0]
        else:
            rgb = map(lambda x: descretize(int(x)), color_str.split(','))
        return map(to_binary, rgb)

    def print_out(self, time_frames):
        # time_frames is an array of time frames
        # each frame has a flattened 3D list of colors of the order (height, radius, angle)
        # we have to transform into a flattened 3D list of the order (blade, radius, timestep)
        # This makes our job extremely easy; to transfrom from the original 3d space list to
        # the new (2d space, 1d time) list, there is no work required :)
        # Okay, I lied. There's a little work required. Because every other blade is offset by 180, it requires
        # that every other blades list be rotated by 1/2.
        # To put it programmatically, every other entry of the 2nd dimension of the list has to be rotated by
        # half its length. To do this, we rebuild the 3D data structure from the flattened list, rotate every other
        # entry on the second dimension, then re-flatten it. THEN we can write to arduino

        # rename some params for readability
        X = Config.VOXELS_PER_ROT
        Y = Config.RADIAL_RES
        Z = Config.NUM_BLADES

        for frame in time_frames:
            # get color data
            color_data = frame.write_out()

            # rebuild 3D list
            data = [[[color_data[a*Z + b*Y + c*X] for c in range(X)] for b in range(Y)] for a in range(Z)]

            # rotate every other element on 2nd dimension by 1/2
            for a in range(len(data)):
                if a % 2 == 0:
                    l = len(data[a])
                    data[a] = data[a][l/2:] + data[a][:l/2]

            # flatten
            color_data = []
            for a in data:
                for b in a:
                    color_data += b

            # write to arduino
            for color in color_data:

                # TODO actually write to arduino
                print self.color_str_to_arduino(color)

