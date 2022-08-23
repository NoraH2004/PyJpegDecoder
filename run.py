import decoder.jpeg_decoder as jpeg_decoder
from pathlib import Path
from sys import argv
import os
from tqdm import tqdm


if __name__ == "__main__":

    output_path = Path("../../progressivejpeg/code/output")

    for dir in [x for x in os.walk(output_path)][1:]:
        cur_dir = dir[0]
        for path in tqdm(dir[2]):
            params = Path(path).stem.split("-")

            if (
                params[3] == "progressive"
                and params[1] == "mozjpeg"
                and params[4].split("qf")[1] in ["50", "64"]
            ):
                continue
            jpeg_decoder.JpegDecoder(Path(cur_dir + "/" + path))

    print("Program finished. Have a nice day!")
