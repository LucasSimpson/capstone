from scene_builder import SceneBuilder
from printer import Printer
from structs.color import Color
import numpy as np

# benchmarking
# vector: 33.5s on hit func
# full numpy: 44.5s
# numpy with custom cross prod: 24.5s

# context:
# (around, radius, height)
# (clockwise, inner -> outer, bottom -> top)

print 'Initializing...'
scene_builder = SceneBuilder(SceneBuilder.CS_RECT)

print 'Rendering...'
data = []
for a in range (100):
    print '%s/100' % (a)

    raster_data = scene_builder\
        .new_scene() \
        .add_plane(
            np.array([a, 100, 100]),
            np.array([a, 100, 0]),
            np.array([a, 0, 100]),
            Color(255, 128, 0)
        )\
        .add_plane(
            np.array([a, 0, 0]),
            np.array([a, 100, 0]),
            np.array([a, 0, 100]),
            Color(0, 128, 255)
        )\
        .rasterize()

    data += [raster_data]

Printer.print_out(data)