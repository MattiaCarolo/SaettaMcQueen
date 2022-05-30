from components.App import App
from SpiralisFractalis import *
from utils import getFractalsListFromParsedJson


def main(fractals, width, height, numIterations):

    app = App(fractals, width, height, numIterations)
    app.mainloop()


if __name__ == "__main__":
    import sys

    # if there is one argument and it's not "-"
    if len(sys.argv) > 1 and sys.argv[1] != "-":
        # process each filename in input
        for filename in sys.argv[1:]:
            parsedJSON = parse(filename)
            fractals = getFractalsListFromParsedJson(parsedJSON)
            width = parsedJSON["width"]
            height = parsedJSON["height"]
            numIterations = parsedJSON["iterations"]
            """            
            i = 0
            for fractal in fractals:
               i += 1
               process_file(fractal, width, height,i-1, numIterations, get_name_index(i))
            """

            main(fractals, width, height, numIterations)
    else:
        # read contents from stdin
        eval(sys.stdin.read())
        # process_file( fract, width, height, iterations)
