import decoder.jpeg_decoder as jpeg_decoder
from pathlib import Path
from sys import argv

if __name__ == "__main__":

    jpeg_decoder.JpegDecoder(Path(argv[1]))

    print("Program finished. Have a nice day!")
