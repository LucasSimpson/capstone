from scene import Scene
from printer import Printer
from structs.color import Color

t0 = Scene().add_line(None, None, Color(255, 0, 0)).rasterize()

Printer.print_out([t0])