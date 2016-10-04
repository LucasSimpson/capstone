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
scene_builder = SceneBuilder()

print 'Rendering...'
data = []
for a in range (10):
    raster_data = scene_builder\
        .new_scene()\
        .add_plane(
            np.array([a * 10, 50, 50]),
            np.array([a * 10, 50, 0]),
            np.array([a * 10, 0, 50]),
            Color(255 if a == 0 else 128, 0 if a == 0 or a == 9 else 255, 255 if a == 9 else 64)
        )\
        .rasterize()

    for b in range(10):
        data += [raster_data]

Printer.print_out(data)