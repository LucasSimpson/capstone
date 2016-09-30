from scene_builder import SceneBuilder
from printer import Printer
from structs.color import Color
from structs.vector import Vector

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
        .add_line(Vector(0, 100, a * 10 + 5), Vector(100, 100, a * 10 + 5), Color(255 if a == 0 else 0, 0 if a == 0 or a == 9 else 255, 255 if a == 9 else 0))\
        .add_line(Vector(0, 0, 100 - a * 10 - 5), Vector(100, 0, 100 - a * 10 - 5), Color(255 if a == 0 else 0, 0 if a == 0 or a == 9 else 255, 255 if a == 9 else 0))\
        .rasterize()

    for b in range(10):
        data += [raster_data]

Printer.print_out(data)