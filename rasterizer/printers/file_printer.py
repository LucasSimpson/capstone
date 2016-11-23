from base import Printer


# prints out to a file, for injestion by simulator
class FilePrinter(Printer):
    def __init__(self, filename, *args, **kwargs):
        super(FilePrinter, self).__init__(self, *args, **kwargs)
        self.filename = filename

    def print_out(self, time_frames):

        # get all lines
        lines = []
        for frame in time_frames:
            lines += frame.write_out()

        # add new line chars
        lines = map(lambda x: x + "\n", lines)

        # write out
        f = open(self.filename, "w")
        f.writelines(lines)
        f.close()

        print "%s lines succesfully wrote" % (len(lines))
