from scene_builder import SceneBuilder
from printer import Printer
from structs.color import Color
import numpy as np

from raster.base import Shape, Polygon

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
for a in range (10):
    print '%s/100' % (a)

    raster_data = scene_builder\
        .new_scene() \
        .add_object(s)\
        .rasterize()

    data += [raster_data]

Printer.print_out(data)