from scene import Scene
from printer import Printer
from structs.color import Color
from structs.vector import Vector

#s = Scene()\
#    .add_line(Vector(0, 0, 1), Vector(100, 100, 99), Color(255, 0, 0))

#t0 = s.rasterize()

print 'building scenes..'
scenes = []
for a in range (10):
    scenes += [Scene().add_line(Vector(0, 0, 0), Vector(100, 100, a * 10 + 5), Color(255 if a == 0 else 0, 0 if a == 0 else 255, 0))]

data = []
for scene in scenes:
    print 'raserrizing..'
    raster = scene.rasterize()
    for a in range(12):
        data += [raster]

Printer.print_out(data)