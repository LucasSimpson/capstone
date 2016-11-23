import numpy as np

from raster.base import Shape, Polygon
from scene_builder import SceneBuilder
from structs.color import Color

s = Shape([
    Polygon(
        np.array([50, 100, 100]),
        np.array([50, 100, 0]),
        np.array([50, 0, 100]),
        Color(255, 128, 0)
    ),
    Polygon(
        np.array([50, 0, 0]),
        np.array([50, 100, 0]),
        np.array([50, 0, 100]),
        Color(0, 128, 255)
    )
])


# context:
# (around, radius, height)
# (clockwise, inner -> outer, bottom -> top)

print 'Initializing...'
scene_builder = SceneBuilder(SceneBuilder.CS_RECT)

print 'Rendering...'
data = []
for a in range (1):
    print '%s/10' % (a)

    raster_data = scene_builder\
        .new_scene() \
        .add_object(s)\
        .rasterize()

    data += [raster_data]

# from printers.file_printer import FilePrinter
# printer = FilePrinter(filename="../simulator/data/data.txt")

from printers.arduino_printer import ArduinoPrinter
printer = ArduinoPrinter()

printer.print_out(data)