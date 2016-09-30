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
data = [scene_builder.new_scene().add_line(Vector(0, 0, 100), Vector(100, 0, 100), Color(255, 0, 0)).rasterize()]

Printer.print_out(data)