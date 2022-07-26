import numpy as np


def bin_twos_complement(bits: str) -> int:
    """Convert a binary number to a signed integer using the two's complement."""
    if bits == "":
        return 0
    elif bits[0] == "1":
        return int(bits, 2)
    elif bits[0] == "0":
        bit_length = len(bits)
        return int(bits, 2) - (2**bit_length - 1)
    else:
        raise ValueError(f"'{bits}' is not a binary number.")


def undo_zigzag(block: np.ndarray) -> np.ndarray:
    """Takes an 1D array of 64 elements and undo the zig-zag scan of the JPEG
    encoding process. Returns a 2D array (8 x 8) that represents a block of pixels.
    """
    return np.array(
        [
            [
                block[0],
                block[1],
                block[5],
                block[6],
                block[14],
                block[15],
                block[27],
                block[28],
            ],
            [
                block[2],
                block[4],
                block[7],
                block[13],
                block[16],
                block[26],
                block[29],
                block[42],
            ],
            [
                block[3],
                block[8],
                block[12],
                block[17],
                block[25],
                block[30],
                block[41],
                block[43],
            ],
            [
                block[9],
                block[11],
                block[18],
                block[24],
                block[31],
                block[40],
                block[44],
                block[53],
            ],
            [
                block[10],
                block[19],
                block[23],
                block[32],
                block[39],
                block[45],
                block[52],
                block[54],
            ],
            [
                block[20],
                block[22],
                block[33],
                block[38],
                block[46],
                block[51],
                block[55],
                block[60],
            ],
            [
                block[21],
                block[34],
                block[37],
                block[47],
                block[50],
                block[56],
                block[59],
                block[61],
            ],
            [
                block[35],
                block[36],
                block[48],
                block[49],
                block[57],
                block[58],
                block[62],
                block[63],
            ],
        ],
        dtype=block.dtype,
    ).T  # <-- transposes the array
    """NOTE
    The array is transposed so the code above matches the (x, y) positions of the elements
    in the 8 x 8 block of pixels:
    array[x, y] = value on that pixel position
    """


# List that undoes the zig-zag ordering for a single element in a band
# (the element index is used on the list, and it returns a (x, y) tuple
# for the coordinates on the data unit)
zagzig = (
    (0, 0),
    (1, 0),
    (0, 1),
    (0, 2),
    (1, 1),
    (2, 0),
    (3, 0),
    (2, 1),
    (1, 2),
    (0, 3),
    (0, 4),
    (1, 3),
    (2, 2),
    (3, 1),
    (4, 0),
    (5, 0),
    (4, 1),
    (3, 2),
    (2, 3),
    (1, 4),
    (0, 5),
    (0, 6),
    (1, 5),
    (2, 4),
    (3, 3),
    (4, 2),
    (5, 1),
    (6, 0),
    (7, 0),
    (6, 1),
    (5, 2),
    (4, 3),
    (3, 4),
    (2, 5),
    (1, 6),
    (0, 7),
    (1, 7),
    (2, 6),
    (3, 5),
    (4, 4),
    (5, 3),
    (6, 2),
    (7, 1),
    (7, 2),
    (6, 3),
    (5, 4),
    (4, 5),
    (3, 6),
    (2, 7),
    (3, 7),
    (4, 6),
    (5, 5),
    (6, 4),
    (7, 3),
    (7, 4),
    (6, 5),
    (5, 6),
    (4, 7),
    (5, 7),
    (6, 6),
    (7, 5),
    (7, 6),
    (6, 7),
    (7, 7),
)


def print_progress(
    current: int, total: int, done: bool = False, header: str = "Progress"
) -> None:
    """Print a progress percentage on the screen. If the process is not done yet,
    the line is updated instead of moving to the next line.
    """
    if not done:
        print(f"{header}: {current}/{total} ({current * 100 / total:.2f}%)", end="\r")
    else:
        print(f"{header}: {current}/{total} ({current * 100 / total:.0f}%) DONE!")
