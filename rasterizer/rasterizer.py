from scene import Scene
from printer import Printer
from structs.color import Color
from structs.vector import Vector

s = Scene()\
    .add_line(Vector(10, 10, 10), Vector(40, 10, 10), Color(255, 0, 0))\
    .add_line(Vector(10, 90, 90), Vector(90, 90, 90), Color(0, 255, 0))

t0 = s.rasterize()

Printer.print_out([t0])