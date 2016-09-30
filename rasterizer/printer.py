class Printer:
    filename = "../simulator/data/data.txt"

    @classmethod
    def print_out(clz, time_frames):

        # get all lines
        lines = []
        for frame in time_frames:
            lines += frame.write_out()

        # add new line chars
        lines = map(lambda x: x + "\n", lines)

        # write out
        f = open(Printer.filename, "w")
        f.writelines(lines)
        f.close()

        print "%s lines succesfully wrote" % (len(lines))