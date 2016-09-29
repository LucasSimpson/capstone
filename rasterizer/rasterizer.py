from scene_builder import SceneBuilder
from printer import Printer
from structs.color import Color
from structs.vector import Vector

#s = Scene()\
#    .add_line(Vector(0, 0, 1), Vector(100, 100, 99), Color(255, 0, 0))

#t0 = s.rasterize()

print 'Initializing...'
scene_builder = SceneBuilder()

print 'Rendering...'
data = []
for a in range(10):
    print '%s / 10' % (a)
    scene_builder.new_scene()
    scene_builder.add_line(
        Vector(0, 0, 0),
        Vector(100, 100, a * 10 + 5),
        Color(255 if a == 0 else 0, 0 if a == 0 else 255, 255 if a == 9 else 0)
    )
    raster_data = scene_builder.rasterize()
    for b in range(12):
        data += [raster_data]

Printer.print_out(data)