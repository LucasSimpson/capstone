# describes a color, and how to write out
class Color:

    # hack to enable dual constructor
    # either Color(255, 255, 255) to draw a color
    # or Color(false) to not draw
    def __init__(self, r, g=0, b=0):
        self.render = not (not r and not g and not b)
        self.r = r
        self.g = g
        self.b = b

    # render to string
    def __str__(self):
        return "%s,%s,%s" % (self.r, self.g, self.b) if self.render else "0"